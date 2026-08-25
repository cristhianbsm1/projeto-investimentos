import pandas as pd
import yfinance as yf

class Dados():
    def __init__(self, codigo):
        self.codigo = codigo
        self.acao = yf.Ticker(self.codigo + ".SA")
        self.informacoes = self.acao.info
        
    def dados_basicos(self):
        return{
        "nome" : self.obter_indicador('longName'),
        "preco" : self.obter_indicador('currentPrice'),
        "max_52" : self.obter_indicador('fiftyTwoWeekHigh'),
        "min_52" :  self.obter_indicador('fiftyTwoWeekLow'),
        "pvp" : self.obter_indicador('priceToBook'),
        "pl" : self.obter_indicador('trailingPE'),
        "dy_12m_reais" : self.dy_12m_reais(),
        "roe_fracao" : self.obter_indicador('returnOnEquity'),
        "industria" : self.obter_indicador('industry')
        }
    
    def dados_banco(self):
        df = pd.read_csv("bancos/dados_bancos.csv")
        banco = df[df["Banco"] == (self.codigo + ".SA")]
        dic = {
            "custocredito" : banco["Custo_Credito"].iloc[0],     
            "npl90" : banco["NPL_90"].iloc[0],
            "basileia" : banco["Basileia"].iloc[0],
            "indice_cobertura" : banco["Cobertura_Stage3"].iloc[0]
        }
        return dic
    
    def dados_eletrica(self):
        arquivos_concessoes = {
            "TAEE11" : "taesa",
            "TAEE4" : "taesa",
            "ISAE4": "isa"
        }
        df = pd.read_csv(f"concessoes/{arquivos_concessoes[self.codigo]}.csv")        
        dic = {
            "totaldebt" : self.obter_indicador('totalDebt'),
            "totalcash" : self.obter_indicador('totalCash'),
            "rap_milhoes" : df["rap_milhoes"],
            "participacao" : df["participacao"],
            "mkt_cap" : self.obter_indicador('marketCap'),
            "ebitda" : self.obter_indicador('ebitda'),
            "lucro_anual" : self.indicadores("Net Income", "income_stmt")      
        }       
        return dic
    
    def dados_seguradora(self):   
        dic = {
            "div" : self.acao.dividends.resample("YE").sum().tail(5),
            "patrim_liquid" : self.indicadores("Stockholders Equity","balance_sheet"),
            "divida" : self.indicadores("Total Liabilities Net Minority Interest","balance_sheet"),
            "fco" : self.indicadores("Operating Cash Flow","cashflow")
        }
        return dic
    
    def dados_saneamento(self):
        dic = {
            "ebit" : self.indicadores("EBIT","financials"),
            "total_debito" : self.obter_indicador('totalDebt'),   
            "total_cash" : self.obter_indicador('totalCash'),   
            "caixa_equivalentes" : self.indicadores("Cash And Cash Equivalents","balance_sheet"),     
            "patrim_liquid" : self.indicadores("Stockholders Equity","balance_sheet"),           
            "ebitda" : self.obter_indicador('ebitda'),
            "receita" : self.obter_indicador('totalRevenue'),
            "juros" : self.indicadores("Interest Expense","financials"),
            "fco" : self.indicadores("Operating Cash Flow","cashflow"),
            "capex" : self.indicadores("Capital Expenditure","cashflow")
        }
        return dic
        
    def indicadores(self, linha, indicador, indice_coluna=0):
        try:
            dados = getattr(self.acao, indicador)
            valor = dados.loc[linha].iloc[indice_coluna]
        except (KeyError, IndexError):
            return None         
        if pd.isna(valor):
            return None
        return valor
    
    def obter_indicador(self, chave):
        valor = self.informacoes.get(chave)
        if valor is None or pd.isna(valor):
            return None
        return valor         
    
    def dy_12m_reais(self):
        historico = self.acao.dividends                                                       
        um_ano_atras = pd.Timestamp.now(tz='America/Sao_Paulo') - pd.DateOffset(years=1)       
        try:
            dy_12m_reais = historico[historico.index > um_ano_atras].sum()   
        except (KeyError, IndexError):
            return None
        if pd.isna(dy_12m_reais):
            return None
        return dy_12m_reais  
    
    def lucro_ultimos_anos(self, linha, anos=5):
        try:
            valores = self.acao.income_stmt.loc[linha]
            return valores.head(anos)
        except KeyError:
            return None    
