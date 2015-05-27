from time import gmtime,strftime
def time_log(option):
    minute = int(strftime("%M ",gmtime()))
    hour = (int(strftime("%H ",gmtime()))+7)%24
    
    second = int(strftime("%S ",gmtime()))
    day = int(strftime("%d ",gmtime()))
    month = int(strftime("%m ",gmtime()))
    year = int("20"+str(strftime("%y ",gmtime())))
    weekday = str(strftime("%a ",gmtime()))
    
    if option=="speparate":
        return(second,minute,hour,weekday,day,month,year)
    elif option =="date":
        if month<10:
            month = "0"+str(month)
        if day<10:
            day = "0"+str(day)
        return weekday.replace(" ","")+"-"+str(day)+"-"+str(month)+"-"+str(year)
    elif option=="time":
        if second<10:
            second = "0"+str(second)
        if minute<10:
            minute = "0"+str(minute)
        if hour<10:
            hour = "0"+str(hour)
        return str(hour)+":"+str(minute)+":"+str(second)

    
  

