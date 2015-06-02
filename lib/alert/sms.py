import sys
from config import *
import httplib, urllib
from urlparse import urlparse
import fixpath
from log.logcenter import *

def sms(url,errcode):
   
    notice = []
    notice.append("none")
    notice.append("server response time is too long")
    notice.append("error 5xx internal server error")
    notice.append("is temporarily unavailabe")
    notice.append("has been defaced")
    body = url +" "+notice[errcode]
    THAMSOS=""
    url="https://api.twilio.com/2010-04-01/Accounts/ACd1a126f172bd9ea2fc4db24772740458/Messages.json"
    time_diff=0
    data=""
    flag=0
    o = urlparse(url)
    
    params = urllib.urlencode({'From':'+19732415890','To':TO,'Body':body})

    if o.query != "":
        uri = o.path + "?" + o.query
    else:
        uri = o.path
   

    

  
    conn = httplib.HTTPSConnection(o.hostname)

    

    conn.request("POST", uri,params,{"Authorization": "Basic QUNkMWExMjZmMTcyYmQ5ZWEyZmM0ZGIyNDc3Mjc0MDQ1ODowMzFhODUxNDZjMGFlZjQ0ODZkMjg1OGIwYjRlNzk1Yg==","Content-Type": "application/x-www-form-urlencoded"})
    response = conn.getresponse()
   
    data = response.read()  
    

    print "[INFO]: a SMS alert has been sent"
    logcenter("[INFO]: a SMS alert has been sent to "+TO)

   
   
    

    

    
   
        
    
 
    


