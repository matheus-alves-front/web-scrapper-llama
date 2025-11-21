import os
import re
from typing import List, Optional

from dotenv import load_dotenv
from firecrawl import Firecrawl

load_dotenv()


class ScrappingService:
    def __init__(self) -> None:
        self.api_key = os.getenv("FIRECRAWL_API_KEY")
        if not self.api_key:
            raise ValueError("API Key do Firecrawl não encontrada. Verifique seu arquivo .env")
        
        self.app = Firecrawl(api_key=self.api_key)

    def _clean_markdown(self, markdown: str) -> str:
        """
        Limpa lixo típico de página de doc:
        - Botões tipo 'Copy page', 'Ask AI', etc.
        - Blocos muito óbvios de navegação.
        Ajuste essas regex conforme você ver o padrão dos seus arquivos.
        """
        text = markdown

        # Remove linhas com 'Copy page' ou 'Ask AI' ou similares
        text = re.sub(r"(?i)^.*(copy page|ask ai|edit this page).*$", "", text, flags=re.MULTILINE)

        # Remove blocos de navegação no topo/rodapé se seguirem um padrão (ajuste conforme necessário)
        # Exemplo bem genérico, então mantenha simples:
        text = re.sub(r"(?i)^.*(back to top).*$", "", text, flags=re.MULTILINE)

        # Remove múltiplas quebras de linha consecutivas (deixa no máximo 2)
        text = re.sub(r"\n{3,}", "\n\n", text)

        return text.strip()

    def scrape_website(
        self,
        url: str,
        collection_name: str,
        include_paths: Optional[List[str]] = None,
        exclude_paths: Optional[List[str]] = None,
        limit: int = 30,
    ):
        """
        Faz o crawl de um site de docs e salva arquivos markdown limpos em data/collections/<collection_name>.

        - url: URL raiz (ex: 'https://docs.agno.com')
        - include_paths: paths que você quer focar (ex: ['/concepts/agents', '/concepts/teams'])
        - exclude_paths: paths pra ignorar (ex: ['/changelog', '/blog'])
        """
        try:
            print(f"🚀 Iniciando crawl para: {url}")

            scrape_options: dict = {
                # queremos markdown pra jogar direto no RAG
                "formats": ["markdown"],
                # já ajuda a tirar header/menu/rodapé
                "onlyMainContent": True,
            }

            # Só passa include/exclude se tiver algo, pra não limitar demais sem querer
            if include_paths:
                scrape_options["includePaths"] = include_paths
            if exclude_paths:
                scrape_options["excludePaths"] = exclude_paths

            scraped_data = self.app.crawl(
                url=url,
                limit=limit,
                scrape_options=scrape_options,
            )

            if not scraped_data or not hasattr(scraped_data, "data") or not scraped_data.data:
                raise Exception(
                    "O processo de crawl não retornou nenhum dado. "
                    "O site pode ser protegido ou incompatível com a extração automática."
                )

            collection_path = os.path.join("data", "collections", collection_name)
            os.makedirs(collection_path, exist_ok=True)

            saved_count = 0
            for i, page in enumerate(scraped_data.data, start=1):
                markdown = getattr(page, "markdown", None)

                if not markdown:
                    source_url = getattr(page, "metadata", {}).get("sourceURL", "desconhecida")
                    print(f"⚠️ Página {source_url} ignorada (sem conteúdo markdown).")
                    continue

                # Limpeza custom
                markdown = self._clean_markdown(markdown)

                # Filtro simples de tamanho (pra tirar lixo tipo páginas só com título)
                if len(markdown) < 200:
                    source_url = getattr(page, "metadata", {}).get("sourceURL", "desconhecida")
                    print(f"⚠️ Página {source_url} ignorada (conteúdo muito curto).")
                    continue

                file_name = f"page_{i}.md"
                file_path = os.path.join(collection_path, file_name)

                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(markdown)

                saved_count += 1
                print(f"✅ Página salva: {file_path}")

            if saved_count == 0:
                return {"success": False, "error": "Nenhum conteúdo markdown válido foi extraído das páginas encontradas."}

            return {"success": True, "files": saved_count}

        except Exception as e:
            print(f"❌ Erro durante o crawl: {str(e)}")
            return {"success": False, "error": str(e)}
