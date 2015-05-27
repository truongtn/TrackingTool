from sms import sms
from email import email

import sys

from config import *

def alertcenter(url,errcode):
    if ALERT_METHOD == "sms":
        sms(url,errcode)
    elif ALERT_METHOD == "email":
        email(url,errcode)
  

