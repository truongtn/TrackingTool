from xacdinhdong import *
import fixpath
from config import *
def checkblacklist(noidung):
    if BLACKLIST_ENABLE == 0:
        return 0
    BLACKLIST=[]
    f = open("blacklist.txt","r")
    a = f.read()
    f.close()
    BLACKLIST = xacdinhdong(a)
    for blacklist in BLACKLIST:
        
        if noidung.find(blacklist)!=-1:
            return 1
    return 0
