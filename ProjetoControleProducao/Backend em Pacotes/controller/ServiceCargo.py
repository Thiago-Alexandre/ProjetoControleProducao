import sys 
import os
sys.path.append(os.path.abspath("./"))
from config.Config import *
from model.Cargo import Cargo

@app.route("/listarCargos")
def listar_cargos():
    cargos = db.session.query(Cargo).all()
    cargos_em_json = [ c.json() for c in cargos ]
    resposta = jsonify(cargos_em_json)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

app.run(debug=True)