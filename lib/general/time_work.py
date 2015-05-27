from time import gmtime,strftime
def time_work(duration):
    minutes = int(strftime("%M ",gmtime()))
    hours = int(strftime("%H ",gmtime()))+7
    
    if (hours*60+minutes) % duration==0:
        result = 1
    else:
        result = 0
    return (result,hours*60+minutes)
  

