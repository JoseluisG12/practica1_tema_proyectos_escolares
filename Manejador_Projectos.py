from Clase_Projecto import Proyecto
import csv
class Lista_Proyectos:
    __Proyectos : list

    def __init__(self):
        self.__Proyectos = []

    def cargadatos(self):
        archivo = open('Proyectos.csv')
        reader  = csv.reader(archivo,delimiter=(';'))
        next(reader)
        for fila in reader:
            id = fila[0]
            titulo = fila[1]
            palabras = fila[2]
            proyecto = Proyecto(id,titulo,palabras)
            self.__Proyectos.append(proyecto)
        archivo.close()

    def calcularpuntos(self,integrantes):
        print("Reglas")
        print("El Director del Proyecto debe tener categoría I o II")
        print("El Codirector del Proyecto debe tener como mínimo categoría III")
        print("El Proyecto debe tener como mínimo 3 integrantes")
        for projecto in self.__Proyectos:
            puntos_A = 0
            cont_integrantes = 0
            band_director = False
            band_codirector = False
            for integrante in integrantes:
                if integrante.getid() == projecto.getid():
                    cont_integrantes = cont_integrantes + 1

                    if integrante.getrol() == 'Director' and integrante.getcategoria() == '1' :
                        puntos_A = puntos_A + 10
                        band_director = True
                    if integrante.getrol() == 'Director' and  integrante.getcategoria() == '2':
                        puntos_A = puntos_A + 10
                        band_director = True

                    if integrante.getrol() == 'Codirector' and integrante.getcategoria() == '3':
                        puntos_A = puntos_A + 10
                        band_codirector = True
            if cont_integrantes < 3:
                puntos_A = puntos_A - 20
            if  band_director == False:
                puntos_A = puntos_A - 5
            if  band_codirector == False:
                puntos_A = puntos_A - 5
            projecto.setpuntaje(puntos_A)

    def mostrarproyectos(self):
        self.__Proyectos.sort()
        for proyectos in self.__Proyectos:
            print("""
Proyecto {}
Puntos: {}
id:{}
palabras clave : [{}]""".format(proyectos.gettitulo(),proyectos.getpuntaje(),proyectos.getid(),proyectos.getpalabras()))

    def ranking(self):


        for i in range(len(self.__Proyectos)):
            print("""
Puesto {}
TITULO : {}
Puntaje:{}""".format(i + 1,self.__Proyectos[i].gettitulo(),self.__Proyectos[i].getpuntaje()))









