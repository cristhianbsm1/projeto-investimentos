from interface.menu import Menu
from api import Api



Menu().analise(Api("BBAS3"))

Menu().analisar_bancos(Api("BBAS3"))

Menu().analisar_eletrica(Api("ISAE4"))

Menu().analisar_seguradora(Api("BBSE3"))

Menu().analisar_saneamento(Api("SAPR4"))