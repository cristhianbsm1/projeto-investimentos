import textwrap
from api import Api
from utilidades import ponto_flutuante


class Menu:
    def codigo_acao(self):
        while True :
            codigo = input("Digite o código da ação:").upper()
            api = Api(codigo)
            if api.empresa_valida() is True:
                return api, codigo
            print("Código da ação inválido. Digite novamente. ")
    

    def analise(self, api): 
        dados = api.dados_basicos()
        print(f"""Análise atual\t{dados["nome"]}: 
                Setor:\t{dados["industria"]}  
                Preço:\tR${dados["preco"]}
                Máxima 52 semanas:\tR${dados["max_52"]} 
                Mínima 52 semanas:\tR${dados["min_52"]}
                Valor pago em dividendos por ação no último ano:\tR${ponto_flutuante(dados["dy_12m_reais"])}   
                Dividendos:\t{ponto_flutuante(dados["dy_percentual"])}%
                P/VP:\t{ponto_flutuante(dados["pvp"])}x 
                P/L:\t{ponto_flutuante(dados["pl"])}x 
                ROE:\t{ponto_flutuante(dados["roe_percentual"])}%
                """) 

    def analisar_bancos(self, api):
        dados = api.dados_bancos()
        print(f"""ANÁLISE ATUAL\t—\t{dados["nome"]}
                Preço atual:\tR${dados["preco"]}
                Máxima 52 semanas:\tR${dados["max_52"]} 
                Mínima 52 semanas:\tR${dados["min_52"]} 
                P/VP:\t{ponto_flutuante(dados["pvp"])}x
                P/L:\t{ponto_flutuante(dados["pl"])}x 
                Valor pago em dividendos por ação no último ano:\tR${ponto_flutuante(dados["dy_12m_reais"])}
                Dividendos:\t{ponto_flutuante(dados["dy_percentual"])}%
                Índice de eficiência operacional:\t{ponto_flutuante(dados["eficiencia"])}%
                ROE:\t{ponto_flutuante(dados["roe_percentual"])}%
                NPL 90+:\t{dados["npl90"]}% 
                Cobertura Estágio 3:\t{dados["indice_cobertura"]}% 
                Custo do crédito:\t{ponto_flutuante(dados["custocredito"])} milhões
                Índice de Basileia:\t{dados["basileia"]}%
                """)

    def analisar_seguradora(self, api):  
        dados = api.dados_seguradora()
        print(f"""Análise focada em holdings de seguros:
            ANÁLISE ATUAL\t—\t{dados["nome"]}
            Preço atual:\tR${dados["preco"]}
            Máxima 52 semanas:\tR${dados["max_52"]} 
            Mínima 52 semanas:\tR${dados["min_52"]} 
            ROE:\t{ponto_flutuante(dados["roe_percentual"])}%
            Valor pago em dividendos por ação no último ano:\tR${ponto_flutuante(dados["dy_12m_reais"])}
            Dividendos:\t{ponto_flutuante(dados["dy_percentual"])}%
            P/VP:\t{ponto_flutuante(dados["pvp"])}x
            P/L:\t{ponto_flutuante(dados["pl"])}x
            Payout:\t{ponto_flutuante(dados["payout"])}%
            Crescimento do Lucro:\t{ponto_flutuante(dados["cresc_lucro"])}%
            Crescimento dos dividendos:\t{ponto_flutuante(dados["cresc_dividendos"])}%
            Fluxo de caixa operacional\t(FCO): {ponto_flutuante(dados["fco_bilhoes"])} bilhões
            Dívida / Patrimônio Líquido:\t{ponto_flutuante(dados["alavancagem"])}x
            """)
    
    def analisar_eletrica(self, api):
        dados = api.dados_eletricas()
        print(f"""ANÁLISE ATUAL\t—\t{dados["nome"]}:
                Preço atual:\tR${dados["preco"]}
                Máxima 52 semanas:\tR${dados["max_52"]} 
                Mínima 52 semanas:\tR${dados["min_52"]}
                Valor pago em dividendos por ação no último ano:\tR${ponto_flutuante(dados["dy_12m_reais"])} 
                Dividendos:\t{ponto_flutuante(dados["dy_percentual"])}%
                ROE:\t{ponto_flutuante(dados["roe_percentual"])}%
                P/VP:\t{ponto_flutuante(dados["pvp"])}x
                P/L:\t{ponto_flutuante(dados["pl"])}x
                Dívida Líquida/EBITDA:\t{ponto_flutuante(dados["div_liq_ebitda"])}x
                RAP por ação:\tR${ponto_flutuante(dados["rap_por_acao"])}
                RAP por real investido:\tR${ponto_flutuante(dados["rap_marketcap"])}
                EV/RAP:\t{ponto_flutuante(dados["ev_rap"])}x
                """)

    def analisar_saneamento(self, api):
        dados = api.dados_saneamento()
        print(f"""ANÁLISE ATUAL\t————\t{dados["nome"]}:        
            Preço atual:\tR${dados["preco"]}
            Máxima 52 semanas:\tR${dados["max_52"]} 
            Mínima 52 semanas:\tR${dados["min_52"]}
            Valor pago em dividendos por ação no último ano:\tR${ponto_flutuante(dados["dy_12m_reais"])} 
            Dividendos:\t{ponto_flutuante(dados["dy_percentual"])}%
            P/VP:\t{ponto_flutuante(dados["pvp"])}x
            P/L:\t{ponto_flutuante(dados["pl"])}x
            Payout:\t{ponto_flutuante(dados["payout"])}%                
            Dívida Líquida/EBITDA:\t{ponto_flutuante(dados["div_liq_ebitda"])}x
            Margem EBITDA:\t{ponto_flutuante(dados["margem_ebitda"])}%
            ROIC:\t{ponto_flutuante(dados["roic"])}%
            ROE:\t{ponto_flutuante(dados["roe_percentual"])}%
            Fluxo de Caixa Livre:\t{ponto_flutuante(dados["fcl"])} bilhões
            Cobertura de Juros:\t{ponto_flutuante(dados["cobertura_juros"])}x
            """)

    def menu_principal(self):
        opcoes = """
        [a]\tAnálise básica
        [as]\tAnálise por setor
        [s]\tSair
        => 
        """
        return input(textwrap.dedent(opcoes))

    def menu_setores(self):
        opcoes = """
        [ab]\tAnalisar bancos
        [ae]\tAnalisar elétrica
        [as]\tAnalisar holdings de seguros
        [asa]\tAnalisar saneamento
        [m]\tMenu
        """
        return input(textwrap.dedent(opcoes))

    def selecionar_analise_setor(self):
        opcao = self.menu_setores()
        if opcao == "ab":
            print("Análise do setor bancário: na V1, a análise utiliza dados complementares armazenados em arquivos CSV. Por isso, atualmente estão disponíveis apenas Itaú, Banco do Brasil e Bradesco.")
            api, codigo = self.codigo_acao()
            if codigo in ["BBAS3", "ITUB4", "BBDC4"]:
                self.analisar_bancos(api)
            else:
                print("Essa ação não esta disponivel para analise de bancos, escolha uma das opcoes disponiveis: BBAS3, ITUB4, BBDC4")
        elif opcao == "as":
            api, codigo = self.codigo_acao()
            self.analisar_seguradora(api)  
        elif opcao == "ae":
            print("Análise do setor elétrico: na V1, a análise utiliza dados complementares das concessões armazenados em arquivos CSV. Por isso, atualmente estão disponíveis apenas Taesa e ISA Energia.")
            api, codigo = self.codigo_acao()
            if codigo in ["TAEE11", "TAEE4", "ISAE4"]:
                self.analisar_eletrica(api)
            else:
                print("Essa ação não esta disponivel para analise de eletricas, escolha uma das opcoes disponiveis: TAEE11, TAEE4, ISAE4")
        elif opcao == "asa":
            api, codigo = self.codigo_acao()
            self.analisar_saneamento(api)    
        elif opcao == "m":
            return
        else:
            print("\nOperação inválida. Por favor selecione novamente a operação desejada. ")

    def selecionar_opcao(self, opcao):
        if opcao == "a":
            api, codigo = self.codigo_acao()
            self.analise(api)
        elif opcao == "as":
            self.selecionar_analise_setor()
        else:
            print("\n Operação inválida. Por favor selecione novamente a operação desejada. ")