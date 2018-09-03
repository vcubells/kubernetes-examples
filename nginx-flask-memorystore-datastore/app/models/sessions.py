import redis
import config

class Sessions(object):

    def __init__(self):
        if hasattr(config, 'REDIS_PASSWORD'):
            self.instance = redis.StrictRedis(
                host=config.REDIS_HOST,
                port=config.REDIS_PORT,
                password=config.REDIS_PASSWORD)
        else:
            self.instance = redis.StrictRedis(
                host= config.REDIS_HOST,
                port=config.REDIS_PORT)

    def get_active_sessions(self):
        """ Regresa las sesiones activas en Memorystore """

        size = self.instance.dbsize()

        return size

    def add(self, id):
        """ Crea una nueva sesión en Redis """

        result = self.instance.set(id, 1)

        return result