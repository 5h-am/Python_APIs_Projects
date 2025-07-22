import requests

def api_work(IP):
    url = f"http://ip-api.com/json/{IP}"
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        print("Error, Can't connect to api")
        return None

    data = response.json()
    if data.get("status") != "success" :
        print("\nInvalid ip address or location not found ")
        return None
    return data

def output(data):
    return data.items()
    
while True:
    print("="*100)
    print("Welcome to Location Checker".center(100))
    print("="*100)
    IP = input("\nEnter the ip address:").strip()
    data = api_work(IP)
    if data:
        print("\nLocation Details:\n")
        for item, value in output(data):
            print(f"{item.capitalize()} : {value}")

        with open("location.txt","a")as f:
            f.write("="*100)
            f.write("\n")
            f.write(f"{'IP Address: ' + IP}".center(100))
            f.write("\n")
            f.write("="*100 + "\n")
            for item, value in output(data):
                f.write(f"\n{item.capitalize()} : {value}")
            f.write("\n\n")

    again= input("\nDo you want to find any other location?, (Yes/No):")
    if again.lower()!= "yes":
        print("\nThanks for using the app, Goodbye\n")
        break

        
       
        
            
