from dados.data import Dados

class Analisar():
    def __init__(self, codigo):
        self.codigo = codigo
        self.dados = Dados(self.codigo)
    
    def empresa_valida(self):    
        return self.dados.informacoes.get("longName") is not None


    def analise_basica(self):
        dados = self.dados.dados_basicos()
        dic = {
            "dy_percentual" : self.multiplicacao(self.divisao(dados["dy_12m_reais"], dados["preco"]), 100),
            "roe_percentual" : self.multiplicacao(dados["roe_fracao"], 100)
        }
        dic.update(dados)
        return dic

    def analisar_bancos(self):
        dados = self.dados.dados_banco()
        dados.update(self.analise_basica())
        ind_eficiencia = self.calcular_indice_eficiencia()        
        dic = {
            "eficiencia" : ind_eficiencia,
        }
        dic.update(dados)
        return dic

    def analisar_eletricas(self):
        dados = self.dados.dados_eletrica()
        dados.update(self.analise_basica())
        lucro_trimestral = self.dados.indicadores("Net Income", "quarterly_income_stmt")      
        divida_liquida = self.subtracao(dados["totaldebt"], dados["totalcash"])
        participacao_decimal = self.divisao(dados["participacao"], 100)    
        rap_por_concessao = self.multiplicacao(          
            dados["rap_milhoes"],
            participacao_decimal                
        )
        rap_total = self.multiplicacao(       
            self.somar_serie(rap_por_concessao),        
            1_000_000                           
        ) 
        quantidade_acoes = self.divisao(dados['mkt_cap'], dados['preco'])
        dic = {
            "lucro_trimestral" : lucro_trimestral,      
            "div_liq_ebitda" : self.divisao(divida_liquida, dados['ebitda']),             
            "rap_por_acao" : self.divisao(rap_total, quantidade_acoes),               
            "rap_marketcap" : self.divisao(rap_total, dados['mkt_cap']),                 
            "ev_rap" : self.divisao(self.adicao(dados['mkt_cap'], divida_liquida), rap_total),     
        }
        dic.update(dados)
        return dic

    def analisar_seguradora(self):
        lucro = self.dados.lucro_ultimos_anos("Net Income")
        dados = self.dados.dados_seguradora()
        dados.update(self.analise_basica())
        dic = {
            "fco_bilhoes" : self.divisao(dados["fco"], 1e9),
            "alavancagem" : self.divisao(dados["divida"], dados["patrim_liquid"]),
            "cresc_lucro": self.multiplicacao(self._cagr(lucro), 100),
            "cresc_dividendos": self.multiplicacao(self._cagr(dados["div"]), 100),
            "payout" : self.multiplicacao(self.divisao(self.dados.obter_indicador("dividendRate"), self.dados.obter_indicador("trailingEps")),100),
        }
        dic.update(dados)
        return dic

    def analisar_saneamento(self):
        dados = self.dados.dados_saneamento()
        dados.update(self.analise_basica())
        taxa_imposto = 0.34 
        capital_investido = self.subtracao(self.adicao(dados["total_debito"], dados["patrim_liquid"]), dados["caixa_equivalentes"])   
        nopat = self.multiplicacao(dados["ebit"], self.subtracao(1, taxa_imposto))       
        capex_bilhoes = self.divisao(dados["capex"], 1e9)   
        fco_bilhoes = self.divisao(dados["fco"], 1e9)
        dic = {
            "payout" : self.multiplicacao(self.divisao(self.dados.obter_indicador("dividendRate"), self.dados.obter_indicador("trailingEps")), 100),
            "roic" : self.multiplicacao(self.divisao(nopat, capital_investido), 100),
            "div_liq_ebitda" : self.divisao(self.subtracao(dados["total_debito"], dados["total_cash"]), dados["ebitda"]),
            "margem_ebitda" : self.multiplicacao(self.divisao(dados["ebitda"], dados["receita"]), 100), 
            "fcl" : self.subtracao(fco_bilhoes, self.valor_absoluto(capex_bilhoes)),
            "cobertura_juros" : self.divisao(dados["ebit"], self.valor_absoluto(dados["juros"])),      
        }
        dic.update(dados)
        return dic
     
    def adicao(self, primeiro_valor, segundo_valor):
        if primeiro_valor is None or segundo_valor is None:
            return None
        return primeiro_valor + segundo_valor
    
    def subtracao(self, primeiro_valor, segundo_valor):
        if primeiro_valor is None or segundo_valor is None:
            return None
        return primeiro_valor - segundo_valor   
     
    def multiplicacao(self, primeiro_valor, segundo_valor):
        if primeiro_valor is None or segundo_valor is None:
            return None
        return primeiro_valor * segundo_valor
    
    def divisao(self, primeiro_valor, segundo_valor):
        if primeiro_valor is None or segundo_valor in (None, 0):
            return None
        return primeiro_valor / segundo_valor
    
    def somar_serie(self, serie):
        if serie is None:
            return None
        return serie.sum()
        
    def _cagr(self, serie):                                 
        try:
            serie = serie.dropna().sort_index()
            if len(serie) < 2:
                return None
            
            inicio = serie.iloc[0]
            fim = serie.iloc[-1]
            if inicio <= 0 or fim <= 0:
                return None
            
            return (serie.iloc[-1] / serie.iloc[0]) ** (1/(len(serie)-1)) - 1
        except:
            return None
  
    def calcular_indice_eficiencia(self) -> float | None:
        receita = self.dados.indicadores("Total Revenue","income_stmt")         
        depreciacao_amortizacao = self.dados.indicadores("Depreciation And Amortization In Income Statement","income_stmt")
        
        for linha in ["Operating Expense", "Selling General And Administration"]:
            valor = self.dados.indicadores(linha, "income_stmt")
            if valor is not None:
                return self.multiplicacao(self.divisao(self.subtracao(valor, depreciacao_amortizacao), receita), 100)
        return None
    
    def valor_absoluto(self, valor):
        if valor is None:
            return None
        return abs(valor)
            


