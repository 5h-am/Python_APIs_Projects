def to_m(quantity):
    dist = quantity
    if dist.endswith("miles"):
        return float(dist[:-5])*1609.34,"m"
    elif dist.endswith("km"):
        return float(dist[:-2])*1000,"m"
    elif dist.endswith("m"):
        return float(dist[:-1]),"m"
    elif dist.endswith("cm"):
        return float(dist[:-2])/100,"m"
    elif dist.endswith("feet"):
        return float(dist[:-4])*0.3048,"m"
    elif dist.endswith("inch"):
        return float(dist[:-4])*0.0254,"m"
    else:
        return None,None
    
def to_g(quantity):
    mass = quantity
    if mass.endswith("kg"):
        return float(mass[:-2])*1000,"g"
    elif mass.endswith("mg"):
        return float(mass[:-2])/1000,"g"
    elif mass.endswith("pound"):
        return float(mass[:-5])*453.59237,"g"
    else :
        return None,None
    
def error():
    print("Write the unit at the end of every quantity.")
    
def get_conv(choices,quantity):
    try:
        quantity = quantity.strip().lower()
        if choices == 1:
            return to_m(quantity) 
        elif choices == 2:
            return to_g(quantity)
    except ValueError:
        return None,None
    
while True:
    print("Welcome")
    print("1.Convert length into metre")
    print("2.Convert weight into gram")

    try:
        convert = int(input("Enter the converter you want to use:"))
        if convert not in range(1,3):
            raise ValueError
    except ValueError:
        print("Error, Enter a valid converter")
        break

    quantity = input("Enter the quantity(e.g., 10miles, 1km, 5kg):").strip()
    new, unit = get_conv(convert,quantity)
    if new is None:
        error()
        continue

    if unit == "m":
        print(f"Converted length: {round(new, 3)}{unit}")
    elif unit == "g":
        print(f"Converted weight: {round(new, 3)}{unit}")

    again= input("Do you want to use other converter?, (Yes/No):")
    if again.lower()!= "yes":
     print("Thanks for using the app, Goodbye")
     break



