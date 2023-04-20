from Contrato import Contrato
from cursorpool import CursorDePool
from Logger import log
class ContratoDAO:

    _SELECCIONAR = "SELECT * FROM Contrato "
    _INSERTAR = "INSERT INTO Contrato(id,NoContrato,Costo,FechaInicio,FechaFin) Values(%s,%s,%s,%s)"
    _ACTUALIZAR ="UPDATE Contrato SET NoContrato=%s,FechaInicio=%s,FechaFin=%s,  WHERE NoContrato=%s"
    _ELIMINAR = "DELETE FROM Contrato WHERE NoContrato=%s"

    @classmethod
    # medotod para seleccionar un alumno de la tabla de la base de datos
    def seleccionarAlumnos(cls):
        with CursorDePool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            Contratoss =[]
            for r in registros:
                Contrato = Contrato(r[0],r[1],r[2],r[3])
                Contratoss.append(Contrato)
                #guardara el registro de que se consulto la tabla de alumnos
            log.debug(f"Consulta de Contratos realizada {Contratoss}")    
            return Contrato

    @classmethod
    # metodo para insertar un alumno a la tabla de la base de datos
    def insertarContrato(cls,Contrato):
        with CursorDePool() as cursor:
            valores = (Contrato.NoContrato,Contrato.Costo,Contrato.FechaInicio,Contrato.FechaFin)
            cursor.execute(cls._INSERTAR,valores)
            #guardara registro de que se agrego un alumno a la tabla
            log.debug(f"Contrato agregado {Contrato}")
            return cursor.rowcount
    @classmethod
    #metodo utilizado para actualizar la informacion de un alumno en la tabla 
    def actualizarContrato(cls,Contrato):
        with CursorDePool() as cursor:
            valores = (Contrato.NoContrato,Contrato.Costo,Contrato.FechaInicio,Contrato.FechaFIn,)
            cursor.execute(cls._ACTUALIZAR,valores)
            log.debug(f"Alumno Actualizado {Contrato}")
            return cursor.rowcount

    @classmethod
    #metodo utilizado para eliminar un alumno de la tabla en la base de datos
    def eliminarContrato(cls,Contrato):
        with CursorDePool() as cursor:
            valores = (Contrato.NoContrato)
            cursor.execute(cls._ELIMINAR,valores)
            #guardara el registro de que se elimino un alumno de la tabla
            log.debug(f"Contrato eliminado {Contrato}")
            return cursor.rowcount