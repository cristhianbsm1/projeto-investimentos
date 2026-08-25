from api import Api

def teste_basico():
    teste = Api("BBAS3").dados_basicos()
    lista_basica = ["nome", "industria", "preco", "max_52", "min_52", "dy_12m_reais", "dy_percentual", "pvp", "pl", "roe_percentual"]

    for campo in lista_basica:
        assert campo in teste, f"O valor {campo} nao aparece no dicionario de dados_basicos"

def teste_bancos():
    teste = Api("BBAS3").dados_bancos()
    lista_bancos = ["eficiencia", "npl90", "indice_cobertura", "custocredito", "basileia" ]

    for campo in lista_bancos:
       assert campo in teste, f"O valor {campo} nao aparece no dicionario de dados_bancos"

def teste_seguradora():
    teste = Api("BBSE3").dados_seguradora()
    lista_seguradora = ["payout", "cresc_lucro", "cresc_dividendos", "fco_bilhoes", "alavancagem"]

    for campo in lista_seguradora:
      assert campo in teste, f"O valor {campo} nao aparece no dicionario de dados_seguradora"

def teste_eletricas():
    teste = Api("ISAE4").dados_eletricas()
    lista_eletricas = ["div_liq_ebitda", "rap_por_acao", "rap_marketcap", "ev_rap"]

    for campo in lista_eletricas:
        assert campo in teste, f"O valor {campo} nao aparece no dicionario de dados_eletricas"

def teste_saneamento():
    teste = Api("SBSP3").dados_saneamento()
    lista_saneamento = ["payout", "div_liq_ebitda", "margem_ebitda", "roic", "fcl", "cobertura_juros"]

    for campo in lista_saneamento:
        assert campo in teste, f"O valor {campo} nao aparece no dicionario de dados_saneamento"

teste_basico()
teste_bancos()
teste_seguradora()
teste_eletricas()
teste_saneamento()