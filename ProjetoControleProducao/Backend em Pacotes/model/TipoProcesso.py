import sys 
import os
sys.path.append(os.path.abspath("./"))
from config.Config import *

class TipoProcesso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    descricao = db.Column(db.String(250))

    # toString da classe TipoProcesso
    def __str__(self):
        return "Tipo de Processo: id:" + str(self.id) + " | Nome: "+ self.nome + " | Descrição: "+ self.descricao

    # retorna classe TipoProcesso em formato JSON
    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "descricao": self.descricao
        }

# método main da classe TipoProcesso
if __name__ == "__main__":

    # apaga o banco para não repetir os dados
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    # cria a tabela TipoProcesso
    db.create_all()

    # testa a classe TipoProcesso
    tipoProcesso1 = TipoProcesso(nome = "Limpeza de Barra", descricao = "Remoção de impurezas na barra utilizando óleo.")
    tipoProcesso2 = TipoProcesso(nome = "Seleção Manual de Chanfro", descricao = "Verificação manual do chanfro das peças.")
    tipoProcesso3 = TipoProcesso(nome = "Torneamento de Chanfro", descricao = "Criação de chanfro nas peças utilizando o torno.")        
    
    # persiste os tipos de processo
    db.session.add(tipoProcesso1)
    db.session.add(tipoProcesso2)
    db.session.add(tipoProcesso3)
    db.session.commit()
    
    # exibe os cargos
    print(tipoProcesso1)
    print(tipoProcesso2)
    print(tipoProcesso3)

    # exibe os cargos no formato JSON
    print(tipoProcesso1.json())
    print(tipoProcesso2.json())
    print(tipoProcesso3.json())