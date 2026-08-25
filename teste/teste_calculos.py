import pytest
import pandas as pd
from analysis import Analisar


def adicao():
    assert Analisar("BBAS3").adicao(5,5) == 10
    assert Analisar("BBAS3").adicao(10, None) is None
    assert Analisar("BBAS3").adicao(None, 10) is None

def subtracao():
    assert Analisar("BBAS3").subtracao(20,10) == 10
    assert Analisar("BBAS3").subtracao(20,None) is None
    assert Analisar("BBAS3").subtracao(None,10) is None
    
def divisao():
    assert Analisar("BBAS3").divisao(20,2) == 10
    assert Analisar("BBAS3").divisao(None,2) is None
    assert Analisar("BBAS3").divisao(20,0) is None

def multiplicacao():
    assert Analisar("BBAS3").multiplicacao(5,2) == 10
    assert Analisar("BBAS3").multiplicacao(5,None) is None
    assert Analisar("BBAS3").multiplicacao(None,10) is None
    
def somar_serie():
    serie = pd.Series([10,20,30])
    assert Analisar("BBAS3").somar_serie(serie) == 60
    assert Analisar("BBAS3").somar_serie(None) is None

def cagr():
    serie = pd.Series([100,110,121])                             
    assert Analisar("BBAS3")._cagr(serie) == pytest.approx(0.10)
    
def valor_absoluto():
    assert Analisar("BBAS3").valor_absoluto(10) == 10
    assert Analisar("BBAS3").valor_absoluto(-10) == 10
    assert Analisar("BBAS3").valor_absoluto(None) is None        

adicao()
subtracao()
divisao()
multiplicacao()
somar_serie()
cagr()