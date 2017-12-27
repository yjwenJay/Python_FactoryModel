import time
from EasyModel.IProduct import IProduct  # 引入同目录的IProduct接口       import EasyModel.IProduct


class Eletronic(IProduct):  # 必须实现interface中的所有函数，否则会编译错误
    def __init__(self):
        self.ShowTime()

    def ShowName(self):
        print("I'm Eletronic Watch。")

    def ShowTime(self):
        dateStr = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        print("Time Now:{0}".format(dateStr))
