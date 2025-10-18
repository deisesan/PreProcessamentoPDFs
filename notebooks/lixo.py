# mostra os primeiros 1000 caracteres
# print(f"\nTexto extraído ({len(texto_bruto)} caracteres):")
# print(texto_bruto[:1000])

# Se estiver processando vários PDFs
# Montar uma lista de documentos enriquecidos
import glob

todos_docs = []

for caminho in glob.glob("pdfs/*.pdf"):
    with pdfplumber.open(caminho) as pdf:
        texto = "\n".join(pagina.extract_text() for pagina in pdf.pages if pagina.extract_text())
        doc = {
            "metadados": {
                "doc_id": Path(caminho).stem.upper(),
                "nome_doc": Path(caminho).name,
                "versao": "1.0",
                "data_publicacao": None,  # pode ser extraída depois
                "paginas_inicial": 1,
                "paginas_final": len(pdf.pages),
            },
            "texto_limpo": texto
        }
        todos_docs.append(doc)