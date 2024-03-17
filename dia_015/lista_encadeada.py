class UmPaciente:
    def __init__(self, paciente):
        self.paciente = paciente
        self.proximoPaciente = None

    def __repr__(self):
        return '%s -> %s' % (self.paciente, self.proximoPaciente)


lista_encadeada = UmPaciente('Marcos')
print(lista_encadeada)
