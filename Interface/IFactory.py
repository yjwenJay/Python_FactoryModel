from abc import ABCMeta, abstractmethod

'''
抽象接口 必须实现接口的方法
'''


class IFactory(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def createQuartz(self):
        pass

    def createEletronic(self):
        pass

    def createMechanical(self):
        pass


'''
非抽象接口 可不必实现所有的方法
'''
