from Logger import log
from conexion import conexiones
class CursorDePool:
    def __init__(self):
       self._conexion= None
       self._cursor= None
    def __enter__(self):
        log.debug("Inicio metodo with")
        self._conexion=conexiones.Obtener_conexion()
        self._cursor=self._conexion.cursor()
        return self._cursor
  
    def __exit__(self, tipo_excepcion, valor_excepcion, detalle_excepcion):
      
       log.debug("Se ejecuta exit")
       if valor_excepcion:
          self._conexion.rollback()
       else:
          self._conexion.commit()
          self._cursor.close()
       conexiones.liberar_conexion(self._conexion)
