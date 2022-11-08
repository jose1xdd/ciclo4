from modelos.resultado import Resultado
from modelos.mesa import Mesa
from modelos.candidato import Candidato
from repositorios.repositorioMesa import RepositorioMesa
from repositorios.repositoriocandidato import RepositorioCandidato
from repositorios.repositorioResultado import RepositorioResultado


class ControladorResultado():
    def __init__(self):
        self.repositorioResultado = RepositorioResultado()
        self.repositorioCandidato = RepositorioCandidato()
        self.repostiorioMesa = RepositorioMesa()

    def index(self):
        return self.repositorioResultado.findAll()

    def create(self, data, id_candidato, id_mesa):
        nuevoResultado = Resultado(data)
        candidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        mesa = Mesa(self.repostiorioMesa.findById(id_mesa))
        nuevoResultado.candidato = candidato
        nuevoResultado.mesa = mesa
        return self.repositorioResultado.save(nuevoResultado)

    def show(self, id):
        elResultado = Resultado(self.repositorioResultado.findById(id))

        return elResultado.__dict__

    def update(self, id, id_candidato, id_mesa):
        nuevoResultado = Resultado(self.repositorioResultado.findById(id))
        candidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        mesa = Mesa(self.repostiorioMesa.findById(id_mesa))
        nuevoResultado.candidato = candidato
        nuevoResultado.mesa = mesa
        return self.repositorioResultado.save(nuevoResultado)

    def delete(self, id):
        return self.repositorioResultado.delete(id)
