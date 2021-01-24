from Config import *

# *********************************** Modelo da classe Cargo ************************************
class Cargo(db.Model):
    # ******************************* Atributos da Classe Cargo *********************************
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    # *******************************************************************************************

    # ****************************** toString da classe Cargo ***********************************
    def __str__(self):
        return "Cargo: id:" + str(self.id) + " | Nome: "+ self.nome
    # *******************************************************************************************

    # ***************************** retorna classe Cargo em formato JSON ************************
    def json(self):
        return {
            "id": self.id,
            "nome": self.nome
        }
    # *******************************************************************************************
# ***********************************************************************************************

# ***************************** Modelo da classe Funcionario ************************************
class Funcionario(db.Model):
    # ************************* Atributos da Classe Funcionario *********************************
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    cargo_id = db.Column(db.Integer, db.ForeignKey(Cargo.id), nullable=False)
    cargo = db.relationship("Cargo")
    # *******************************************************************************************

    # ************************* toString da classe Funcionario **********************************
    def __str__(self):
        return "Funcionario: id:" + str(self.id) + " | Nome: " + self.nome + " | Cargo: " + self.cargo.nome
    # *******************************************************************************************

    # ************************* retorna classe Funcionario em formato JSON **********************
    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "cargo": self.cargo.json()
        }
    # *******************************************************************************************
# ***********************************************************************************************

# **************************** Modelo da classe TipoProcesso ************************************
class TipoProcesso(db.Model):
    # ************************ Atributos da Classe TipoProcesso *********************************
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50),nullable=False)
    descricao = db.Column(db.String(250), nullable=True)
    # *******************************************************************************************

    # *********************** toString da classe TipoProcesso ***********************************
    def __str__(self):
        return "Tipo de Processo: id:" + str(self.id) + " | Nome: "+ self.nome + " | Descrição: "+ self.descricao
    # *******************************************************************************************

    # *********************** retorna classe TipoProcesso em formato JSON ***********************
    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "descricao": self.descricao
        }
    # *******************************************************************************************
# ***********************************************************************************************

# ******************************** Modelo da classe Material ************************************
# É necessário transformar em classe abstrata ainda!
class Material(db.Model):
    # **************************** Atributos da Classe Material *********************************
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.String(250), nullable=True)
    quantidadeEstoque = db.Column(db.Numeric(10,2), default=0)
    # *******************************************************************************************

    # ************** Método atualizarEstoque da Classe Material *********************************
    # *******************************************************************************************

    # *************************** toString da classe Material ***********************************
    def __str__(self):
        return "Material: id:" + str(self.id) + " | Nome: "+ self.nome + " | Descrição: " + self.descricao + " | Estoque: " + self.quantidadeEstoque
    # *******************************************************************************************

    # ************************** retorna classe Material em formato JSON ************************
    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "descricao": self.descricao,
            "quantidadeEstoque": self.quantidadeEstoque
        }
    # *******************************************************************************************
# ***********************************************************************************************

# ************************* Modelo da classe MateriaPrima ***************************************

    # ************************ Atributos da Classe MateriaPrima *********************************
    # *******************************************************************************************

    # *********************** toString da classe MateriaPrima ***********************************
    # *******************************************************************************************

    # ********************** retorna classe MateriaPrima em formato JSON ************************
    # *******************************************************************************************
# ***********************************************************************************************

# ************************* Modelo da classe Produto ********************************************

    # ************************ Atributos da Classe Produto *************************************
    # *******************************************************************************************

    # ****************** Método calculaValorProducao da classe Produto **************************
    # *******************************************************************************************

    # *********************** toString da classe Produto ****************************************
    # *******************************************************************************************

    # ********************** retorna classe Produto em formato JSON *****************************
    # *******************************************************************************************
# ***********************************************************************************************

# ************************* Modelo da classe Producao ******************************************

    # ************************ Atributos da Classe Producao *************************************
    # *******************************************************************************************

    # **************** Método calcularTempoTotal da Classe Producao *****************************
    # *******************************************************************************************

    # **************** Método calcularCustoTotal() da Classe Producao ***************************
    # *******************************************************************************************

    # *********************** toString da classe Producao ***************************************
    # *******************************************************************************************

    # ********************** retorna classe Producao em formato JSON ****************************
    # *******************************************************************************************
# ***********************************************************************************************

# ************************* Modelo da classe Processo ******************************************

    # ************************ Atributos da Classe Processo *************************************
    # *******************************************************************************************

    # **************** Método calcularTempoTotal da Classe Processo *****************************
    # *******************************************************************************************

    # **************** Método calcularCustoTotal() da Classe Processo ***************************
    # *******************************************************************************************

    # *********************** toString da classe Processo ***************************************
    # *******************************************************************************************

    # ********************** retorna classe Processo em formato JSON ****************************
    # *******************************************************************************************
# ***********************************************************************************************

# ************************* Modelo da classe MaterialUsado **************************************

    # ************************ Atributos da Classe MaterialUsado ********************************
    # *******************************************************************************************

    # *********************** toString da classe MaterialUsado **********************************
    # *******************************************************************************************

    # ********************** retorna classe MaterialUsado em formato JSON ***********************
    # *******************************************************************************************
# ***********************************************************************************************

# ********************* Modelo da classe FuncionarioNoProcesso **********************************

    # ***************** Atributos da Classe FuncionarioNoProcesso *******************************
    # *******************************************************************************************

    # ***************** toString da classe FuncionarioNoProcesso ********************************
    # *******************************************************************************************

    # *************** retorna classe FuncionarioNoProcesso em formato JSON **********************
    # *******************************************************************************************
# ***********************************************************************************************

# ****************************** Teste das Classes **********************************************
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
    funcionario1 = Funcionario(nome="Thiago", cargo=cargo1)
    funcionario2 = Funcionario(nome="Alexandre", cargo=cargo2)
    funcionario3 = Funcionario(nome="Hylson", cargo=cargo3)
    
    # persiste os objetos das classes
    db.session.add(cargo1)
    db.session.add(cargo2)
    db.session.add(cargo3)
    db.session.add(tipoProcesso1)
    db.session.add(tipoProcesso2)
    db.session.add(tipoProcesso3)
    db.session.add(funcionario1)
    db.session.add(funcionario2)
    db.session.add(funcionario3)
    db.session.commit()
    
    # exibe os objetos das classes
    print(cargo1)
    print(cargo2)
    print(cargo3)
    print(tipoProcesso1)
    print(tipoProcesso2)
    print(tipoProcesso3)
    print(funcionario1)
    print(funcionario2)
    print(funcionario3)

    # exibe os objetos das classes no formato JSON
    print(cargo1.json())
    print(cargo2.json())
    print(cargo3.json())
    print(tipoProcesso1.json())
    print(tipoProcesso2.json())
    print(tipoProcesso3.json())
    print(funcionario1.json())
    print(funcionario2.json())
    print(funcionario3.json())
# ***********************************************************************************************