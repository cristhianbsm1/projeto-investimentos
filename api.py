from analysis import Analisar


class Api:
    def __init__(self, codigo):
        self.analisador = Analisar(codigo)
        
    def empresa_valida(self):
        return self.analisador.empresa_valida()    
        
    def dados_basicos(self):
        return self.analisador.analise_basica()

    def dados_bancos(self):
        return self.analisador.analisar_bancos()
    
    def dados_seguradora(self):
        return self.analisador.analisar_seguradora()
    
    def dados_eletricas(self):
        return self.analisador.analisar_eletricas()
    
    def dados_saneamento(self):
        return self.analisador.analisar_saneamento()