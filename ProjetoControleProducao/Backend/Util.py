from datetime import datetime

class Validacao():
    @staticmethod
    def validarTexto(texto, qtdPalavras):
        if texto == None:
            return False
        if texto == "":
            return False
        if len(texto) > qtdPalavras:
            return False
        if len(texto) == texto.count(' '):
            return False
        return True
    
    @staticmethod
    def validarValor(valorTexto):
        try:
            valor = float(valorTexto)
            if valor == None:
                return False
            if valor == 0 or valor < 0:
                return False
            return True    
        except:
            return False