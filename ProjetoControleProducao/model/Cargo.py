import sys 
import os
sys.path.append(os.path.abspath("./config"))
from Config import *

class Cargo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))

    # toString da classe Cargo
    def __str__(self):
        return "Cargo: id:" + str(self.id) + " | Nome: "+ self.nome

    # retorna classe Cargo em formato JSON
    def json(self):
        return {
            "id": self.id,
            "nome": self.nome
        }

# método main da classe Cargo
if __name__ == "__main__":

    # apaga o banco para não repetir os dados
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    # cria a tabela Cargo
    db.create_all()

    # testa a classe Cargo
    cargo1 = Cargo(nome = "Operador de Máquina")
    cargo2 = Cargo(nome = "Auxiliar de Operador")
    cargo3 = Cargo(nome = "Supervisor de Produção")        
    
    # persiste os cargos
    db.session.add(cargo1)
    db.session.add(cargo2)
    db.session.add(cargo3)
    db.session.commit()
    
    # exibe os cargos
    print(cargo1)
    print(cargo2)
    print(cargo3)

    # exibe os cargos no formato JSON
    print(cargo1.json())
    print(cargo2.json())
    print(cargo3.json())