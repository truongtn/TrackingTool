#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append('../..')
from config import *
import httplib, urllib
from urlparse import urlparse
import datetime
def cookietrick(url):
    data=""
    o = urlparse(url)
    
    params = urllib.urlencode(THAMSOS)
    if o.query != "":
        uri = o.path + "?" + o.query
    else:
        uri = o.path
    try:
        conn = httplib.HTTPConnection(o.hostname)
    
        conn.request(METHOD, uri,params,HEADERS)
    
        response = conn.getresponse()
        data = response.read()
    
        if data.find("document.cookie=")!=-1:
            vitri1 = data.find("document.cookie=")+len("document.cookie=")+1
            vitri2 = data.find('"',vitri1+1)
            data=data[vitri1:vitri2]
            return data
    except:
        print ""
        

    return "0"
def httptruong(url):
    time_diff=0
    data=""
    flag=0
    o = urlparse(url)
    
    params = urllib.urlencode(THAMSOS)
    if o.query != "":
        uri = o.path + "?" + o.query
    else:
        uri = o.path
   
    if len(cookietrick(url)):
        flag=1
    
    start = datetime.datetime.now()
  
    conn = httplib.HTTPConnection(o.hostname)
    if HEADER_ENABLE==1 or flag==1:
   
        COOKIE=cookietrick(url)
        
        HEADERS.update({"cookie":COOKIE})

        conn.request(METHOD, uri, params, HEADERS)
    elif HEADER_ENABLE==0 and flag==0:
      
            conn.request(METHOD, uri,params)
    
    
    response = conn.getresponse()
   
    end = datetime.datetime.now()
   
    diff = end - start
    time_diff = diff.seconds
    data = response.read()
    if DEBUG ==1:
        print "Response status: "+str(response.status)
        #if data.find('<META HTTP-EQUIV="Refresh"'):
      
        
    
    return (data,int(response.status),time_diff)
   
        
    
 
    


