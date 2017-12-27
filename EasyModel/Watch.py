import time
from EasyModel.Quartz import Quartz
from EasyModel.Eletronic import Eletronic
from EasyModel.Mechanical import Mechanical
from EasyModel.Switch import Switch


class Watch:
    watchId = 0

    def __init__(self, watchID):
        self.watchId = watchID
        dateStr = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        print("Time Now:{0}".format(dateStr))
        self.GetWatch(self.watchId)
        '''
        /// 默认为石英表
        /// 1--电子表
        /// 2--机械表 
       '''

    def GetWatch(self, watchId):
        for Case in Switch(watchId):
            if Case(0):
                Quartz()
                break
            if Case(1):
                Eletronic()
                break
            if Case(2):
                Mechanical()
                break

            if Case():  # 默认
                print("Default value for my argument.")
                break
