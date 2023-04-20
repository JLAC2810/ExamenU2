import logging as log

log.basicConfig(level=log.DEBUG,
    format="%(asctime)s: %(levelname)s [%(filename)s]:%(lineno)s %(message)s",
    datefmt='%I:%M:%S %p',
    handlers=[
    #el archivo de guarda en la ubicacion marcada
        log.FileHandler('registros_de_logexamen.log'),
        log.StreamHandler()
    ])


if __name__ == '__main__':
    log.debug("Mensaje Debug")