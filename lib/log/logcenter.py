from fixpath import *
from general.time_log import *
def logcenter(noidung):
    f = open("log.txt","a")
    f.write(time_log("time")+noidung+"\n")
    f.close()
