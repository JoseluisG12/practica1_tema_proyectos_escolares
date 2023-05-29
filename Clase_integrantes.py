
class integrante:
    __idproyecto : int
    __apellido : str
    __nombre : str
    __dni : int
    __categoria : int
    __rol :str

    def __init__(self,id,apellido,nombre,dni,categoria,rol):
        self.__idproyecto = id
        self.__apellido = apellido
        self.__nombre = nombre
        self.__dni = dni
        self. __categoria = categoria
        self. __rol = rol

    def getid(self):
        return self.__idproyecto

    def getcategoria(self):
        return self.__categoria

    def getrol(self):
        return self.__rol

    def getnombre(self):
        return self.__nombre



