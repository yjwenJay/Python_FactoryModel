from abc import ABCMeta, abstractmethod

'''
抽象接口 必须实现接口的方法
'''


class IQuartz(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def ShowName(self):
        pass

    def ShowTime(self):
        pass


'''
非抽象接口 可不必实现所有的方法
'''
