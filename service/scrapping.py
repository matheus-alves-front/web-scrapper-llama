import os
from dotenv import load_dotenv
from firecrawl import Firecrawl

load_dotenv()

class ScrappingService:
    def __init__(self):
        self.api_key = os.getenv("FIRECRAWL_API_KEY")
        self.api_url = os.getenv("FIRECRAWL_API_URL")

        self.app = Firecrawl(api_key=self.api_key, api_url=self.api_url)

    def scrape_website(self, url, collection_name):
        try:
            map_result = self.app.map(url)

            links = getattr(map_result, "links", [])
            print(f"Found {len(links)} raw links")

            url_list = [
                item["url"]
                for item in links
                if isinstance(item, dict)
                and isinstance(item.get("url"), str)
                and item["url"].startswith("http")
            ]

            # FALLBACK: sem links válidos
            if not url_list:
                print("⚠ No valid links found — using single scrape")
                single_page = self.app.scrape(url, formats=["markdown"])

                markdown_content = getattr(single_page, "markdown", None)

                if not markdown_content:
                    raise Exception("Scrape returned no markdown content.")

                collection_path = f"data/collections/{collection_name}"
                os.makedirs(collection_path, exist_ok=True)

                with open(f"{collection_path}/page_1.md", "w", encoding="utf-8") as f:
                    f.write(markdown_content)

                return {"success": True, "files": 1}

            # MULTI-PÁGINAS
            print(f"Valid links to scrape: {len(url_list)}")

            scrape_result = self.app.batch_scrape(url_list, formats=["markdown"])
            scraped_data = getattr(scrape_result, "data", [])

            collection_path = f"data/collections/{collection_name}"
            os.makedirs(collection_path, exist_ok=True)

            saved_count = 0

            for i, page in enumerate(scraped_data, start=1):
                markdown_content = getattr(page, "markdown", None)
                if not markdown_content:
                    continue

                with open(f"{collection_path}/page_{i}.md", "w", encoding="utf-8") as f:
                    f.write(markdown_content)

                saved_count += 1

            return {"success": True, "files": saved_count}

        except Exception as e:
            print("Error during scraping:", str(e))
            return {"success": False, "error": str(e)}
