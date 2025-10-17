# Pré-processamento de PDFs

Projeto Integrador 2025 do Curso de Ciência da Computação do IFNMG Campus Montes Claros.

## Estrutura
- `src/`: funções Python reutilizáveis
- `notebooks/`: exemplos em Jupyter Notebook
- `data/input/`: documentos PDF de entrada
- `data/output/`: resultados gerados em JSON
- `results/`: entregas organizadas (prévia, final)

## Etapa 1: Consolidação de Documentos Institucionais
1. Regulamento dos Cursos de Graduação do Instituto Federal do Norte de Minas Gerais (IFNMG) - RCG2025
2. Regulamento Disciplinar Discente dos Cursos de Graduação (Nova versão 2025) 
3. Regimento Geral - RG2025
4. Regimento Interno dos Campi - RIC2025

# Etapa 2: Pré-processamento de Documentos Institucionais para RAG

Etapas do Pipeline
  1. Extração de texto bruto: remover cabeçalhos, rodapés, numeração de páginas.
  2. Normalização linguística: padronizar texto e expandir siglas.
  3. Detecção de estrutura: identificar capítulos, seções, artigos, parágrafos, incisos.
  4. Extração de tabelas: converter tabelas do PDF em formato estruturado (linhas e colunas).
  5. Deduplicação e consistência: eliminar trechos redundantes ou repetidos.
  6. Enriquecimento com metadados: acrescentar informações como doc_id, nome_doc, versão, data_publicação, páginas inicial e final.
