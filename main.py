from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
from controladores.controladorCandidato import ControladorCandidato
from controladores.controladorPartido import ControladorPartido
from controladores.controladorResultado import ControladorResultado

app = Flask(__name__)
cors = CORS(app)
miControladorCandidato=ControladorCandidato()
miControladorPartido=ControladorPartido()
miControladorResultado=ControladorResultado()

def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

@app.route("/", methods=['GET'])
def test():
    json = {}
    json["message"] = "Server running ..."
    return jsonify(json)

if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running : " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])

#########################  candidato  #########################

@app.route("/Candidatos",methods=['GET'])
def getCandidatos():
    json=miControladorCandidato.index()
    return jsonify(json)

@app.route("/Candidatos",methods=['POST'])
def crearCandidato():
    data = request.get_json()
    json=miControladorCandidato.create(data)
    return jsonify(json)

@app.route("/Candidatos/<string:id>",methods=['GET'])
def getCandidato(id):
    json=miControladorCandidato.show(id)
    return jsonify(json)

@app.route("/Candidatos/<string:id>",methods=['PUT'])
def modificarCandidato(id):
    data = request.get_json()
    json=miControladorCandidato.update(id,data)
    return jsonify(json)

@app.route("/Candidatos/<string:id>",methods=['DELETE'])
def eliminarCandidato(id):
    json=miControladorCandidato.delete(id)
    return jsonify(json)

#########################  partido  #########################

@app.route("/Partido",methods=['GET'])
def getPartido():
    json=miControladorPartido.index()
    return jsonify(json)

@app.route("/Partido",methods=['POST'])
def crearPartido():
    data = request.get_json()
    json=miControladorPartido.create(data)
    return jsonify(json)

@app.route("/Partido/<string:id>",methods=['GET'])
def getPartido(id):
    json=miControladorPartido.show(id)
    return jsonify(json)

@app.route("/Partido/<string:id>",methods=['PUT'])
def modificarPartido(id):
    data = request.get_json()
    json=miControladorPartido.update(id,data)
    return jsonify(json)

@app.route("/Partido/<string:id>",methods=['DELETE'])

def eliminarPartido(id):
    json=miControladorPartido.delete(id)
    return jsonify(json)

#########################  resultado  #########################

@app.route("/Resultado",methods=['GET'])
def getResultado():
    json=miControladorResultado.index()
    return jsonify(json)

@app.route("/Resultado",methods=['POST'])
def crearResultado(numero_mesa,id_partido):
    data = request.get_json()
    json=miControladorResultado.create(data, numero_mesa, id_partido)
    return jsonify(json)

@app.route("/Resultado/<string:id>",methods=['GET'])
def getResultado(id):
    json=miControladorResultado.show(id)
    return jsonify(json)

@app.route("/Resultado/<string:id>",methods=['PUT'])
def modificarResultado(id,numero_mesa,id_partido):
    data = request.get_json()
    json=miControladorResultado.update(id,data,numero_mesa,id_partido)
    return jsonify(json)

@app.route("/Resultado/<string:id>",methods=['DELETE'])
def eliminarResultado(id):
    json=miControladorResultado.delete(id)
    return jsonify(json)


