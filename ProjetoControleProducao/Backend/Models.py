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

if __name__ == "__main__":

    # apaga o banco para não repetir os dados
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    # cria as tabelas
    db.create_all()

    # testa as classes
    cargo1 = Cargo(nome = "Operador de Máquina")
    cargo2 = Cargo(nome = "Auxiliar de Operador")
    cargo3 = Cargo(nome = "Supervisor de Produção") 
    tipoProcesso1 = TipoProcesso(nome = "Limpeza de Barra", descricao = "Remoção de impurezas na barra utilizando óleo.")
    tipoProcesso2 = TipoProcesso(nome = "Seleção Manual de Chanfro", descricao = "Verificação manual do chanfro das peças.")
    tipoProcesso3 = TipoProcesso(nome = "Torneamento de Chanfro", descricao = "Criação de chanfro nas peças utilizando o torno.")        
    
    # persiste os objetos das classes
    db.session.add(cargo1)
    db.session.add(cargo2)
    db.session.add(cargo3)
    db.session.add(tipoProcesso1)
    db.session.add(tipoProcesso2)
    db.session.add(tipoProcesso3)
    db.session.commit()
    
    # exibe os objetos das classes
    print(cargo1)
    print(cargo2)
    print(cargo3)
    print(tipoProcesso1)
    print(tipoProcesso2)
    print(tipoProcesso3)

    # exibe os objetos das classes no formato JSON
    print(cargo1.json())
    print(cargo2.json())
    print(cargo3.json())
    print(tipoProcesso1.json())
    print(tipoProcesso2.json())
    print(tipoProcesso3.json())