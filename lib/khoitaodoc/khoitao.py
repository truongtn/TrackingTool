#!/usr/bin/env python
# -*- coding: utf-8 -*-
from deface.httptruong import *
from ghifile import *
from tachhead import *
from xacdinhdong import *
from urlparse import urlparse
from makemd5 import *
from ngoaile import *
import fixpath
from colorama import init, Fore, Back, Style

from general.time_log import *
def khoitao():
        init()
        f =open("list.txt","r")
        a = f.read()
        
        DONG = xacdinhdong(a)
        for dong in DONG:
                try:
                        o = urlparse(dong)
                        noidung = httptruong(dong)[0]
                
                        noidung = ngoaile(noidung)
              
                        ghifile(o.hostname,makemd5(tachhead(noidung)))
                        
                        print(Fore.GREEN+ "[INFO]:"+time_log("date")+" "+time_log("time")+" "+dong+"'s content has been exported:"+makemd5(tachhead(noidung)))
                        f.close()
                except:
                        print(Fore.YELLOW+ "[WARNING]:"+time_log("date")+" "+time_log("time")+" "+dong+" is not able to created initial content")
                       
       
        return DONG
       


