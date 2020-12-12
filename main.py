import tkinter
import pickle

class Contactos():
    def __init__(self,telefono,nombre,apellidos):
        self.telefono = telefono
        self.nombre = nombre
        self.apellidos = apellidos

    def imprimir(self):
        print("Telefono : " + str(self.telefono) + " | Nombre : " + self.nombre + " | Apellidos :" + self.apellidos)

    def __str__(self):
        return "Telefono : {} | Nombre : {} | Apellidos : {}".format(self.telefono,self.nombre,self.apellidos)

class ListaContactos:

    contactos=[]

    def __init__(self):
        try:
            listaDeContactos=open("fichero_contactos","ab+")
            listaDeContactos.seek(0)

            self.contactos=pickle.load(listaDeContactos)
        except:
            print("")
        finally:
            listaDeContactos.close()
            del(listaDeContactos)

    def guardarContactosFichero(self):
        listaDeContactos = open("fichero_contactos","wb")
        pickle.dump(self.contactos,listaDeContactos)
        listaDeContactos.close()
        del (listaDeContactos)

    def añadirContacto(self,p):
        self.contactos.append(p)
        self.guardarContactosFichero()

    def eliminarContacto(self,p):
        self.contactos.pop(p)
        self.guardarContactosFichero()

    def mostrarContactos(self):
        for item in self.contactos:
            print(item)


ventana = tkinter.Tk()
ventana.geometry("400x300")

telLabel = tkinter.Label(ventana,text="Telefono:")
telLabel.pack()

telefono = tkinter.Entry(ventana)
telefono.pack()

nomLabel = tkinter.Label(ventana,text="Nombre:")
nomLabel.pack()

nombre = tkinter.Entry(ventana)
nombre.pack()

apelLabel = tkinter.Label(ventana,text="Apellidos:")
apelLabel.pack()

apellidos = tkinter.Entry(ventana)
apellidos.pack()


def crearContacto():

    tel = telefono.get()
    nom = nombre.get()
    apel = apellidos.get()

    contacto = Contactos(tel, nom, apel)

    listaContactos = ListaContactos()

    listaContactos.añadirContacto(contacto)


def mostrarContactos():
    listaContactos = ListaContactos()

    listaContactos.mostrarContactos()

def eliminarContacto(numero):

    try:

        listaContactos = ListaContactos()

        listaContactos.eliminarContacto(numero)

    except:
        print("No se puede borrar nada porque el fichero está vacío")




seleccion = tkinter.Label(ventana,text="Seleccione una opcion")
seleccion.pack()

boton1 = tkinter.Button(ventana,text="Alta",command = crearContacto)
boton1.pack(side=tkinter.LEFT)

boton2 = tkinter.Button(ventana,text="Baja",command = lambda: eliminarContacto(0))
boton2.pack(side=tkinter.RIGHT)

boton4 = tkinter.Button(ventana,text="Visualizar",command = mostrarContactos)
boton4.pack(side=tkinter.TOP)

ventana.mainloop()


