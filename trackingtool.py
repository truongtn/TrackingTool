import sys, getopt
from config import *

from lib.alert.sms import *
from lib.alert.email import email
from lib.alert.alertcenter import alertcenter


from lib.ddos.checkddos import *

from lib.general.time_work import *
from lib.general.time_log import *

from  lib.deface.checkdeface import *
from urlparse import urlparse

from lib.khoitaodoc.khoitao import *



from controller.trackingController import *

def main(argv):
   
   try:
 
      opts, args = getopt.getopt(argv,"u:h")
   except getopt.GetoptError:
      print '-h for help'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
      
         print "-u: start"
         sys.exit()
         
      elif opt == '-u':
        trackingController()
      
banner="""






  W  W       wW  Ww oo_      c  c       \\\  ///\\\  ///      ))     
 (O)(O)   wWw(O)(O)/  _)-<   (OO)   /)  ((O)(O))((O)(O)) wWw (Oo)-.  
   ||     (O)_(..) \__ `.  ,'.--.)(o)(O) | \ ||  | \ ||  (O)_ | (_)) 
   | \   .' __)||     `. |/ //_|_\ //\\  ||\\||  ||\\|| .' __)|  .'  
   |  `.(  _) _||_    _| || \___  |(__)| || \ |  || \ |(  _)  )|\\   
  (.-.__))/  (_/\_),-'   |'.    ) /,-. | ||  ||  ||  || `.__)(/  \)  
   `-'  (         (_..--'   `-.' -'   ''(_/  \_)(_/  \_)      )      


                                                                      


"""
banner+="TRACKINGTOOL\nAuthor: truongtn \nHome:http://abc.com\n\n\n\n\n"


                                                             
                                                             


print banner

if __name__ == "__main__":
   main(sys.argv[1:])