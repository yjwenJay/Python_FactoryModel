from Factory.IFactory import IFactory
from Factory.Quartz import Quartz


class QuartzFactory(IFactory):
    def __init__(self):
        self.getProduct()

    def getProduct(self):
        return Quartz()
