
class Menu:
    __switcher = None

    def __init__(self):
        self.__switcher = {1:self.op1,
                           2:self.op2

        }

    def run(self,proyectos,integrantes):
        band = True
        while band:
            b = int(input("""
Menu Pirncipal:
1-para ordenar los proyectos de mayor a menor puntaje
2-ranking de puntaje
\n"""))
            func = self.__switcher.get(b)
            if func:
                func(proyectos,integrantes)
            else:
                print("saliendo")
                band = False

    def op1(self,proyectos,integrantes):
        integrantes_proyectos = integrantes.getlista()
        proyectos.calcularpuntos(integrantes_proyectos)
        proyectos.mostrarproyectos()

    def op2(self,proyectos,participantes):
        proyectos.ranking()