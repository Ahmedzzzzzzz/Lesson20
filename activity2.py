import random

import time

def getrandomdate(startDate,endDate):
    print("printing random date bewtween ",startDate, endDate)
    randomgenerator = random.random()
    dateFormat= '%m/%d/%Y'
    starttime= time.mktime(time.strptime(startDate, dateFormat))
    endtime = time.mktime(time.strptime(endDate, dateFormat))
    randomtime = starttime + randomgenerator *(endtime - starttime)
    randomdate = time.strftime(dateFormat, time.localtime(randomtime))
    return randomdate


print ("Random date = ",getrandomdate("1/1/2020", "12/12/2025"))