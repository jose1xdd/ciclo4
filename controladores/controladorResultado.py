from modelos.resultado import Resultado
from repositorios.repositorioResultado import RepositorioResultado

class ControladorResultado():
    def __init__(self):
        self.repositorioResultado = RepositorioResultado()

    def index(self):
        return self.repositorioResultado.findAll()

    def create(self, elResultado):
        ResultadoFinal = Resultado(elResultado)

        return self.repositorioResultado.save(ResultadoFinal)

    def show(self, id):
        elResultado = Resultado(self.repositorioResultado.findById(id))

        return elResultado.__dict__

    def update(self, id, elResultado):
        ResultadoActual = Resultado(self.repositorioResultado.findById(id))
        ResultadoActual.id = elResultado["id"]
        ResultadoActual.numero_mesa = elResultado["numero_mesa"]
        ResultadoActual.id_partido = elResultado["id_partido"]
        return self.repositorioResultado.save(ResultadoActual)

    def delete(self, id):
        return self.repositorioResultado.delete(id)
