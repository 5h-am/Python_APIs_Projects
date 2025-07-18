import winsound
import datetime
import time

print("Welcome")
try:
    option = input("Do you want to set an alarm? (Yes/No):").strip().lower()
    if option != "yes" and option != "no":
        raise  ValueError
except ValueError:
    print("Error, Type a valid command")

if option == "yes":
    print("Set date")
    year = int(input("Enter year:"))
    month = int(input("Enter month:"))
    day = int(input("Enter day:"))
    
    print("Set time")
    hour = int(input("Enter hours:"))
    minute = int(input("Enter minutes:"))
    print("Alarm set. Waiting")

    dt = datetime.datetime(year,month,day,hour,minute)
    ts_of_dt = dt.timestamp()
    dn = datetime.datetime.now()
    ts_of_dn = dn.timestamp()
    diff  = ts_of_dt-ts_of_dn
    if diff > 0:
        time.sleep(diff)
        winsound.PlaySound("Alarm_clock\ile_example_WAV_2MG copy.wav" ,winsound.SND_FILENAME)
    else:
        print("Error,Enter a correct date")
