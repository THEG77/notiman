import psutil,requests,time
from discord import Webhook, RequestsWebhookAdapter


  
# function returning time in hh:mm:ss
def convertTime(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)
  
# returns a tuple
def calculate():
    battery = psutil.sensors_battery()
    
    try:
        if battery.percent < 10  and battery.power_plugged == True:
            webhook = Webhook.from_url("YOUR WEBHOOK HERE", adapter=RequestsWebhookAdapter())
            
            timetosend = convertTime(battery.secsleft)
            powerstatustosend = battery.power_plugged
            percenttosend = battery.percent
            percentstring = ("Battery percentage : " + str(percenttosend))
            statusstring = "Power plugged in : " + str(powerstatustosend)
            timestring = "Battery left : " + str(timetosend)
            print(percentstring)
            print(statusstring)
            print(timestring)
            allinonestring = percentstring , "                                                  " , statusstring , "                                                    " , timestring, "                                                    " , "BATTERY LOW"
            webhook.send(allinonestring)
            
            print("Sent Notification!")
        else:
            timetosend = convertTime(battery.secsleft)
            powerstatustosend = battery.power_plugged
            percenttosend = battery.percent
            percentstring = ("Battery percentage : " + str(percenttosend))
            statusstring = "Power plugged in : " + str(powerstatustosend)
            timestring = "Battery left : " + str(timetosend)
            print(percentstring,statusstring,timestring)
            print("Did Not Send!\n =========================================================================== \n")    
    except Exception as e:
        print(e)
while True:
    calculate()
    print("CHECKING AGAIN IN 5 MINS")
    time.sleep(300)
