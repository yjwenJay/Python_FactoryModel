from Interface.IQuartz import IQuartz
import time


class TISSOTQuartz(IQuartz):

    def __init__(self):
        self.ShowName()
        self.ShowTime()

    def ShowName(self):
        print("I'm TISSOT quartz watch.")

    def ShowTime(self):
        dateStr = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        print("Time Now:{0}".format(dateStr))
