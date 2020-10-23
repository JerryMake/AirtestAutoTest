#coding = utf-8
#author     :CJQ
#Description:   a class that used to write log to file and console
#               get_logger: return the loogger
#               MyLog:use static method to call the Log


import logging,threading,os
from datetime import datetime
from lib.common import *
class Log:
    def __init__(self):

        logName = nowDate()+".log"
        fName = prePath("log", logName)
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)  #设置Logger的日志等级：INFO
        #create handler
        #detailLog = os.path.join(logPath, "detailLog")
        currentPath = fName
        fh = logging.FileHandler(currentPath,encoding="utf-8")
        formatter = logging.Formatter( '[%(asctime)s][%(thread)d][%(filename)s][line: %(lineno)d][%(levelname)s] ## %(message)s')
        fh.setFormatter(formatter)
        fh.setLevel(logging.INFO)   #日志文件输入log等级：INFO

        sh = logging.StreamHandler()
        sh.setFormatter(formatter)
        sh.setLevel(logging.WARNING) #控制台输入log等级：WARNING

        self.logger.addHandler(fh)
        self.logger.addHandler(sh)
    def get_logger(self):
        return self.logger


class MyLog:
    log = None
    mutex = threading.Lock()
    def __init__(self):
        pass
    #静态方法，不用实例化就可以直接调用该方法MyLog.get_log()
    @staticmethod
    def get_log():
        if MyLog.log is None:
            MyLog.mutex.acquire()
            MyLog.log = Log().get_logger()
            MyLog.mutex.release()
        return MyLog.log


'''if __name__ == "__main__":
    logger = MyLog.get_log()
    #logger = log.get_logger()
    logger.info("123")'''
