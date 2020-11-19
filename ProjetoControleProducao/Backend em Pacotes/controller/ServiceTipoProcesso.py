import sys 
import os
sys.path.append(os.path.abspath("./"))
from config.Config import *
from model.TipoProcesso import TipoProcesso

@app.route("/listarTiposProcesso")
def listar_tipos_processo():
    tipos_processo = db.session.query(TipoProcesso).all()
    tipos_processo_em_json = [ c.json() for c in tipos_processo ]
    return jsonify(tipos_processo_em_json)

app.run(debug=True)