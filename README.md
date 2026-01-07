# Gerador-automatico-de-relatorio-python

📊 Gerador Automático de Relatórios em Python
Projeto em Python que realiza leitura de dados em Excel, limpeza automática, análise, geração de gráficos e criação de relatórios em PDF, tudo de forma automatizada.

Projeto desenvolvido para estudos e portfólio, com foco em automação de dados e organização de código em services.

Pode ser executado 100% no celular (Pydroid 3).

🚀 Funcionalidades
📂 Leitura de arquivos Excel (.xlsx)
🧹 Limpeza automática dos dados
📈 Análise financeira
📊 Gráficos automáticos (Matplotlib)
📄 Relatórios em PDF (ReportLab)
🗂 Código organizado em services
⚙ Escolha do tipo de relatório via variável
📁 Estrutura do Projeto


GeradorRelatorios/
│
├── main.py
│
├── services/
│   ├── data_service.py
│   ├── report_service.py
│   ├── chart_service.py
│   └── pdf_service.py
│
├── data/
│   └── vendas.xlsx
│
└── output/
    ├── grafico_produto.png
    ├── grafico_vendedor.png
    └── relatorio_*.pdf
    
🧠 Arquitetura do Projeto
O projeto segue o princípio de separação de responsabilidades, onde cada parte do sistema tem uma função clara:
Camada
Responsabilidade
main.py

Controla o fluxo da aplicação
data_service.py

Leitura e limpeza dos dados
report_service.py

Regras de negócio e análises
chart_service.py

Geração de gráficos
pdf_service.py

Criação do PDF


Instale os pacotes abaixo no Pydroid 3 ou no seu ambiente Python:

pip install pandas matplotlib reportlab openpyxl

📊 Formato do Excel esperado
O arquivo vendas.xlsx deve conter as seguintes colunas:
produto vendedor valor
Produto A João   100
Produto B Maria  200

Os nomes das colunas não podem mudar.

▶ Como executar o projeto

Coloque o arquivo Excel em:
data/vendas.xlsx
No arquivo main.py, escolha o tipo de relatório:

Python
tipo_relatorio = "produto"
Opções disponíveis:
"financeiro"
"produto"
"vendedor"

Execute:
python main.py
📄 Relatórios Gerados
Os arquivos PDF são salvos automaticamente em:
output/

Exemplo:
relatorio_relatorio_por_produto.pdf
relatorio_relatorio_financeiro.pdf

Cada relatório pode conter:
Texto explicativo
Tabela de dados
Gráfico de barras
🛠 Tecnologias Utilizadas

Python
Pandas – manipulação de dados
Matplotlib – geração de gráficos
ReportLab – criação de PDF
Excel (.xlsx) como fonte de dados

📱 Execução no celular
Este projeto pode ser executado diretamente no celular usando:
Pydroid 3 (Android)
Ideal para quem:
não possui computador
quer aprender Python na prática
deseja criar projetos reais no celular

🎯 Próximas melhorias (ideias)
Escolha do tipo de relatório via input()
Geração de múltiplos PDFs automaticamente
Logs de execução
Dashboard em vez de PDF
Interface gráfica simples
Exportar para CSV ou HTML

## 👨‍💻 Autor
Projeto desenvolvido por FusionCode
Desenvolvedor focado em automação, fullstack