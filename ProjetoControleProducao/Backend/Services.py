from Config import *
from Models import Cargo, TipoProcesso

# ************************************* Rota para listar todos os Cargos ******************************
@app.route("/listarCargos")
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

# ************************** Rota para listar todos os Tipos de Processo ******************************
@app.route("/listarTiposProcesso")
def listarTiposProcesso():
    try:
        tipos_processo = db.session.query(TipoProcesso).all()
    except:
        tipos_processo = []
    tipos_processo_em_json = [ t.json() for t in tipos_processo ]
    resposta = jsonify(tipos_processo_em_json)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta
# *****************************************************************************************************

# ************************************* Rota para adicionar novo Cargo ********************************
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!! Não verifica se o cargo já está salvo no banco !!!!!!!!!!!!!!!!!!!!!!!!
@app.route("/incluirCargo", methods=['post']) 
def incluirCargo(): 
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"}) 
    dados = request.get_json() 
    try:
        new = Cargo(**dados) 
        db.session.add(new)
        db.session.commit()
    except Exception as e: 
        resposta = jsonify({"resultado":"erro", "detalhes":str(e)}) 
    resposta.headers.add("Access-Control-Allow-Origin", "*") 
    return resposta
# *****************************************************************************************************

# ************************************* Rota para excluir um Cargo ************************************
# !!!!!!!!!!!!!!!!!!!!!!!!! Não verifica se o Cargo está vinculado em um Funcionário !!!!!!!!!!!!!!!!!!
@app.route("/excluirCargo/<int:cargo_id>", methods=['DELETE'])
def excluirCargo(cargo_id):
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    try:
        Cargo.query.filter(Cargo.id == cargo_id).delete()
        db.session.commit()
    except Exception as e:
        resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta
# *****************************************************************************************************

app.run(debug=True)