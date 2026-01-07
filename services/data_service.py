import pandas as pd

def carregar_dados(caminho):
    """
    Lê o arquivo Excel e faz limpeza básica
    """
    df = pd.read_excel(caminho)

    df.columns = df.columns.str.strip().str.lower()
    df = df.dropna()

    return df