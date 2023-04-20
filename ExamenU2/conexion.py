import psycopg2 as bd
import sys
from psycopg2 import pool
from Logger import log


class conexiones:
    _HOST="127.0.0.1"
    _PASSWORD="l16100172"
    _USER="postgres"
    _PORT="5432"
    _DATABASE="examenU2"
    _MIN_CON=1
    _MAX_CON=5
    _pool=None

    @classmethod
    def ObtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON, cls._MAX_CON, host=cls._HOST,
                                                       user=cls._USER, password=cls._PASSWORD,
                                                       port=cls._PORT,database=cls._DATABASE)
               #guardara el evento en el log creado
                log.debug(f'Se creo exitasamente el pool {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'Ocurrio un error en el pool{e}')
                sys.exit()

        else:
            return cls._pool
    @classmethod
    def Obtener_conexion(cls):
        conection= cls.ObtenerPool().getconn()
        #guardara el evento de que se pudo conectar a la base de datos
        log.debug(f'Conexion obtenida: {conection}')
        return conection

    @classmethod
    def liberar_conexion(cls,conection):
        cls.ObtenerPool().putconn(conection)
        #guardara el evento de que se libero una conexion
        log.debug(f'Conexion finalizada: {conection}')

    @classmethod
    def cerrar_conexion(cls):
        cls.ObtenerPool().closeall()
#genera conexiones a la base de datos
if __name__ =='__main__':
        conexion1 = conexiones.Obtener_conexion()
        conexion2 = conexiones.liberar_conexion(conexion1)
        
