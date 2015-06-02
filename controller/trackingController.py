import sys
import fixpath
from colorama import init, Fore, Back, Style
sys.path.append('../')
from config import *
from log.logcenter import *


from alert.alertcenter import *

from ddos.checkddos import *

from deface.checkdeface import *

from khoitaodoc.khoitao import *

from general.time_log import *
from general.time_work import *
def trackingController():
    init()
    
    print(Fore.YELLOW+ "[START]: Preparing for the initial step...\n")
    logcenter("[START]: Preparing for the initial step...")
    configinfo = " TIME OUT= "+str(TIME_OUT)+" DURATION= "+str(DURATION)+" RETRY= "+str(RETRY)+" ALERT METHOD= "+str(ALERT_METHOD)
    logcenter(configinfo)
    minutesall = 0
    
    DONG = khoitao()
   
    
    
    
    print(Fore.GREEN+ "[INFO]: The initial step is done, process is ready")
    logcenter("[INFO]: The initial step is done, the process is ready")
    print(Fore.GREEN+ "[INFO]: Tracking...")
    logcenter("[INFO]: Tracking...")
    while(1):
        if minutesall!=time_work(DURATION)[1]:
            if time_work(DURATION)[0]==1:
                minutesall = time_work(DURATION)[1]
                
                for dong in DONG:
                
                    a = checkdeface(dong)
                   
                    try:
                        checkddos(dong,a[1],a[2])
                    except:
                        None
                


