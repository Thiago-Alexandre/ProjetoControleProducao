from Datetime import datetime

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
    def validarValor(valor):
        if valor == None:
            return False
        if not isinstance(valor , float):
            return False
        if valor == 0:
            return False
        return True