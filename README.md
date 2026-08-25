# Projeto Investimentos V1

O Projeto Investimentos é uma aplicação em Python para análise de ações da bolsa brasileira.

# Sobre o projeto

O projeto busca organizar indicadores fundamentalistas e apresentar análises básicas e específicas para diferentes setores, facilitando a consulta e comparação de informações das empresas.

Atualmente, o projeto possui análises específicas para os setores bancário, elétrico, saneamento e seguradoras.


# Funcionalidades
- Consulta de dados básicos de empresas
- Cálculo de indicadores fundamentalistas
- Análise de bancos
- Análise de empresas de energia elétrica
- Análise de empresas de saneamento
- Análise de seguradoras
- Tratamento e formatação dos dados para apresentação
- Testes automatizados das principais funções   

# Tecnologias 
- Python ——— linguagem principal
- Pandas ——— manipulação e análise de dados
- yfinance ——— obtenção de dados financeiros    
- Pytest ——— testes automatizados
- CSV ——— armazenamento de dados complementares

# Estrutura do projeto


projeto_investimentos_v1/
    main.py                 >       Arquivo principal responsável por iniciar a aplicação.
    api.py                  >       Organiza e disponibiliza os dados para a aplicação
    analysis.py             >       Realiza os cálculos e a análise dos indicadores fundamentalistas.
    utilidades.py           >       Funções auxiliares utilizadas pelo projeto. 

    dados/
        data.py             >       Responsável pela obtenção e organização dos dados financeiros.

    interface/
        menu.py             >       Contém a interface de interação com o usuário.

    bancos/
        dados_bancos.csv        >       Dados complementares utilizados na análise de bancos.
        
    concessoes/
        taesa.csv               >       Dados das concessões da Taesa.
        isa.csv                 >       Dados das concessões da ISA Energia.
        teste/
        teste.py                >       Contém os testes automatizados do projeto.
        teste_calculos.py       >       Testes dos cálculos e operações.    
        teste_estrutura.py      >       Testes da estrutura e funcionamento básico dos módulos.

    requirements.txt            >       Lista as bibliotecas utilizadas no projeto.
    .gitignore                  >       Define arquivos e pastas que não devem ser enviados ao Git.
    README.md                   >       Documentação do projeto.

Na V1, a análise bancária está disponível para Itaú, Banco do Brasil e Bradesco. A análise de empresas elétricas está disponível para Taesa e ISA Energia, devido à utilização de dados complementares armazenados em arquivos CSV.

# Como executar

Clone o repositório:
- git clone https://github.com/cristhianbsm1/projeto-investimentos.git

Entre na pasta do projeto:
- cd projeto_investimentos_v1

Instale as dependências:
- pip install -r requirements.txt

Execute a aplicação:
- python main.py

# Testes

Com o terminal aberto na pasta projeto_investimentos_v1, execute o teste desejado:
- Testes gerais da aplicação
python -m teste.teste
- Testes dos cálculos e operações utilizadas nas análises.
python -m teste.teste_calculos
- Testes da estrutura e do funcionamento básico dos módulos.
python -m teste.teste_estrutura

# Demonstração

A aplicação funciona através do terminal. O usuário interage com a interface de menu para selecionar o tipo de análise e, em seguida, informa o código da empresa que deseja analisar.

Exemplo:
python main.py
[a]     Análise básica
[as]    Análise por setor
[s]     Sair
=> 
a
Digite o código da ação:BBAS3
Análise atual   Banco do Brasil S.A.: 
                Setor:  Banks - Regional  
                Preço:  R$18.43
                Máxima 52 semanas:      R$27.81 
                Mínima 52 semanas:      R$17.79
                Valor pago em dividendos por ação no último ano:        R$0.55   
                Dividendos:     2.98%
                P/VP:   0.58x 
                P/L:    8.57x 
                ROE:    10.55%
                

[a]     Análise básica
[as]    Análise por setor
[s]     Sair