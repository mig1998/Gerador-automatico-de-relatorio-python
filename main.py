from services.data_service import carregar_dados
from services.report_service import (
    relatorio_financeiro,
    relatorio_por_produto,
    relatorio_por_vendedor
)
from services.chart_service import gerar_grafico
from services.pdf_service import gerar_pdf


# Caminho do Excel
arquivo_excel = "data/vendas.xlsx"

# financeiro | produto | vendedor
tipo_relatorio = "produto"

# Carregar dados
df = carregar_dados(arquivo_excel)

# Escolher relatório
if tipo_relatorio == "financeiro":
    texto, serie = relatorio_financeiro(df)
    gerar_pdf("Relatório Financeiro", texto)

elif tipo_relatorio == "produto":
    texto, serie = relatorio_por_produto(df)
    gerar_grafico(serie, "Vendas por Produto", "output/grafico_produto.png")
    gerar_pdf(
        "Relatório por Produto",
        texto,
        tabela=serie,
        imagem="output/grafico_produto.png"
    )

elif tipo_relatorio == "vendedor":
    texto, serie = relatorio_por_vendedor(df)
    gerar_grafico(serie, "Vendas por Vendedor", "output/grafico_vendedor.png")
    gerar_pdf(
        "Relatório por Vendedor",
        texto,
        tabela=serie,
        imagem="output/grafico_vendedor.png"
    )

else:
    print("Tipo de relatório inválido")