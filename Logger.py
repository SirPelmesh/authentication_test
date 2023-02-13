import logging

class Logg():
    def __init__(self):
        self.logger = logging.getLogger()

    def makeLog(self,text):
        self.logger.info(msg=text)
