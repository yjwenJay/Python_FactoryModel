from Interface.IFactory import IFactory
from AbstractFactory.TISSOTQuartz import TISSOTQuartz


class TISSOTFactory(IFactory):
    def __init__(self):
        pass

    def createQuartz(self):
        TISSOTQuartz()

    def createEletronic(self):
        pass

    def createMechanical(self):
        pass
