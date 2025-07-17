import time
def start():
    t = time.time()
    return t
def stop():
    t = time.time()
    return t
def error():
    print("Error,Enter a valid command")
while True:
    print("Welcome")
    print("1.Stopwatch")
    print("2.Timer")
    try:
        feature = int(input("What do you want to use?(1/2):"))
        if feature not in range (1,3):
            raise ValueError
    except ValueError:
        error()
        break

    if feature == 1:
        try:
            strt = int(input("Type 1 to start:"))
            if strt != 1:
                raise ValueError
        except ValueError:
            error()
            break
        if strt == 1:
         a = start()    
         print(f"Stopwatch started...Waiting for stop")
        try:
            stp = int(input("Type 2 to stop:"))
            if stp != 2:
                raise ValueError
        except ValueError:
            error()
            break
        if stp == 2:
            b = stop()
            print(round((b-a),3))
    
    elif feature == 2:
        b = float(input("Enter time:"))
        print(f"Timer set for {b} seconds")
        time.sleep(b)
        print("Times up")
                
    again= input("Do you want to use other features?, (Yes/No):")
    if again.lower()!= "yes":
        print("Thanks for using the clock, Goodbye")
        break

