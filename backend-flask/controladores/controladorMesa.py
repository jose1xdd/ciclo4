from modelos.mesa import Mesa
from repositorios.repositorioMesa import RepositorioMesa


class ControladorMesa():
    def __init__(self):
        self.repositorioMesa = RepositorioMesa()

    def index(self):
        return self.repositorioMesa.findAll()

    def create(self, LaMesa):
        nuevaMesa = Mesa(LaMesa)

        return self.repositorioMesa.save(nuevaMesa)

    def show(self, id):
        LaMesa = Mesa(self.repositorioMesa.findById(id))

        return Mesa.__dict__

    def update(self, id, LaMesa):
        MesaActual = Mesa(self.repositorioMesa.findById(id))
        MesaActual.id = LaMesa["numero"]
        MesaActual.nombre = LaMesa["cantidadInscritos"]
        return self.repositorioMesa.save(MesaActual)

    def delete(self, id):
        return self.repositorioMesa.delete(id)
