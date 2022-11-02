from modelos.resultado import Resultado

class ControladorResultado():
    def __init__(self):
        print("Creando ControladorResultado")

    def index(self):
        print("Listar todos los Resultados")

    def create(self, elResultado):
        print("Crear un Resultado")

    def show(self, id):
        print("Mostrando un Resultado con id ", id)

    def update(self, id, elResultado):
        print("Actualizando Resultado con id ", id)

    def delete(self, id):
        print("Elimiando Resultado con id ", id)
