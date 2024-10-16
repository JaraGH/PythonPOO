# Clases Contacto y Agenda


class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def __str__(self):
        return f"Nombre: {self.nombre}, Telefono: {self.telefono}, Email: {self.email}"

    def __repr__(self):
        return f"Contacto({self.nombre}, {self.telefono}, {self.email})"

    def __eq__(self, otro):
        return (
            self.nombre == otro.nombre
            and self.telefono == otro.telefono
            and self.email == otro.email
        )


class Agenda:
    lista_contactos = [
        Contacto("Juan", "1234567890", "juan@johnq.es"),
        Contacto("Pepe", "0987654321", "pepe@gggamil.com"),
        Contacto("Maria", "6789012345", "maria@joomla.es"),
        Contacto("Ana", "5432167890", "ana@hotmail.com"),
        Contacto("Luis", "988567890", "luis@marino.es"),
        Contacto("Carmen", "876567890", "carmen@arroba.com"),
        Contacto("Sara", "934567890", "sara@gmaill.es"),
        Contacto("Pedro", "926567890", "peter@parker.com"),
        Contacto("Batman", "9334333330", "batman@bat.com"),
    ]

    @classmethod
    def buscar(cls, nombre):
        for contacto in cls.lista_contactos:
            if contacto.nombre.lower() == nombre.lower():
                return contacto
        return None

    @classmethod
    def telefono_contacto(cls, nombre):
        contacto = cls.buscar(nombre)
        if contacto:
            return contacto.telefono
        return None

    @classmethod
    def email_contacto(cls, nombre):
        contacto = cls.buscar(nombre)
        if contacto:
            return contacto.email
        return None

    @classmethod
    def cambiar_telefono(cls, nombre, telefono):
        contacto = cls.buscar(nombre)
        if contacto:
            contacto.telefono = telefono
            return True
        return False

    @classmethod
    def cambiar_email(cls, nombre, email):
        contacto = cls.buscar(nombre)
        if contacto:
            contacto.email = email
            return True
        return False

    @classmethod
    def listar_todos(cls):
        for c in cls.lista_contactos:
            print(c)

    @classmethod
    def contar_contactos(cls):
        return len(cls.lista_contactos)
