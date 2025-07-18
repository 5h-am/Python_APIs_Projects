import winsound
import time
import datetime
import os

def get_value(prompt,min,max):
    while True:
        try:
            value = int(input(prompt))
            if not (max >= value >= min):
                raise ValueError
            return value
        except ValueError:
            print(f"Enter a valid number from {min} to {max}")


def stop():
    while True:
        button = input("Type stop to stop the alarm:").lower().strip()
        if button == "stop":
            return
        else:
            print("Wrong key. Type stop")
    

def play(audio_file):
    if os.path.exists(audio_file):
        print("Times up. Playing the alarm")
        winsound.PlaySound(audio_file ,winsound.SND_FILENAME|winsound.SND_ASYNC|winsound.SND_LOOP)
    else:
        print(f"{audio_file} not found")


def start_stopwatch():
    t = time.time()
    return t

def stop_stopwatch():
    t = time.time()
    return t

def error():
    print("Error,Enter a valid command")

while True:
    print("\n===== Welcome to Clock =====")
    print("1.Stopwatch")
    print("2.Timer")
    print("3.Alarm clock")
    try:
        feature = int(input("What do you want to use?(1/2/3):"))
        if feature not in range (1,4):
            raise ValueError
    except ValueError:
        error()
        continue

    if feature == 1:
        print("\n--- Stopwatch ---")
        try:
            strt = int(input("Type 1 to start:"))
            if strt != 1:
                raise ValueError
        except ValueError:
            error()
            continue
        if strt == 1:
         a = start_stopwatch()    
         print(f"Stopwatch started...Waiting for stop")
        try:
            stp = int(input("Type 2 to stop:"))
            if stp != 2:
                raise ValueError
        except ValueError:
            error()
            continue
        if stp == 2:
            b = stop_stopwatch()
            winsound.Beep(1000,500)
            print(f"Time:{round((b-a),3)}")
    
    elif feature == 2:
        print("--- Timer---")
        try:
            b = float(input("Enter time:"))
        except ValueError:
            print("Error,Enter the value in seconds(e.g. 45, 65, 100)")
            continue
        print(f"Timer set for {b} seconds")
        time.sleep(b)
        winsound.Beep(1000,500)
        print("Times up")


    elif feature == 3:
        print("--- Alarm Clock ---")
        option = input("Do you want to set an alarm? (Yes/No):").strip().lower()
        if option != "yes":
            print("Alarm not set")
            continue

        print("\nSet date")
        year = get_value("Enter year (e.g. 2025):",2025,2100)
        month = get_value("Enter month(1-12):",1,12)
        day = get_value("Enter day(1-31):",1,31)

        print("\nSet time")
        hour = get_value("Enter hour(0-23):",0,23)
        minutes = get_value("Enter minutes(0-59):",0,59)
        print("Setting Alarm")

        try:
            dt = datetime.datetime(year,month,day,hour,minutes)
        except ValueError as e:
            print(f"Enter valid date/time:{e}")
            continue

        ts_of_dt = dt.timestamp()
        dn = datetime.datetime.now()
        ts_of_dn = dn.timestamp()
        diff  = ts_of_dt-ts_of_dn
        audio_file = "Real-clock\ile_example_WAV_2MG_copy.wav"
        if diff <= 0:
            print("Time has already passed. Enter a future time")
            continue
        winsound.Beep(1000,500)
        print(f"Alarm set for {dt} .Waiting")
        time.sleep(diff)
        play(audio_file)
        stop()
        winsound.PlaySound(None,winsound.SND_PURGE)

    again= input("Do you want to use other features?, (Yes/No):")
    if again.lower()!= "yes":
        print("Thanks for using the clock, Goodbye")
        break






