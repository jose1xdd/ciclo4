from modelos.partido import Partido
from repositorios.repositoriopartido import RepositorioPartido
class ControladorPartido():
    def __init__(self):
        self.repositorioPartido = RepositorioPartido()

    def index(self):
        return self.repositorioPartido.findAll()

    def create(self, elPartido):
        nuevoPartido = Partido(elPartido)

        return self.repositorioPartido.save(nuevoPartido)

    def show(self, id):
        elPartido = Partido(self.repositorioPartido.findById(id))

        return elPartido.__dict__

    def update(self, id, elPartido):
        PartidoActual = Partido(self.repositorioPartido.findById(id))
        PartidoActual.id = elPartido["id"]
        PartidoActual.nombre = elPartido["nombre"]
        PartidoActual.lema = elPartido["lema"]
        return self.repositorioPartido.save(PartidoActual)

    def delete(self, id):
        return self.repositorioPartido.delete(id)