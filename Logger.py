import logging

class Logg():
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        logging.basicConfig(level=logging.WARNING, filename=f'{name}.log', filemode="w")
        logging.StreamHandler(stream=None)
        #logging.FileHandler(filename=f'{name}.log', filemode="w")

    #@staticmethod
    def makeLog(self,text):
        self.logger.info(msg=text)
