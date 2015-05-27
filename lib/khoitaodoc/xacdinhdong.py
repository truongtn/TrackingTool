import sys
sys.path.append('../..')
from config import *

def xacdinhdong(noidung):
    DONG=[]
    noidung=noidung+"\n"
    string=""
    
    for i in range(0,len(noidung)):
       
        if( (noidung[i]!="\n") ):
            string = string + noidung[i]
        
        else:
            DONG.append(string)
            string = ""
    return DONG
    
