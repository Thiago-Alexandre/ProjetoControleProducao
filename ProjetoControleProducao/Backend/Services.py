from Config import *
from Models import Cargo, TipoProcesso

@app.route("/listarCargos")
def listar_cargos():
    cargos = db.session.query(Cargo).all()
    cargos_em_json = [ c.json() for c in cargos ]
    resposta = jsonify(cargos_em_json)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

@app.route("/listarTiposProcesso")
def listar_tipos_processo():
    tipos_processo = db.session.query(TipoProcesso).all()
    tipos_processo_em_json = [ t.json() for t in tipos_processo ]
    resposta = jsonify(tipos_processo_em_json)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

app.run(debug=True)