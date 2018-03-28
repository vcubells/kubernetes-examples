import redis
import config

class Sessions(object):

    def __init__(self):
        if config.REDIS_PASSWORD:
            self.instance = redis.StrictRedis(
                host=config.REDIS_HOST,
                port=config.REDIS_PORT,
                password=config.REDIS_PASSWORD)
        else:
            self.instance = redis.StrictRedis(
                host= config.REDIS_HOST,
                port=config.REDIS_PORT)


    def get_active_sessions(self):
        """ Regresa las sesiones activas en Redis """

        size = self.instance.dbsize()

        return size

    def add(self, id):
        """ Crea una nueva sesion en Redis """

        result = self.instance.set(id, 1)

        return result