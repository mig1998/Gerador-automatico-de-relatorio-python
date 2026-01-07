def relatorio_financeiro(df):
    """
    Relatório financeiro geral
    """
    total = df["valor"].sum()
    texto = f"Total financeiro: R$ {total:.2f}"
    return texto, None


def relatorio_por_produto(df):
    """
    Relatório de vendas por produto
    """
    vendas = df.groupby("produto")["valor"].sum()
    texto = "Vendas por produto:"
    return texto, vendas


def relatorio_por_vendedor(df):
    """
    Relatório de vendas por vendedor
    """
    vendas = df.groupby("vendedor")["valor"].sum()
    texto = "Vendas por vendedor:"
    return texto, vendas