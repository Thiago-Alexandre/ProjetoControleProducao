from Config import *
from Models import Cargo, TipoProcesso

@app.route("/listarCargos")
def listar_cargos():
    try:
        cargos = db.session.query(Cargo).all()
    except:
        cargos = []
    cargos_em_json = [ c.json() for c in cargos ]
    resposta = jsonify(cargos_em_json)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

@app.route("/listarTiposProcesso")
def listar_tipos_processo():
    try:
        tipos_processo = db.session.query(TipoProcesso).all()
    except:
        tipos_processo = []
    tipos_processo_em_json = [ t.json() for t in tipos_processo ]
    resposta = jsonify(tipos_processo_em_json)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

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

app.run(debug=True)