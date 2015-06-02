# -*- coding: utf-8 -*-
from khoitaodoc.ngoaile import *
from httptruong import *
from checkblacklist import *
from xacdinhdong import *
from urlparse import urlparse
from makemd5 import *
from tachhead import *
import fixpath
from colorama import init, Fore, Back, Style
import sys

from general.time_log import *

from config import *
from log.logcenter import *

from  alert.alertcenter import *

def checkdeface(url):
        init()
        try:
                try:
                        if retry[url]:
                                pass
                except:
                        w = {url:0}
                        retry.update(w)
                o = urlparse(url)
                dump = httptruong(url)
                noidung = dump[0]
                noidung = ngoaile(noidung)
                if tachhead(noidung)=="":
                        b1="0"
                else:
                        b1=tachhead(noidung)
                        
                        noidung = makemd5(b1)
                       
                f=open("base/"+o.hostname+".txt","r")
                noidung1 = f.read()
                if noidung == noidung1 and checkblacklist(dump[0])==0:
                        None
                else:
                        retry_time = retry[url]
                        retry_time +=1
                        w = {url:retry_time}
                        retry.update(w)
                        
                        print(Fore.YELLOW+"[WARNING]:"+time_log("date")+" "+time_log("time")+" "+url+" seem to be deface(#"+str(retry[url])+")")
                        logcenter("[WARNING]:"+" "+url+" seem to be deface(#"+str(retry[url])+")")
                        if retry[url] >= RETRY:
                                print(Fore.RED+"[ERROR]:"+time_log("date")+" "+time_log("time")+" "+url+" has been defaced")
                                logcenter("[ERROR]:"+" "+url+" has been defaced")
                                alertcenter(url,4)
                                w = {url:0}
                                retry.update(w)
                return (dump[0],dump[1],dump[2])
        except:       
                print(Fore.RED+ "[ERROR]:"+time_log("date")+" "+time_log("time")+" "+url+" is temporarily unavailabe")
                logcenter("[ERROR]: "+url+" is temporarily unavailabe")
                alertcenter(url,3)

