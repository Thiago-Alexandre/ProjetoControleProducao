from Config import *
from Models import *
from Util import Validacao

# ************************************* Rota para listar todos os Cargos ******************************
@app.route("/cargos")
def listarCargos():
    try:
        cargos = db.session.query(Cargo).all()
    except:
        cargos = []
    cargos_em_json = [ c.json() for c in cargos ]
    resposta = jsonify(cargos_em_json)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta
# *****************************************************************************************************

# ************************************* Rota para listar todos os Tipos de Processo *******************
@app.route("/tipos")
def listarTipos():
    try:
        tipos = db.session.query(TipoProcesso).all()
    except:
        tipos = []
    tipos_em_json = [ t.json() for t in tipos ]
    resposta = jsonify(tipos_em_json)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta
# *****************************************************************************************************

# ************************************* Rota para listar todos os Funcionarios ************************
@app.route("/funcionarios")
def listarFuncionarios():
    try:
        funcionarios = db.session.query(Funcionario).all()
    except:
        funcionarios = []
    funcionarios_em_json = [ f.json() for f in funcionarios ]
    resposta = jsonify(funcionarios_em_json)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta
# *****************************************************************************************************

# ************************************* Rota para listar todas as Materias-Prima **********************
@app.route("/materias")
def listarMaterias():
    try:
        materias = db.session.query(MateriaPrima).all()
    except:
        materias = []
    materias_em_json = [ m.json() for m in materias ]
    resposta = jsonify(materias_em_json)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta
# *****************************************************************************************************

# ************************************* Rota para listar todos os Produtos ****************************
@app.route("/produtos")
def listarProdutos():
    try:
        produtos = db.session.query(Produto).all()
    except:
        produtos = []
    produtos_em_json = [ p.json() for p in produtos ]
    resposta = jsonify(produtos_em_json)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta
# *****************************************************************************************************

# ************************************* Rota para listar todos as Produções ***************************
@app.route("/producoes")
def listarProducoes():
    try:
        producoes = db.session.query(Producao).all()
    except:
        producoes = []
    producoes_em_json = [ p.json() for p in producoes ]
    resposta = jsonify(producoes_em_json)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta
# *****************************************************************************************************

# ***************************** Rota para listar todos os Processos de uma Producao *******************
@app.route("/producoes/<int:producao_id>/processos")
def listarProcessosProducao(producao_id):
    try:
        #producao = Producao.query.join(Producao, Producao.id == Processo.producao_id).filter(Processo.producao_id == producao_id).first()
        processos = db.session.query(Processo).filter(Processo.producao_id == producao_id).all()
    except:
        processos = []
    processos_em_json = [ p.json() for p in processos ]
    resposta = jsonify(processos_em_json)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta
# *****************************************************************************************************

# ***************************** Rota para listar todos os Materiais de um Processo ********************
@app.route("/processos/<int:processo_id>/materiais")
def listarMateriaisProcesso(processo_id):
    try:
        materiais = db.session.query(MaterialUsado).filter(MaterialUsado.processo_id == processo_id).all()
    except:
        materiais = []
    materiais_em_json = [ m.json() for m in materiais ]
    resposta = jsonify(materiais_em_json)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta
# *****************************************************************************************************

# ***************************** Rota para listar todos os Funcionarios de um Processo *****************
@app.route("/processos/<int:processo_id>/funcionarios")
def listarFuncionariosProcesso(processo_id):
    try:
        funcionarios = db.session.query(FuncionarioNoProcesso).filter(FuncionarioNoProcesso.processo_id == processo_id).all()
    except:
        funcionarios = []
    funcionarios_em_json = [ f.json() for f in funcionarios ]
    resposta = jsonify(funcionarios_em_json)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta
# *****************************************************************************************************

# ************************************* Rota para listar todos os Materiais **********************
@app.route("/materiais")
def listarMateriais():
    try:
        materiais = db.session.query(Material).all()
    except:
        materiais = []
    materiais_em_json = [ m.json() for m in materiais ]
    resposta = jsonify(materiais_em_json)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta
# *****************************************************************************************************

# ************************************* Rota para pesquisar um Cargo **********************************
@app.route("/cargos/<int:cargo_id>")
def pesquisarCargo(cargo_id):
    try:
        cargos = db.session.query(Cargo).filter(Cargo.id == cargo_id).all()
    except:
        cargos = []
    cargos_em_json = [ c.json() for c in cargos ]
    resposta = jsonify(cargos_em_json)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta
# *****************************************************************************************************

# ************************************* Rota para pesquisar um Tipo de Processo ***********************
@app.route("/tipos/<int:tipo_id>")
def pesquisarTipo(tipo_id):
    try:
        tipos = db.session.query(TipoProcesso).filter(TipoProcesso.id == tipo_id).all()
    except:
        tipos = []
    tipos_em_json = [ t.json() for t in tipos ]
    resposta = jsonify(tipos_em_json)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta
# *****************************************************************************************************

# ************************************* Rota para pesquisar um Funcionario ****************************
@app.route("/funcionarios/<int:funcionario_id>")
def pesquisarFuncionario(funcionario_id):
    try:
        funcionarios = db.session.query(Funcionario).filter(Funcionario.id == funcionario_id).all()
    except:
        funcionarios = []
    funcionarios_em_json = [ f.json() for f in funcionarios ]
    resposta = jsonify(funcionarios_em_json)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta
# *****************************************************************************************************

# ************************************* Rota para pesquisar uma Materia-Prima *************************
@app.route("/materias/<int:materia_id>")
def pesquisarMateria(materia_id):
    try:
        materias = db.session.query(MateriaPrima).filter(MateriaPrima.id == materia_id).all()
    except:
        materias = []
    materias_em_json = [ m.json() for m in materias ]
    resposta = jsonify(materias_em_json)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta
# *****************************************************************************************************

# ************************************* Rota para pesquisar um Produto ********************************
@app.route("/produtos/<int:produto_id>")
def pesquisarProduto(produto_id):
    try:
        produtos = db.session.query(Produto).filter(Produto.id == produto_id).all()
    except:
        produtos = []
    produtos_em_json = [ p.json() for p in produtos ]
    resposta = jsonify(produtos_em_json)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta
# *****************************************************************************************************

# ************************************* Rota para pesquisar uma Producao ******************************
@app.route("/producoes/<int:producao_id>")
def pesquisarProducao(producao_id):
    try:
        producoes = db.session.query(Producao).filter(Producao.id == producao_id).all()
    except:
        producoes = []
    producoes_em_json = [ p.json() for p in producoes ]
    resposta = jsonify(producoes_em_json)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta
# *****************************************************************************************************

# ************************************* Rota para pesquisar um Processo *******************************
@app.route("/processos/<int:processo_id>")
def pesquisarProcesso(processo_id):
    try:
        processos = db.session.query(Processo).filter(Processo.id == processo_id).all()
    except:
        processos = []
    processos_em_json = [ p.json() for p in processos ]
    resposta = jsonify(processos_em_json)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta
# *****************************************************************************************************

# ************************************* Rota para adicionar novo Cargo ********************************
@app.route("/cargos", methods=['POST']) 
def incluirCargo(): 
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"}) 
    dados = request.get_json()
    if Validacao.validarTexto(dados.get("nome"), 50):
        try:
            cargos = db.session.query(Cargo).filter(Cargo.nome == dados.get("nome")).all()
            if not cargos:
                novo = Cargo(nome = dados.get("nome"))
                db.session.add(novo)
                db.session.commit()
            else:
                resposta = jsonify({"resultado": "erro", "detalhes": "Já existe um cargo com esse nome!"})
        except Exception as e: 
            resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    else:
         resposta = jsonify({"resultado": "erro", "detalhes": "Informações inválidas!"})
    resposta.headers.add("Access-Control-Allow-Origin", "*") 
    return resposta
# *****************************************************************************************************

# ************************************* Rota para adicionar novo Tipo de Processo *********************
@app.route("/tipos", methods=['POST']) 
def incluirTipo():
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    dados = request.get_json()
    if not Validacao.validarTexto(dados.get("nome"), 50):
        resposta = jsonify({"resultado": "erro", "detalhes": "Informações inválidas!"})
    elif not Validacao.validarTexto(dados.get("descricao"), 250):
        resposta = jsonify({"resultado": "erro", "detalhes": "Informações inválidas!"})
    else:
        try:
            tipos = db.session.query(TipoProcesso).filter(TipoProcesso.nome == dados.get("nome")).all()
            if not tipos:
                novo = TipoProcesso(nome = dados.get("nome"), descricao = dados.get("descricao"))
                db.session.add(novo)
                db.session.commit()
            else:
                resposta = jsonify({"resultado": "erro", "detalhes": "Já existe um tipo de processo com esse nome!"})
        except Exception as e: 
            resposta = jsonify({"resultado":"erro", "detalhes":str(e)}) 
    resposta.headers.add("Access-Control-Allow-Origin", "*") 
    return resposta
# *****************************************************************************************************

# ************************************* Rota para adicionar novo Funcionario **************************
@app.route("/funcionarios", methods=['POST']) 
def incluirFuncionario(): 
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"}) 
    dados = request.get_json()
    if Validacao.validarTexto(dados.get("nome"), 50):
        try:
            cargoFuncionario = db.session.query(Cargo).filter(Cargo.id == dados.get("cargo_id")).first()
            if cargoFuncionario != None:
                novo = Funcionario(nome = dados.get("nome"), cargo = cargoFuncionario)
                db.session.add(novo)
                db.session.commit()
            else:
                resposta = jsonify({"resultado": "erro", "detalhes": "Nenhum cargo encontrado!"})
        except Exception as e: 
            resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    else:
        resposta = jsonify({"resultado": "erro", "detalhes": "Informações inválidas!"})
    resposta.headers.add("Access-Control-Allow-Origin", "*") 
    return resposta
# *****************************************************************************************************

# ************************************* Rota para adicionar nova Materia-Prima ************************
@app.route("/materias", methods=['POST']) 
def incluirMateria(): 
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"}) 
    dados = request.get_json()
    if not Validacao.validarTexto(dados.get("nome"), 50):
        resposta = jsonify({"resultado": "erro", "detalhes": "Informações inválidas!"})
    elif not Validacao.validarTexto(dados.get("descricao"), 250):
        resposta = jsonify({"resultado": "erro", "detalhes": "Informações inválidas!"})
    elif not Validacao.validarValor(dados.get("valorUnitario")):
        resposta = jsonify({"resultado": "erro", "detalhes": "Informações inválidas!"})
    elif not Validacao.validarTexto(dados.get("fornecedor"), 50):
        resposta = jsonify({"resultado": "erro", "detalhes": "Informações inválidas!"})
    else:
        try:
            materias = db.session.query(MateriaPrima).filter(MateriaPrima.nome == dados.get("nome")).all()
            if not materias:
                nova = MateriaPrima(nome = dados.get("nome"),
                                    descricao = dados.get("descricao"),
                                    quantidadeEstoque = 0,
                                    valorUnitario = float(dados.get("valorUnitario")),
                                    fornecedor = dados.get("fornecedor"))
                db.session.add(nova)
                db.session.commit()
            else:
                resposta = jsonify({"resultado": "erro", "detalhes": "Já existe uma matéria-prima com esse nome!"})
        except Exception as e: 
            resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    resposta.headers.add("Access-Control-Allow-Origin", "*") 
    return resposta
# *****************************************************************************************************

# ************************************* Rota para adicionar novo Produto ******************************
@app.route("/produtos", methods=['POST']) 
def incluirProduto(): 
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"}) 
    dados = request.get_json()
    if not Validacao.validarTexto(dados.get("nome"), 50):
        resposta = jsonify({"resultado": "erro", "detalhes": "Informações inválidas!"})
    elif not Validacao.validarTexto(dados.get("descricao"), 250):
        resposta = jsonify({"resultado": "erro", "detalhes": "Informações inválidas!"})
    else:
        try:
            produtos = db.session.query(Produto).filter(Produto.nome == dados.get("nome")).all()
            if not produtos:
                novo = Produto(nome = dados.get("nome"),
                                descricao = dados.get("descricao"),
                                quantidadeEstoque = 0,
                                valorUnitario = 0,
                                valorVenda = 0)
                db.session.add(novo)
                db.session.commit()
            else:
                resposta = jsonify({"resultado": "erro", "detalhes": "Já existe um produto com esse nome!"})
        except Exception as e: 
            resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    resposta.headers.add("Access-Control-Allow-Origin", "*") 
    return resposta
# *****************************************************************************************************

# ************************************* Rota para adicionar nova Producao *****************************
@app.route("/producoes", methods=['POST']) 
def incluirProducao(): 
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"}) 
    dados = request.get_json()
    if not Validacao.validarValor(dados.get("quantidadeProduzida")):
        resposta = jsonify({"resultado": "erro", "detalhes": "Informações inválidas!"})
    else:
        try:
            produtoProducao = db.session.query(Produto).filter(Produto.id == dados.get("produto_id")).first()
            if produtoProducao != None:
                nova = Producao(produto = produtoProducao,
                                quantidadeProduzida = dados.get("quantidadeProduzida"),
                                finalizada = False)
                db.session.add(nova)
                db.session.commit()
            else:
                resposta = jsonify({"resultado": "erro", "detalhes": "Nenhum produto encontrado!"})
        except Exception as e: 
            resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    resposta.headers.add("Access-Control-Allow-Origin", "*") 
    return resposta
# *****************************************************************************************************

# ************************************* Rota para adicionar novo Processo *****************************
@app.route("/processos", methods=['POST']) 
def incluirProcesso(): 
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"}) 
    dados = request.get_json()
    try:
        tipoProcesso = db.session.query(TipoProcesso).filter(TipoProcesso.id == dados.get("tipo_id")).first()
        producaoProcesso = db.session.query(Producao).filter(Producao.id == dados.get("producao_id")).first()
        supervisorProcesso = db.session.query(Funcionario).filter(Funcionario.id == dados.get("supervisor_id")).first()
        if tipoProcesso == None:
            resposta = jsonify({"resultado": "erro", "detalhes": "Nenhum tipo de processo encontrado!"})
        elif producaoProcesso == None:
            resposta = jsonify({"resultado": "erro", "detalhes": "Nenhuma produção encontrada!"})
        elif supervisorProcesso == None:
            resposta = jsonify({"resultado": "erro", "detalhes": "Nenhum funcionário encontrado!"})
        else:
            novo = Processo(tipo = tipoProcesso,
                            producao = producaoProcesso,
                            supervisor = supervisorProcesso,
                            horaInicial = datetime.utcnow(),
                            horaFinal = None,
                            aprovado = False)
            db.session.add(novo)
            db.session.commit()
    except Exception as e: 
        resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    resposta.headers.add("Access-Control-Allow-Origin", "*") 
    return resposta
# *****************************************************************************************************

# ************************************* Rota para adicionar novo Material Usado ***********************
@app.route("/materiais_processo", methods=['POST']) 
def incluirMaterialProcesso(): 
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"}) 
    dados = request.get_json()
    try:
        processoReferente = db.session.query(Processo).filter(Processo.id == dados.get("processo_id")).first()
        materialUsado = db.session.query(Material).filter(Material.id == dados.get("material_id")).first()
        if processoReferente == None:
            resposta = jsonify({"resultado": "erro", "detalhes": "Nenhum processo encontrado!"})
        elif materialUsado == None:
            resposta = jsonify({"resultado": "erro", "detalhes": "Nenhum material encontrado!"})
        elif not Validacao.validarValor(dados.get("quantidadeUsada")):
            resposta = jsonify({"resultado": "erro", "detalhes": "Informações inválidas!"})
        else:
            novo = MaterialUsado(processo = processoReferente,
                                 material = materialUsado,
                                 quantidadeUsada = float(dados.get("quantidadeUsada")))
            db.session.add(novo)
            db.session.commit()
            materialUsado.atualizar_estoque(float(dados.get("quantidadeUsada")), False)
            db.session.add(materialUsado)
            db.session.commit()
    except Exception as e: 
        resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    resposta.headers.add("Access-Control-Allow-Origin", "*") 
    return resposta
# *****************************************************************************************************

# ************************************* Rota para adicionar novo Funcionario no Processo **************
@app.route("/funcionarios_processo", methods=['POST']) 
def incluirFuncionarioProcesso(): 
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"}) 
    dados = request.get_json()
    try:
        processoReferente = db.session.query(Processo).filter(Processo.id == dados.get("processo_id")).first()
        funcionarioReferente = db.session.query(Funcionario).filter(Funcionario.id == dados.get("funcionario_id")).first()
        if processoReferente == None:
            resposta = jsonify({"resultado": "erro", "detalhes": "Nenhum processo encontrado!"})
        elif funcionarioReferente == None:
            resposta = jsonify({"resultado": "erro", "detalhes": "Nenhum funcionário encontrado!"})
        else:
            funcionariosProcesso = FuncionarioNoProcesso.query.join(Processo, Processo.id == FuncionarioNoProcesso.processo_id
                                                                    ).filter(FuncionarioNoProcesso.processo_id == processoReferente.id)
            funcionarioProcesso = funcionariosProcesso.join(Funcionario, Funcionario.id == FuncionarioNoProcesso.funcionario_id
                                                                    ).filter(FuncionarioNoProcesso.funcionario_id == funcionarioReferente.id).first()
            if funcionarioProcesso == None:
                novo = FuncionarioNoProcesso(processo = processoReferente,
                                            funcionario = funcionarioReferente)
                db.session.add(novo)
                db.session.commit()
            else:
                resposta = jsonify({"resultado": "erro", "detalhes": "Funcionário já está no processo!"})
    except Exception as e: 
        resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    resposta.headers.add("Access-Control-Allow-Origin", "*") 
    return resposta
# *****************************************************************************************************

# ************************************* Rota para excluir um Cargo ************************************
@app.route("/cargos/<int:cargo_id>", methods=["DELETE"])
def excluirCargo(cargo_id):
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    try:
        cargo = Cargo.query.filter(Cargo.id == cargo_id)
        funcionarios = Funcionario.query.join(Cargo, Cargo.id == Funcionario.cargo_id).filter(Funcionario.cargo_id == cargo_id).all()
        if not funcionarios:
            cargo.delete()
            db.session.commit()
        else:
            resposta = jsonify({"resultado":"erro", "detalhes":"Cargo em uso!"})
    except Exception as e:
        resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta
# *****************************************************************************************************

# ************************************* Rota para excluir um Tipo de Processo *************************
@app.route("/tipos/<int:tipo_id>", methods=["DELETE"])
def excluirTipo(tipo_id):
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    try:
        tipo = TipoProcesso.query.filter(TipoProcesso.id == tipo_id)
        processos = Processo.query.join(TipoProcesso, TipoProcesso.id == Processo.tipo_id).filter(Processo.tipo_id == tipo_id).all()
        if not processos:
            tipo.delete()
            db.session.commit()
        else:
            resposta = jsonify({"resultado":"erro", "detalhes":"Tipo de Processo em uso!"})
    except Exception as e:
        resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta
# *****************************************************************************************************

# ************************************* Rota para excluir um Funcionario ******************************
@app.route("/funcionarios/<int:funcionario_id>", methods=["DELETE"])
def excluirFuncionario(funcionario_id):
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    try:
        funcionario = Funcionario.query.filter(Funcionario.id == funcionario_id)
        processosSupervisor = Processo.query.join(Funcionario, Funcionario.id == Processo.supervisor_id)
        processosSupervisor = processosSupervisor.filter(Processo.supervisor_id == funcionario_id).all()
        processosFuncionario = FuncionarioNoProcesso.query.join(Funcionario, Funcionario.id == FuncionarioNoProcesso.funcionario_id)
        processosFuncionario = processosFuncionario.filter(FuncionarioNoProcesso.funcionario_id == funcionario_id).all()
        if not processosSupervisor and not processosFuncionario:
            funcionario.delete()
            db.session.commit()
        else:
            resposta = jsonify({"resultado":"erro", "detalhes":"Funcionário em uso!"})
    except Exception as e:
        resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta
# *****************************************************************************************************

# ************************************* Rota para excluir uma MateriaPrima ****************************
@app.route("/materias/<int:materia_id>", methods=["DELETE"])
def excluirMateria(materia_id):
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    try:
        materia = MateriaPrima.query.filter(MateriaPrima.id == materia_id)
        processosMateria = MaterialUsado.query.join(MateriaPrima, MateriaPrima.id == MaterialUsado.material_id)
        processosMateria = processosMateria.filter(MaterialUsado.material_id == materia_id).all()
        if not processosMateria:
            materia.delete()
            db.session.commit()
        else:
            resposta = jsonify({"resultado":"erro", "detalhes":"Matéria-Prima em uso!"})
    except Exception as e:
        resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta
# *****************************************************************************************************

# ************************************* Rota para excluir um Produto ******************************
@app.route("/produtos/<int:produto_id>", methods=["DELETE"])
def excluirProduto(produto_id):
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    try:
        produto = Produto.query.filter(Produto.id == produto_id)
        producoesProduto = Producao.query.join(Produto, Produto.id == Producao.produto_id)
        producoesProduto = producoesProduto.filter(Producao.produto_id == produto_id).all()
        processosMateria = MaterialUsado.query.join(Produto, Produto.id == MaterialUsado.material_id)
        processosMateria = processosMateria.filter(MaterialUsado.material_id == produto_id).all()
        if not producoesProduto and not processosMateria:
            produto.delete()
            db.session.commit()
        else:
            resposta = jsonify({"resultado":"erro", "detalhes":"Produto em uso!"})
    except Exception as e:
        resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta
# *****************************************************************************************************

# ************************************* Rota para excluir uma Produção ********************************
@app.route("/producoes/<int:producao_id>", methods=["DELETE"])
def excluirProducao(producao_id):
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    try:
        producao = Producao.query.filter(Producao.id == producao_id)
        producoesProcesso = Processo.query.join(Producao, Producao.id == Processo.producao_id)
        producoesProcesso = producoesProcesso.filter(Processo.producao_id == producao_id).all()
        if not producoesProcesso and not producao.first().finalizada:
            producao.delete()
            db.session.commit()
        else:
            resposta = jsonify({"resultado":"erro", "detalhes":"Produção em andamento ou já finalizada!"})
    except Exception as e:
        resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta
# *****************************************************************************************************

# ************************************* Rota para excluir um Processo *********************************
@app.route("/processos/<int:processo_id>", methods=["DELETE"])
def excluirProcesso(processo_id):
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    try:
        processo = Processo.query.filter(Processo.id == processo_id)
        materiaisProcesso = MaterialUsado.query.join(Processo, Processo.id == MaterialUsado.processo_id)
        materiaisProcesso = materiaisProcesso.filter(MaterialUsado.processo_id == processo_id).all()
        if not materiaisProcesso:
            processo.delete()
            db.session.commit()
        else:
            resposta = jsonify({"resultado":"erro", "detalhes":"Não é possível excluir este processo por ele já ter alterado o estoque!"})
    except Exception as e:
        resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta
# *****************************************************************************************************

# ************************************* Rota para excluir um Material do Processo *********************
@app.route("/materiais_processo/<int:material_usado_id>", methods=["DELETE"])
def excluirMaterialProcesso(material_usado_id):
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    try:
        materialUsado = MaterialUsado.query.filter(MaterialUsado.id == material_usado_id)
        materialUsado.delete()
        db.session.commit()
        materialUsado.material.atualizarEstoque(materialUsado.quantidadeUsada, True)
        db.session.add(materialUsado.material)
        db.session.commit()
    except Exception as e:
        resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta
# *****************************************************************************************************

# ************************************* Rota para excluir um Funcionario do Processo ******************
@app.route("/funcionarios_processo/<int:funcionario_processo_id>", methods=["DELETE"])
def excluirFuncionarioProcesso(funcionario_processo_id):
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    try:
        funcionarioProcesso = FuncionarioNoProcesso.query.filter(FuncionarioNoProcesso.id == funcionario_processo_id)
        funcionarioProcesso.delete()
        db.session.commit()
    except Exception as e:
        resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta
# *****************************************************************************************************

# ************************************* Rota para editar um Cargo *************************************
@app.route("/cargos/<int:cargo_id>", methods=["PUT"])
def editarCargo(cargo_id):
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    dados = request.get_json()
    if Validacao.validarTexto(dados.get("nome"), 50):
        try:
            cargos = db.session.query(Cargo).filter(Cargo.nome == dados.get("nome")).all()
            if not cargos or cargos[0].id == cargo_id:
                cargo = Cargo.query.filter(Cargo.id == cargo_id).first()
                cargo.nome = dados.get("nome")
                db.session.add(cargo)
                db.session.commit()
            else:
                resposta = jsonify({"resultado": "erro", "detalhes": "Já existe um cargo com esse nome!"})
        except Exception as e: 
            resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    else:
         resposta = jsonify({"resultado": "erro", "detalhes": "Informações inválidas!"})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta
# *****************************************************************************************************

# ************************************* Rota para editar um Tipo de Processo **************************
@app.route("/tipos/<int:tipo_id>", methods=["PUT"])
def editarTipo(tipo_id):
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    dados = request.get_json()
    if not Validacao.validarTexto(dados.get("nome"), 50):
        resposta = jsonify({"resultado": "erro", "detalhes": "Informações inválidas!"})
    elif not Validacao.validarTexto(dados.get("descricao"), 250):
        resposta = jsonify({"resultado": "erro", "detalhes": "Informações inválidas!"})
    else:
        try:
            tipos = db.session.query(TipoProcesso).filter(TipoProcesso.nome == dados.get("nome")).all()
            if not tipos or tipos[0].id == tipo_id:
                tipo = TipoProcesso.query.filter(TipoProcesso.id == tipo_id).first()
                tipo.nome = dados.get("nome")
                tipo.descricao = dados.get("descricao")
                db.session.add(tipo)
                db.session.commit()
            else:
                resposta = jsonify({"resultado": "erro", "detalhes": "Já existe um tipo de processo com esse nome!"})
        except Exception as e: 
            resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta
# *****************************************************************************************************

# ************************************* Rota para editar um Funcionario *******************************
@app.route("/funcionarios/<int:funcionario_id>", methods=["PUT"])
def editarFuncionario(funcionario_id):
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    dados = request.get_json()
    if Validacao.validarTexto(dados.get("nome"), 50):
        try:
            cargoFuncionario = db.session.query(Cargo).filter(Cargo.id == dados.get("cargo_id")).first()
            if cargoFuncionario != None:
                funcionario = Funcionario.query.filter(Funcionario.id == funcionario_id).first()
                funcionario.nome = dados.get("nome")
                funcionario.cargo = cargoFuncionario
                db.session.add(funcionario)
                db.session.commit()
            else:
                resposta = jsonify({"resultado": "erro", "detalhes": "Nenhum cargo encontrado!"})
        except Exception as e: 
            resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    else:
        resposta = jsonify({"resultado": "erro", "detalhes": "Informações inválidas!"})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta
# *****************************************************************************************************

# ************************************* Rota para editar uma Matéria-Prima ****************************
@app.route("/materias/<int:materia_id>", methods=["PUT"])
def editarMateria(materia_id):
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    dados = request.get_json()
    if not Validacao.validarTexto(dados.get("nome"), 50):
        resposta = jsonify({"resultado": "erro", "detalhes": "Informações inválidas!"})
    elif not Validacao.validarTexto(dados.get("descricao"), 250):
        resposta = jsonify({"resultado": "erro", "detalhes": "Informações inválidas!"})
    elif not Validacao.validarValor(dados.get("valorUnitario")):
        resposta = jsonify({"resultado": "erro", "detalhes": "Informações inválidas!"})
    elif not Validacao.validarTexto(dados.get("fornecedor"), 50):
        resposta = jsonify({"resultado": "erro", "detalhes": "Informações inválidas!"})
    else:
        try:
            materias = db.session.query(MateriaPrima).filter(MateriaPrima.nome == dados.get("nome")).all()
            if not materias or materias[0].id == materia_id:
                materia = MateriaPrima.query.filter(MateriaPrima.id == materia_id).first()
                materia.nome = dados.get("nome")
                materia.descricao = dados.get("descricao")
                materia.valorUnitario = dados.get("valorUnitario")
                materia.fornecedor = dados.get("fornecedor")
                db.session.add(materia)
                db.session.commit()
            else:
                resposta = jsonify({"resultado": "erro", "detalhes": "Já existe uma matéria-prima com esse nome!"})
        except Exception as e: 
            resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta
# *****************************************************************************************************

# ************************************* Rota para editar um Produto ***********************************
@app.route("/produtos/<int:produto_id>", methods=["PUT"])
def editarProduto(produto_id):
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    dados = request.get_json()
    if not Validacao.validarTexto(dados.get("nome"), 50):
        resposta = jsonify({"resultado": "erro", "detalhes": "Informações inválidas!"})
    elif not Validacao.validarTexto(dados.get("descricao"), 250):
        resposta = jsonify({"resultado": "erro", "detalhes": "Informações inválidas!"})
    else:
        try:
            produtos = db.session.query(Produto).filter(Produto.nome == dados.get("nome")).all()
            if not produtos or produtos[0].id == produto_id:
                produto = Produto.query.filter(Produto.id == produto_id).first()
                produto.nome = dados.get("nome")
                produto.descricao = dados.get("descricao")
                db.session.add(produto)
                db.session.commit()
            else:
                resposta = jsonify({"resultado": "erro", "detalhes": "Já existe um produto com esse nome!"})
        except Exception as e: 
            resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta
# *****************************************************************************************************

# ************************************* Rota para adicionar Estoque ***********************************
@app.route("/materiais/<int:material_id>", methods=["POST"])
def adicionarEstoque(material_id):
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    dados = request.get_json()
    if not Validacao.validarValor(dados.get("quantidade")):
        resposta = jsonify({"resultado": "erro", "detalhes": "Informações inválidas!"})
    else:
        try:
            material = db.session.query(Material).filter(Material.id == material_id).first()
            if material == None:
                resposta = jsonify({"resultado": "erro", "detalhes": "Nenhum material encontrado!"})
            else:
                material.atualizar_estoque(float(dados.get("quantidade")), True)
                db.session.add(material)
                db.session.commit()
        except Exception as e: 
            resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta
# *****************************************************************************************************

# ************************************* Rota para finalizar Processo **********************************
@app.route("/processos/<int:processo_id>/finalizar", methods=["POST"])
def finalizarProcesso(processo_id):
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    dados = request.get_json()
    try:
        processo = db.session.query(Processo).filter(Processo.id == processo_id).first()
        if processo == None:
            resposta = jsonify({"resultado": "erro", "detalhes": "Nenhum processo encontrado!"})
        else:
            processo.finalizar_processo(dados.get("aprovado"))
            db.session.add(processo)
            db.session.commit()
    except Exception as e: 
        resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta
# *****************************************************************************************************

# ************************************* Rota para finalizar Produção **********************************
@app.route("/producoes/<int:producao_id>/finalizar", methods=["POST"])
def finalizarProducao(producao_id):
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    try:
        producao = db.session.query(Producao).filter(Producao.id == producao_id).first()
        if producao == None:
            resposta = jsonify({"resultado": "erro", "detalhes": "Nenhuma produção encontrada!"})
        else:
            producao.finalizar_producao()
            db.session.add(producao)
            db.session.commit()
            print(producao.produto)
            print(producao.produto_id)
            producao.produto.calcular_valor_producao()
            producao.produto.calcular_valor_venda(10)
            db.session.add(producao.produto)
            db.session.commit()
    except Exception as e: 
        resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta
# *****************************************************************************************************

app.run(debug=True)