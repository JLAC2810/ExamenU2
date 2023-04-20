from Logger import log

class Persona:
    def __init__(self, Id=None, Nombre=None,Edad=None,Correo=None) -> None:
        self._id=Id
        self._Nombre=Nombre
        self._Edad=Edad
        self._Correo=Correo
        log.debug(Persona)
    def __str__(self) -> str:
        return f'''
            Id: {self._id}, Nombre: {self._Nombre},
            Edad: {self._Edad}, Correo: {self._Correo}
        '''   
    @property
    def id(self):
        return self._id
    @id.setter
    def Id (self,id):
        return self._id
    @property
    def nombre(self):
        return self._Nombre
    @nombre.setter
    def nombre(self,nombre):
        return self._Nombre
    @property
    def edad(self):
        return self._Edad
    @edad.setter
    def edad(self,edad):
        return self._Edad
    @property
    def correo(self):
        return self._Correo
    @correo.setter
    def correo(self, correo):
        return self._Correo