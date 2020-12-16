
import os,datetime,re
import configparser
from functools import wraps
import logging,time

nowPath = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
prePath = lambda *x: os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), *x)

nowTime = lambda: datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
nowDate = lambda: datetime.datetime.now().strftime("%Y-%m-%d")



def today(fmt,delt=0):
    date = (datetime.datetime.now()+datetime.timedelta(days=delt)).strftime(fmt)
    return date

def extract_digit(strData):
    s = re.sub("\D", "", strData)
    return s

def get_file_data(sector,item):
    file = prePath('config', sector + ".cfg")
    conf = configparser.ConfigParser()
    conf.read(file, encoding="utf-8")
    value = conf.get(sector, item)
    return value

def Logging(sMsg):
    logging.error(sMsg)
    print(sMsg)


def RetryFunc(iTimes=3, iSec=2):
    def CatchErr(func):
        @wraps(func)
        def MyWrapper(*args, **kwargs):
            for _ in range(iTimes):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    Logging(e)
                    time.sleep(iSec)
                    continue

        return MyWrapper

    return CatchErr