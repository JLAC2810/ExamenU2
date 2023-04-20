from Logger import log

class contrato_persona:
    def __init__(self, Id_Pesona=None, IdContrato=None) -> None:
        self._idpsersona=Id_Pesona
        self._idcontrato=IdContrato
        log.debug(contrato_persona)
    def __str__(self) -> str:
        return f'''
            IdPersona: {self._idpsersona}, IdContrato: {self._idcontrato}
        '''   
    
    @property
    def idPersona(self):
        return self.idPersona
    @idPersona.setter
    def idPersona(self,idpersona):
        return self.idPersona
    @property
    def idcontrato(self):
        return self._idcontrato
    @idcontrato.setter
    def idcontrato(self,idcontrato):
        return self._idcontrato