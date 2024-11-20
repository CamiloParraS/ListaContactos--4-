__author__="juan camilo parra"
__license__="GPL"
__version__="1.0.0"
__Email__="juan.parrasan@campusucc.edu.co"

from Mundo.Contacto import Contacto

class ListaDeContactos:
    def __init__(self):
        self.contactos = []

    def darTodosLosContactos(self):
        return [f"{contacto.darNombre()} {contacto.darApellido()}" for contacto in self.contactos] 
 
    def buscarContactosPalabraClave(self, palabra):
        resultado = []
        for contacto in self.contactos:
            nombre = contacto.darNombre()
            apellido = contacto.darApellido()
            palabras_clave = contacto.darPalabras()
        
            if palabra in palabras_clave:
                resultado.append(f"{nombre} {apellido}")
                
            elif palabra in nombre:
                resultado.append(f"{nombre} {apellido}")
                
            elif palabra in apellido:
                resultado.append(f"{nombre} {apellido}")
        return resultado
    
    def buscarContacto(self, nombre, apellido):
        for contacto in self.contactos:
            if contacto.darNombre() == nombre and contacto.darApellido() == apellido:
                return contacto
        return None

    def agregarContacto(self, nombre, apellido, direccion, correo, telefonos, palabras):
        if self.buscarContacto(nombre, apellido):
            return 0
        nuevo_contacto = Contacto(nombre, apellido, direccion, correo)
        for telefono in telefonos:
            nuevo_contacto.agregarTelefono(telefono)
        for palabra in palabras:
            nuevo_contacto.agregarPalabra(palabra)
        self.contactos.append(nuevo_contacto)
        return 1

    def eliminarContacto(self, nombre, apellido):
        contacto_a_eliminar = self.buscarContacto(nombre, apellido)
        if contacto_a_eliminar:
            self.contactos.remove(contacto_a_eliminar)

    def modificarContacto(self, nombre, apellido, direccion, correo, telefonos, palabras):
        contacto_a_modificar = self.buscarContacto(nombre, apellido)
        if contacto_a_modificar:
            contacto_a_modificar.direccion = direccion
            contacto_a_modificar.correo = correo
            contacto_a_modificar.telefonos = telefonos
            contacto_a_modificar.palabras = palabras

    def actualizarTelefonos(self, telefonos, contacto):
        contacto.telefonos = telefonos  

    def actualizarPalabras(self, palabras, contacto):
        contacto.palabras = palabras  

    def metodo1(self):
        pass

    def metodo2(self):
        pass