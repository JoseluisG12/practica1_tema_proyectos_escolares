from Manejador_Projectos import  Lista_Proyectos
from Manejador_participantes import  Lista_Integrantes
from Clase_Menu import Menu

if __name__=='__main__':
    proyectos = Lista_Proyectos()
    proyectos.cargadatos()
    integrantes = Lista_Integrantes()
    integrantes.cargadatos()
    menu = Menu()
    menu.run(proyectos,integrantes)
