import os
import matplotlib.pyplot as plt

def gerar_grafico(serie, titulo, arquivo):
    """
    Gera gráfico de barras e salva como imagem
    """
    os.makedirs("output", exist_ok=True)

    serie.plot(kind="bar")
    plt.title(titulo)
    plt.tight_layout()
    plt.savefig(arquivo)
    plt.close()