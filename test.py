import yfinance as yf

acao = yf.Ticker("BBAS3.SA")
informacoes = acao.info
mostrar = acao.dividends.resample("YE").sum().tail(5)
print(mostrar)
