
class Proyecto:
    __id : int
    __titulo : str
    __palabras_clave : str
    __puntaje : int

    def __init__(self,id,titulo,palabras):
        self.__id = id
        self. __titulo = titulo
        self. __palabras_clave = palabras
        self.__puntaje = 0

    def getid(self):
        return self.__id

    def gettitulo(self):
        return self.__titulo

    def getpalabras(self):
        return self.__palabras_clave

    def getpuntaje(self):
        return self.__puntaje

    def setpuntaje(self,puntos):
        self.__puntaje = puntos

    def __gt__(self, other):
        if self.__puntaje < other.__puntaje:
            return True