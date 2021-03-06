from Config import *

# *********************************** Modelo da classe Cargo ************************************
class Cargo(db.Model):
    # ******************************* Atributos da Classe Cargo *********************************
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    # *******************************************************************************************

    # ****************************** toString da classe Cargo ***********************************
    def __str__(self):
        retorno = f"Cargo(\n"
        retorno += f"   ID: {self.id},\n"
        retorno += f"   Nome: {self.nome}\n)"
        return retorno
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
        retorno = f"Funcionario(\n"
        retorno += f"   ID: {self.id},\n"
        retorno += f"   Nome: {self.nome},\n"
        retorno += f"   Cargo: {self.cargo.nome}\n)"
        return retorno
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
    descricao = db.Column(db.String(250), nullable=False)
    # *******************************************************************************************

    # *********************** toString da classe TipoProcesso ***********************************
    def __str__(self):
        retorno = f"Tipo de Processo(\n"
        retorno += f"   ID: {self.id},\n"
        retorno += f"   Nome: {self.nome},\n"
        retorno += f"   Descrição: {self.descricao}\n)"
        return retorno
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
class Material(db.Model):
    # **************************** Atributos da Classe Material *********************************
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.String(250), nullable=False)
    quantidadeEstoque = db.Column(db.Float, nullable=False)
    valorUnitario = db.Column(db.Float, nullable=False)
    type = db.Column(db.String(50))
    __mapper_args__ = { 
        'polymorphic_identity':'pessoa',
        'polymorphic_on':type
    }
    # *******************************************************************************************
    
    # ************** Método atualizarEstoque da Classe Material *********************************
    def atualizar_estoque(self, qtd, entrada):
        if entrada:
            self.quantidadeEstoque += qtd
        else:
            self.quantidadeEstoque -= qtd
    # *******************************************************************************************
    
    # *************************** toString da classe Material ***********************************
    def __str__(self):
        retorno = f"   ID: {self.id},\n"
        retorno += f"   Nome: {self.nome},\n"
        retorno += f"   Descrição: {self.descricao},\n"
        retorno += f"   Estoque: {self.quantidadeEstoque},\n"
        retorno += f"   Valor Unitário: {self.valorUnitario},"
        return retorno
    # *******************************************************************************************

    # ************************** retorna classe Material em formato JSON ************************
    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "descricao": self.descricao,
            "quantidadeEstoque": self.quantidadeEstoque,
            "valorUnitario": self.valorUnitario
        }
    # *******************************************************************************************
# ***********************************************************************************************

# ************************* Modelo da classe MateriaPrima ***************************************
class MateriaPrima(Material):
    # ************************ Atributos da Classe MateriaPrima *********************************
    id = db.Column(db.Integer, db.ForeignKey(Material.id), primary_key=True)
    __mapper_args__ = { 
        'polymorphic_identity':'materia_prima' 
    }
    fornecedor = db.Column(db.String(50), nullable=False)
    # *******************************************************************************************

    # *********************** toString da classe MateriaPrima ***********************************
    def __str__(self):
        retorno = f"Matéria-Prima(\n"
        retorno += super().__str__() + f"\n"
        retorno += f"   Fornecedor: {self.fornecedor}\n)"
        return retorno
    # *******************************************************************************************

    # ********************** retorna classe MateriaPrima em formato JSON ************************
    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "descricao": self.descricao,
            "quantidadeEstoque": self.quantidadeEstoque,
            "valorUnitario": self.valorUnitario,
            "fornecedor": self.fornecedor
        }
    # *******************************************************************************************
# ***********************************************************************************************

# ************************* Modelo da classe Produto ********************************************
class Produto(Material):
    # ************************ Atributos da Classe Produto **************************************
    id = db.Column(db.Integer, db.ForeignKey(Material.id), primary_key=True)
    __mapper_args__ = { 
        'polymorphic_identity':'produto'
    }
    valorVenda = db.Column(db.Float, nullable=False)
    # *******************************************************************************************

    # ********************* Lista de processos de cada Producao *********************************
    producoes = db.relationship("Producao", primaryjoin="Produto.id==Producao.produto_id")
    # *******************************************************************************************

    # ****************** Método calcularValorProducao da classe Produto *************************
    def calcular_valor_producao(self):
        custos = 0
        count = 0
        for p in self.producoes:
            if p.finalizada:
                custos += p.calcular_custo_total() / p.quantidadeProduzida
                count += 1
        if count > 0:
            self.valorUnitario = custos / count
    # *******************************************************************************************

    # ****************** Método calculaValorProducao da classe Produto **************************
    def calcular_valor_venda(self, valorAdicional):
        self.valorVenda = self.valorUnitario + valorAdicional
    # *******************************************************************************************

    # *********************** toString da classe Produto ****************************************
    def __str__(self):
        retorno = f"Produto(\n"
        retorno += super().__str__() + f"\n"
        retorno += f"   Valor Venda: {self.valorVenda}\n)"
        return retorno
    # *******************************************************************************************

    # ********************** retorna classe Produto em formato JSON *****************************
    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "descricao": self.descricao,
            "quantidadeEstoque": self.quantidadeEstoque,
            "valorUnitario": self.valorUnitario,
            "valorVenda": self.valorVenda
        }
    # *******************************************************************************************
# ***********************************************************************************************

# ************************* Modelo da classe Producao *******************************************
class Producao(db.Model):
    # ************************ Atributos da Classe Producao *************************************
    id = db.Column(db.Integer, primary_key=True)
    produto_id = db.Column(db.Integer, db.ForeignKey(Produto.id), nullable=False)
    produto = db.relationship("Produto")
    quantidadeProduzida = db.Column(db.Float, nullable=False)
    finalizada = db.Column(db.Boolean, nullable=False)
    # *******************************************************************************************

    # ********************* Lista de processos de cada Producao *********************************
    processos = db.relationship("Processo", primaryjoin="Producao.id==Processo.producao_id")
    # *******************************************************************************************

    # **************** Método finalizarProducao da Classe Producao ******************************
    def finalizar_producao(self):
        self.produto.quantidadeEstoque += self.quantidadeProduzida
        self.finalizada = True
    # *******************************************************************************************    

    # **************** Método calcularTempoTotal da Classe Producao *****************************
    def calcular_tempo_total(self):
        tempoTotal = datetime.utcnow() - datetime.utcnow()
        for p in self.processos:
            if p.calcular_tempo_total() == None:
                return None
            else:
                tempoTotal += p.calcular_tempo_total()
        return tempoTotal
    # *******************************************************************************************

    # **************** Método calcularCustoTotal() da Classe Producao ***************************
    def calcular_custo_total(self):
        custoTotal = 0
        for p in self.processos:
            if p.calcular_custo_total() == None:
                return None
            else:
                custoTotal += p.calcular_custo_total()
        return custoTotal
    # *******************************************************************************************

    # *********************** toString da classe Producao ***************************************
    def __str__(self):
        retorno = f"Produção(\n"
        retorno += f"   ID: {self.id},\n"
        retorno += f"   Produto: {self.produto.nome},\n"
        retorno += f"   Quantidade Produzida: {self.quantidadeProduzida},\n"
        if self.finalizada:
            retorno += f"   Finalizada(\n"
            retorno += f"      Tempo Total: {self.calcular_tempo_total()},\n"
            retorno += f"      Custo Total: {self.calcular_custo_total()}\n   )\n)"
            return retorno
        return retorno + f"   Em produção\n)"
    # *******************************************************************************************

    # ********************** retorna classe Producao em formato JSON ****************************
    def json(self):
        return {
            "id": self.id,
            "produto": self.produto.json(),
            "quantidadeProduzida": self.quantidadeProduzida,
            "finalizada": self.finalizada,
            "tempoTotal": str(self.calcular_tempo_total()),
            "custoTotal": self.calcular_custo_total()
        }
    # *******************************************************************************************
# ***********************************************************************************************

# ************************* Modelo da classe Processo *******************************************
class Processo(db.Model):
    # ************************ Atributos da Classe Processo *************************************
    id = db.Column(db.Integer, primary_key=True)
    tipo_id = db.Column(db.Integer, db.ForeignKey(TipoProcesso.id), nullable=False)
    tipo = db.relationship("TipoProcesso")
    producao_id = db.Column(db.Integer, db.ForeignKey(Producao.id), nullable=False)
    producao = db.relationship("Producao")
    supervisor_id = db.Column(db.Integer, db.ForeignKey(Funcionario.id), nullable=False)
    supervisor = db.relationship("Funcionario")
    horaInicial = db.Column(db.DateTime, nullable=False)
    horaFinal = db.Column(db.DateTime)
    aprovado = db.Column(db.Boolean, nullable=False)
    # *******************************************************************************************

    # ****************** Lista de Materiais utilizados em cada Processo *************************
    materiais = db.relationship("MaterialUsado", primaryjoin="Processo.id==MaterialUsado.processo_id")
    # *******************************************************************************************

    # **************** Método finalizarProcesso da Classe Processo *****************************
    def finalizar_processo(self, aprovado):
        self.horaFinal = datetime.utcnow()
        self.aprovado = aprovado
        for m in self.materiais:
            m.material.atualizar_estoque(m.quantidadeUsada, False)
    # *******************************************************************************************

    # **************** Método calcularTempoTotal da Classe Processo *****************************
    def calcular_tempo_total(self):
        if self.horaFinal == None:
            return None
        else:
            return self.horaFinal - self.horaInicial
    # *******************************************************************************************

    # **************** Método calcularCustoTotal() da Classe Processo ***************************
    def calcular_custo_total(self):
        custoTotal = 0
        for m in self.materiais:
            custo = m.material.valorUnitario * m.quantidadeUsada
            custoTotal += custo
        return custoTotal
    # *******************************************************************************************

    # *********************** toString da classe Processo ***************************************
    def __str__(self):
        retorno = f"Processo(\n"
        retorno += f"   ID: {self.id},\n"
        retorno += f"   Tipo Processo: {self.tipo.nome},\n"
        retorno += f"   Produção(\n"
        retorno += f"      ID: {self.producao_id},\n"
        retorno += f"      Produto: {self.producao.produto.nome}\n   ),\n"
        retorno += f"   Supervisor: {self.supervisor.nome},\n"
        retorno += f"   Hora Inicial: {self.horaInicial},\n"
        if self.horaFinal != None:
            retorno += f"   Hora Final: {self.horaFinal},\n"
            retorno += f"   Tempo Total: {self.calcular_tempo_total()},\n"
            retorno += f"   Custo Total: {self.calcular_custo_total()},\n"
            if self.aprovado:
                return retorno + f"   Processo Aprovado\n)"
            return retorno + f"   Processo Reprovado\n)"
        return retorno + f"   Em andamento\n)"
    # *******************************************************************************************

    # ********************** retorna classe Processo em formato JSON ****************************
    def json(self):
        return {
            "id": self.id,
            "tipo": self.tipo.json(),
            "producao": self.producao.json(),
            "supervisor": self.supervisor.json(),
            "horaInicial": str(self.horaInicial),
            "horaFinal": str(self.horaFinal),
            "aprovado": self.aprovado,
            "tempoTotal": str(self.calcular_tempo_total()),
            "custoTotal": self.calcular_custo_total()
        }
    # *******************************************************************************************
# ***********************************************************************************************

# ************************* Modelo da classe MaterialUsado **************************************
class MaterialUsado(db.Model):
    # ************************ Atributos da Classe MaterialUsado ********************************
    id = db.Column(db.Integer, primary_key=True)
    processo_id = db.Column(db.Integer, db.ForeignKey(Processo.id, ondelete="CASCADE"), nullable=False)
    processo = db.relationship("Processo")
    material_id = db.Column(db.Integer, db.ForeignKey(Material.id), nullable=False)
    material = db.relationship("Material")
    quantidadeUsada = db.Column(db.Float, nullable=False)
    # *******************************************************************************************

    # *********************** toString da classe MaterialUsado **********************************
    def __str__(self):
        retorno = f"Material Usado(\n"
        retorno += f"   ID: {self.id},\n"
        retorno += f"   Processo(\n"
        retorno += f"      ID: {self.processo.id},\n"
        retorno += f"      Tipo Processo: {self.processo.tipo.nome}\n   ),\n"
        retorno += f"   Material(\n"
        retorno += f"      ID: {self.material.id},\n"
        retorno += f"      Nome: {self.material.nome}\n   ),\n"
        retorno += f"   Quantidade Usada: {self.quantidadeUsada}\n)"
        return retorno
    # *******************************************************************************************

    # ********************** retorna classe MaterialUsado em formato JSON ***********************
    def json(self):
        return {
            "id": self.id,
            "processo": self.processo.json(),
            "material": self.material.json(),
            "quantidadeUsada": self.quantidadeUsada
        }
    # *******************************************************************************************
# ***********************************************************************************************

# ********************* Modelo da classe FuncionarioNoProcesso **********************************
class FuncionarioNoProcesso(db.Model):
    # ***************** Atributos da Classe FuncionarioNoProcesso *******************************
    id = db.Column(db.Integer, primary_key=True)
    processo_id = db.Column(db.Integer, db.ForeignKey(Processo.id, ondelete="CASCADE"), nullable=False)
    processo = db.relationship("Processo")
    funcionario_id = db.Column(db.Integer, db.ForeignKey(Funcionario.id), nullable=False)
    funcionario = db.relationship("Funcionario")
    # *******************************************************************************************
    
    # ***************** toString da classe FuncionarioNoProcesso ********************************
    def __str__(self):
        retorno = f"Funcionario no Processo(\n"
        retorno += f"   ID: {self.id},\n"
        retorno += f"   Processo(\n"
        retorno += f"      ID: {self.processo.id},\n"
        retorno += f"      Tipo Processo: {self.processo.tipo.nome}\n   ),\n"
        retorno += f"   Funcionário(\n"
        retorno += f"      ID: {self.funcionario.id},\n"
        retorno += f"      Nome: {self.funcionario.nome}\n   )\n)"
        return retorno
    # *******************************************************************************************

    # *************** retorna classe FuncionarioNoProcesso em formato JSON **********************
    def json(self):
        return {
            "id": self.id,
            "processo": self.processo.json(),
            "funcionario": self.funcionario.json()
        }
    # *******************************************************************************************
# ***********************************************************************************************

# ****************************** Teste das Classes **********************************************
if __name__ == "__main__":

    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    db.create_all()

    cargos = []
    tipos = []
    funcionarios = []
    materias = []
    produtos = []
    producoes = []
    processos = []
    materiaisUsados = []
    funcionariosProcessos = []

    cargos.append(Cargo(nome = "Operador de Máquina"))
    cargos.append(Cargo(nome = "Auxiliar de Operador"))
    cargos.append(Cargo(nome = "Supervisor de Produção"))
    for c in cargos:
        db.session.add(c)

    tipos.append(TipoProcesso(nome = "Seleção Manual de Chanfro", descricao = "Verificação manual do chanfro das peças."))
    tipos.append(TipoProcesso(nome = "Limpeza de Barra", descricao = "Remoção de impurezas na barra utilizando óleo."))
    tipos.append(TipoProcesso(nome = "Torneamento de Chanfro", descricao = "Criação de chanfro nas peças utilizando o torno."))
    for t in tipos:
        db.session.add(t)

    funcionarios.append(Funcionario(nome = "Thiago", cargo = cargos[0]))
    funcionarios.append(Funcionario(nome = "Alexandre", cargo = cargos[1]))
    funcionarios.append(Funcionario(nome = "Hylson", cargo = cargos[2]))
    for f in funcionarios:
        db.session.add(f)

    materias.append(MateriaPrima(nome="Barra de Alumínio", descricao = "", quantidadeEstoque = 0, valorUnitario = 100, fornecedor = "Fornecedor1"))
    materias.append(MateriaPrima(nome="Óleo", descricao = "", quantidadeEstoque = 0, valorUnitario = 10, fornecedor = "Fornecedor2"))
    materias.append(MateriaPrima(nome="Vaselina", descricao = "", quantidadeEstoque = 0, valorUnitario = 5, fornecedor = "Fornecedor3"))
    materias[0].atualizar_estoque(10, True)
    materias[1].atualizar_estoque(1000, True)
    materias[2].atualizar_estoque(1, True)
    for m in materias:
        db.session.add(m)
    
    produtos.append(Produto(nome = "Peça 1", descricao = "Teste Peça 1", quantidadeEstoque = 0, valorUnitario = 0, valorVenda = 0))
    produtos.append(Produto(nome = "Peça 2", descricao = "Teste Peça 2", quantidadeEstoque = 0, valorUnitario = 0, valorVenda = 0))
    for p in produtos:
        db.session.add(p)

    producoes.append(Producao(produto = produtos[0], quantidadeProduzida = 1000, finalizada = False))
    producoes.append(Producao(produto = produtos[1], quantidadeProduzida = 2000, finalizada = False))
    for p in producoes:
        db.session.add(p)

    processos.append(Processo(tipo = tipos[2], producao = producoes[0], supervisor = funcionarios[0], horaInicial = datetime.utcnow(), horaFinal = None, aprovado = False))
    processos.append(Processo(tipo = tipos[1], producao = producoes[0], supervisor = funcionarios[0], horaInicial = datetime.utcnow(), horaFinal = None, aprovado = False))
    processos.append(Processo(tipo = tipos[1], producao = producoes[0], supervisor = funcionarios[1], horaInicial = datetime.utcnow(), horaFinal = None, aprovado = False))
    processos.append(Processo(tipo = tipos[2], producao = producoes[1], supervisor = funcionarios[2], horaInicial = datetime.utcnow(), horaFinal = None, aprovado = False))
    processos.append(Processo(tipo = tipos[1], producao = producoes[1], supervisor = funcionarios[2], horaInicial = datetime.utcnow(), horaFinal = None, aprovado = False))
    processos.append(Processo(tipo = tipos[0], producao = producoes[1], supervisor = funcionarios[1], horaInicial = datetime.utcnow(), horaFinal = None, aprovado = False))
    for p in processos:
        db.session.add(p)
    
    materiaisUsados.append(MaterialUsado(processo = processos[0], material = materias[0], quantidadeUsada = 2))
    materiaisUsados.append(MaterialUsado(processo = processos[1], material = materias[1], quantidadeUsada = 50))
    materiaisUsados.append(MaterialUsado(processo = processos[3], material = materias[0], quantidadeUsada = 4))
    materiaisUsados.append(MaterialUsado(processo = processos[4], material = materias[1], quantidadeUsada = 100))
    for m in materiaisUsados:
        db.session.add(m)

    funcionariosProcessos.append(FuncionarioNoProcesso(processo = processos[0], funcionario = funcionarios[0]))
    funcionariosProcessos.append(FuncionarioNoProcesso(processo = processos[1], funcionario = funcionarios[0]))
    funcionariosProcessos.append(FuncionarioNoProcesso(processo = processos[2], funcionario = funcionarios[0]))
    funcionariosProcessos.append(FuncionarioNoProcesso(processo = processos[2], funcionario = funcionarios[1]))
    funcionariosProcessos.append(FuncionarioNoProcesso(processo = processos[3], funcionario = funcionarios[2]))
    funcionariosProcessos.append(FuncionarioNoProcesso(processo = processos[4], funcionario = funcionarios[1]))
    funcionariosProcessos.append(FuncionarioNoProcesso(processo = processos[5], funcionario = funcionarios[0]))
    for f in funcionariosProcessos:
        db.session.add(f)

    db.session.commit()

    processos[0].finalizar_processo(True)
    processos[1].finalizar_processo(True)
    processos[3].finalizar_processo(True)
    processos[4].finalizar_processo(True)
    processos[5].finalizar_processo(False)
    processos.append(Processo(tipo = tipos[0], producao = producoes[1], supervisor = funcionarios[1], horaInicial = datetime.utcnow(), horaFinal = None, aprovado = False))
    for p in processos:
        db.session.add(p)

    materiaisUsados.append(MaterialUsado(processo = processos[6], material = materias[2], quantidadeUsada = 1))
    for m in materiaisUsados:
        db.session.add(m)

    funcionariosProcessos.append(FuncionarioNoProcesso(processo = processos[6], funcionario = funcionarios[0]))
    funcionariosProcessos.append(FuncionarioNoProcesso(processo = processos[6], funcionario = funcionarios[1]))
    for f in funcionariosProcessos:
        db.session.add(f)

    db.session.commit()
    
    processos[6].finalizar_processo(True)
    for p in processos:
        db.session.add(p)

    producoes[1].finalizar_producao()
    for p in producoes:
        db.session.add(p)

    db.session.commit()

    produtos[0].calcular_valor_producao()
    produtos[0].calcular_valor_venda(10)
    produtos[1].calcular_valor_producao()
    produtos[1].calcular_valor_venda(10)
    for p in produtos:
        db.session.add(p)
    
    db.session.commit()
    
    # exibe os objetos das classes
    for c in cargos:
        print(c)
    for t in tipos:
        print(t)
    for f in funcionarios:
        print(f)
    for m in materias:
        print(m)
    for p in produtos:
        print(p)
    for p in producoes:
        print(p)
    for p in processos:
        print(p)
    for m in materiaisUsados:
        print(m)
    for f in funcionariosProcessos:
        print(f)

    # exibe os objetos das classes no formato JSON
    for c in cargos:
        print(c.json())
    for t in tipos:
        print(t.json())
    for f in funcionarios:
        print(f.json())
    for m in materias:
        print(m.json())
    for p in produtos:
        print(p.json())
    for p in producoes:
        print(p.json())
    for p in processos:
        print(p.json())
    for m in materiaisUsados:
        print(m.json())
    for f in funcionariosProcessos:
        print(f.json())
# ***********************************************************************************************