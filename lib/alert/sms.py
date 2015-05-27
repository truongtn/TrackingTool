import sys
from config import *
import httplib, urllib
from urlparse import urlparse


def sms(url,errcode):
    print "SFs"
    notice = []
    notice.append("none")
    notice.append("time out")
    notice.append("500")
    notice.append("dut han")
    notice.append("deface")
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
    

    print "[INFO]: SMS alert has been sent"

   
   
    

    

    
   
        
    
 
    


