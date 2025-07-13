while True:
    print("Temperature Converter")
    print("1.Convert to celsius")
    print("2.Convert to fahrenheit")
    print("3.Convert to kelvin")
    try:
        convert = int(input("Enter the converter you want to use(1/2/3):"))
        if convert not in range(1,4):
            raise ValueError
    except ValueError:
        print("Error,Invalid converter")
        break
    temp = input("Enter the temperature(eg. 100C, 50F, 273K):").strip()
    temp = temp.upper()
    def error():
        print("Invalid Temperature Format. Use C , F , K at the end")

    if convert == 1:
        if temp.endswith("K") :
            temp1 = temp.removesuffix("K")
            celsius  = float(temp1) - 273.15
            print(round(celsius,2),"C")

        elif temp.endswith("F") :
            temp1 = temp.removesuffix("F")
            celsius  = (5/9)*(float(temp1) - 32)
            print(round(celsius,2),"C") 
        else :
            error()

    elif convert == 2:
        if temp.endswith("C") :
            temp1 = temp.removesuffix("C")
            fahrenheit  = (float(temp1)*(9/5))+32
            print(round(fahrenheit,2),"F")
    
        elif temp.endswith("K") :
            temp1 = temp.removesuffix("K")
            fahrenheit  = 32+(float(temp1)-273.15)*(9/5)
            print(round(fahrenheit,2),"F")
        else :
            error()
    
    elif convert == 3:
        if temp.endswith("C") :
            temp1 = temp.removesuffix("C")
            kelvin  = float(temp1) + 273.15
            print(round(kelvin,2),"K")
    
        elif temp.endswith("F") :
            temp1 = temp.removesuffix("F")
            kelvin  = 273.15+(float(temp1)-32)*(5/9)
            print(round(kelvin,2),"K")
        else :
            error() 

    again= input("Do you want to convert any other temperature?, (Yes/No):")
    if again.lower()!= "yes":
        print("Thanks for using the app, Goodbye")
        break
