class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
    def clear(cls):
        try:
            del Singleton._instances[cls]
        except KeyError:
            pass
        # cls._instances={}

    '''    def __init__(cls, name, bases, methods):
            cls._instance = None
            super().__init__(name, bases, methods)'''
