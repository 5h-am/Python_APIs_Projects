import requests
import os
from dotenv import load_dotenv
import re

load_dotenv()
def error_check(url,headers,query=None):
    try:
        response = requests.get(url,headers=headers,params=query)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None
    return response.json()

def date():
    api = os.getenv("NASA_API_KEY")

    url = "https://api.nasa.gov/planetary/apod"

    headers ={
    "x-api-key": api
    }
    date = input("\nEnter date to get Astronomy Picture of that Date(YYYY-MM-DD)or(You can just leave it to get today's picture):")
    if date :
        if re.match(r"\d{4}-\d{2}-\d{2}", date):
            query = {
                "date": date
            }
            return error_check(url,headers,query)
        else:
            print("\nError, Enter a valid date format(YYYY-MM-DD)")
            return None
    else:
        return error_check(url,headers)
    
def count():
    api = os.getenv("NASA_API_KEY")

    url = "https://api.nasa.gov/planetary/apod"

    headers ={
    "x-api-key": api
    }
    try:
        count = int(input("\nEnter the number of pictures you want:"))
    except ValueError:
        print("\nError, Enter a valid number")
        return None
    query = {
        "count": count
     }
    return error_check(url,headers,query)

def output():
    print("\n1.Get Astronomy Picture of a specific date.")
    print("2.Get specific number of Astronomy Pictures")
    try:
        option = int(input("\nEnter the feature you want to use(1/2):"))
        if option not in range(1,3):
            raise ValueError
    except ValueError:
        print("\nError, Enter a valid command")
        return
    if option == 1:
        return date()
    elif option == 2:
        return count()
    else:
        print("\nError, Enter a valid command")
        return None
    
   
while True:
    print()
    print("="*100)
    print("Welcome to my NASA App".center(100))
    print("="*100)
    print("\n1.Astronomy Picture of the Day")
    print("2.Future API")
    print("3.Close the program")

    try:
        choice = int(input("\nWhat do you want to do(1/2/3):"))
        if choice not in range(1,4):
            raise ValueError
    except ValueError:
        print("Error, Enter a valid command")
        continue

    if choice == 1:
        data = output()
        if isinstance(data, dict):
            copyright = data.get('copyright')or 'N/A'
            name = copyright.replace("\n","")
            print(f"\nCopyright: {name}")
            print(f"Date: {data.get('date')or 'N/A'}")
            print(f"\nTitle: {data.get('title')or 'N/A'}")
            print(f"\nExplanation: {data.get('explanation')or 'N/A'}")
            print(f"\nHD Image: {data.get('hdurl')or 'N/A'}")
            print(f"Image: {data.get('url')or 'N/A'}")

        elif isinstance(data, list):
            no_of_images = len(data)
            for number, i in enumerate(range(no_of_images),1):
                print(f"\nImage No: {number}")
                copyright = data[i].get('copyright')or 'N/A'
                name = copyright.replace("\n","")
                print(f"\nCopyright: {name}")
                print(f"Date: {data[i].get('date')or 'N/A'}")
                print(f"\nTitle: {data[i].get('title')or 'N/A'}")
                print(f"\nExplanation: {data[i].get('explanation')or 'N/A'}")
                print(f"\nHD Image: {data[i].get('hdurl')or 'N/A'}")
                print(f"Image: {data[i].get('url')or 'N/A'}")
                print("-"*100)

        elif data is None:
            continue
    elif choice == 3:
        print("\nThanks for using the app. Have a nice day\n")
        break

    again =input("\nDo you want to use the app again ? (yes/no):" )
    if again.strip().lower()!= "yes":
        print("\nThanks for using the app, Goodbye!\n")
        break





        
    
