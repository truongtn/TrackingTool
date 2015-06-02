
import fixpath
from colorama import init, Fore, Back, Style
import sys

from deface.httptruong import *
from log.logcenter import *
from config import *
from alert.alertcenter import *
def checkddos(name,code,timeout):
    init()
    if timeout>=TIME_OUT:
        print(Fore.YELLOW+ "[WARNING]:"+time_log("date")+" "+time_log("time")+" "+name+": server response time is too long ("+str(timeout)+" seconds)")
        logcenter("[WARNING]: "+name+": server response time is too long ("+str(timeout)+" seconds)")
        alertcenter(name,1)
    if code>=500:
        print(Fore.RED+ "[ERROR]:"+time_log("date")+" "+time_log("time")+" "+name+": error 5xx internal server error (STATUS CODE:"+code+")")
        logcenter("[WARNING]: "+name+": error 5xx internal server error (STATUS CODE:"+code+")")
        alertcenter(name,2)
    
    
    


