import csv
from Clase_integrantes import integrante
class Lista_Integrantes:
    __Integrantes: list

    def __init__(self):
        self.__Integrantes = []

    def cargadatos(self):
        archivo = open('integrantesProyecto.csv')
        reader = csv.reader(archivo,delimiter=(';'))
        next(reader)
        for fila in reader:
            id = fila[0]
            apellido = fila[1]
            Nombre = fila[2]
            dni = fila[3]
            categoria = fila[4]
            rol = fila[5]
            participantes = integrante(id,apellido,Nombre,dni,categoria,rol)
            self.__Integrantes.append(participantes)
        archivo.close()

    def getlista(self):
        return self.__Integrantes

    def mostradatos(self):
        for inte in self.__Integrantes:
            print(inte.getnombre())