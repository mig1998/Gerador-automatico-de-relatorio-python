import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def gerar_pdf(titulo, texto, tabela=None, imagem=None):
    """
    Gera PDF de forma inteligente (sem páginas extras)
    """
    os.makedirs("output", exist_ok=True)

    titulo_arquivo = titulo.replace(" ", "_").lower()
    caminho_pdf = f"output/relatorio_{titulo_arquivo}.pdf"

    c = canvas.Canvas(caminho_pdf, pagesize=A4)
    largura, altura = A4

    y = altura - 50

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, titulo)
    y -= 40

    c.setFont("Helvetica", 12)
    for linha in texto.split("\n"):
        if y < 50:
            c.showPage()
            c.setFont("Helvetica", 12)
            y = altura - 50

        c.drawString(50, y, linha)
        y -= 20

    if tabela is not None:
        if y < 100:
            c.showPage()
            y = altura - 50

        c.setFont("Helvetica-Bold", 14)
        c.drawString(50, y, "Tabela de Dados")
        y -= 30

        c.setFont("Helvetica", 10)
        for chave, valor in tabela.items():
            if y < 50:
                c.showPage()
                c.setFont("Helvetica", 10)
                y = altura - 50

            c.drawString(50, y, f"{chave}: {valor}")
            y -= 15

    if imagem:
        if y < 350:
            c.showPage()
            y = altura - 50

        c.setFont("Helvetica-Bold", 14)
        c.drawString(50, y, "Gráfico")
        y -= 20

        c.drawImage(imagem, 50, y - 300, width=500, height=300)

    c.save()
    return caminho_pdf