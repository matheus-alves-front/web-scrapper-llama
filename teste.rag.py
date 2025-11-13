print("Tentando importar RAGService...")
try:
    from service.rag import RAGService
    print("SUCESSO! A classe RAGService foi importada.")
    
    # Opcional: Tenta criar uma instância para ver se o __init__ tem erros
    # print("Tentando instanciar RAGService...")
    # service = RAGService()
    # print("SUCESSO! Instância criada.")

except ImportError as e:
    print(f"FALHA NA IMPORTAÇÃO: {e}")
except Exception as e:
    print(f"ERRO GERAL AO IMPORTAR: {e}")

print("Teste concluído.")
