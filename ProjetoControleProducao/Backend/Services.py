from Config import *
from Models import *

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

# ************************************* Rota para listar todos os Processos ***************************
@app.route("/processos")
def listarProcessos():
    try:
        processos = db.session.query(Processo).all()
    except:
        processos = []
    processos_em_json = [ p.json() for p in processos ]
    resposta = jsonify(processos_em_json)
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

# ************************************* Rota para listar todos as Materias-Prima **********************
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
@app.route("/producao/<int:producao_id>")
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


# ************************************* Rota para adicionar novo Cargo ********************************
@app.route("/cargos", methods=['POST']) 
def incluirCargo(): 
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"}) 
    dados = request.get_json() 
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
        print(funcionarios)
        if not funcionarios:
            cargo.delete()
            db.session.commit()
        else:
            resposta = jsonify({"resultado":"erro", "detalhes":"Objeto Cargo em uso!"})
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
    try:
        cargos = db.session.query(Cargo).filter(Cargo.nome == dados.get("nome")).all()
        if not cargos:
            cargo = Cargo.query.filter(Cargo.id == cargo_id).first()
            cargo.nome = dados.get("nome")
            db.session.add(cargo)
            db.session.commit()
        else:
            resposta = jsonify({"resultado": "erro", "detalhes": "Já existe um cargo com esse nome!"})
    except Exception as e:
        resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta
# *****************************************************************************************************

app.run(debug=True)