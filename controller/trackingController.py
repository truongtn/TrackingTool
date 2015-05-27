import sys
sys.path.append('../')
from config import *


from alert.alertcenter import *

from ddos.checkddos import *

from deface.checkdeface import *

from khoitaodoc.khoitao import *

from general.time_log import *
from general.time_work import *
def trackingController():
    

    minutesall = 0
    DONG=khoitao()
    
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
                


