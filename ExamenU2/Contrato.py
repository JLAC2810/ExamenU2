from Logger import log
class Contrato:
    def __init__(self,id=None, NoControl=None, Costo=None,FechaInicio=None,FechaFin=None) -> None:
        self._Id=id
        self._NoControl=NoControl
        self._Costo=Costo
        self._FechaInicio=FechaInicio
        self._FechaFin=FechaFin
        log.debug(Contrato)
    def __str__(self) -> str:
        return f'''
            Id: {self._Id}, NoControl: {self._NoControl},
            Costo: {self._Costo}, FechaInicio: {self._FechaInicio}, FechaFin:{self._FechaFin}
        '''

#propiedades get y set
    @property
    def Id(self):
        return self._Id
    @Id.setter
    def Id(self,Id):
        return self._Id
    @property
    def NoControl(self):
        return self._NoControl
    @NoControl.setter
    def NoControl(self,NoControl):
        return self.NoControl
    @property
    def Costo(self):
        return self._Costo
    @Costo.setter
    def Costo(self,Costo):
        return self._Costo
    @property
    def FechaInicio(self):
        return self.FechaInicio
    @FechaInicio.setter
    def FechaInicio(self,FechaInicio):
        return self._FechaInicio
    @property
    def FechaFin(self):
        return self._FechaFin
    @FechaFin.setter
    def FechaFin(self,FechaFin):
        return self._FechaFin