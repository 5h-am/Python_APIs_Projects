import requests
import os
from dotenv import load_dotenv
import re

load_dotenv() # It handle the errors regarding the response and give the data in the form of a json file
def error_check(url,headers,query=None): 
    try:
        response = requests.get(url,headers=headers,params=query)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None
    return response.json()


# NASA Astronomy picture of the day API related functions


def date():# It gives the astronomy picture according to a specific date
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
    
def count():# It gives a selected number of Astronomy picture of the day
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

def output():# It handles the error and gives option to select what kind of feature you want to use. It also handles the data from count and date
    print("\n1.Get Astronomy Picture of a specific date.")
    print("2.Get specific number of Astronomy Pictures")
    print("3.Go to Main Menu")
    try:
        option = int(input("\nEnter the feature you want to use(1/2/3):"))
        if option not in range(1,4):
            raise ValueError
    except ValueError:
        print("\nError, Enter a valid command")
        return
    if option == 1:
        return date()
    elif option == 2:
        return count()
    elif option == 3:
        return None
    else:
        print("\nError, Enter a valid command")
        return None
    
def choice1(data): # It prints the astronomy picture of the day according to inputs
    if isinstance(data, dict):
        copyright = data.get('copyright')or 'N/A'
        name = copyright.replace("\n","")
        print("-"*100)
        print("-"*100)
        print(f"\nCopyright: {name}")
        print(f"Date: {data.get('date')or 'N/A'}")
        print(f"\nTitle: {data.get('title')or 'N/A'}")
        print(f"\nExplanation: {data.get('explanation')or 'N/A'}")
        print(f"\nHD Image: {data.get('hdurl')or 'N/A'}")
        print(f"Image: {data.get('url')or 'N/A'}")


    elif isinstance(data, list):
        no_of_images = len(data)
        for number, i in enumerate(range(no_of_images),1):
            print("-"*100)
            print(f"Image No: {number}".center(100))
            print("-"*100)
            copyright = data[i].get('copyright')or 'N/A'
            name = copyright.replace("\n","")
            print(f"\nCopyright: {name}")
            print(f"Date: {data[i].get('date')or 'N/A'}")
            print(f"\nTitle: {data[i].get('title')or 'N/A'}")
            print(f"\nExplanation: {data[i].get('explanation')or 'N/A'}")
            print(f"\nHD Image: {data[i].get('hdurl')or 'N/A'}")
            print(f"Image: {data[i].get('url')or 'N/A'}")

    elif data is None:
        return None
    


# NASA Image and Videos Library API related Functions



def page_size(): #It specifies the total number of media 
    while True:
        try:
            page_size = input("Enter the number of media you want(Max-20/Min-1):")
            if page_size not in [str(x) for x in range(1,21)]:
                raise ValueError
        except ValueError:
            print("Error, Enter a number from range 1 to 20")
            continue
        break 
    return page_size
        

def nasa_search_api():# It uses the api to get the data according to the selected parameters
    api = os.getenv("NASA_API_KEY")
    try:
        media_type = input("\nEnter the media type(Image/Video/Audio):").lower().strip()
        if media_type not in ["image","video","audio"]:
            raise ValueError
    except ValueError:
        print("Error, Enter a valid media type")
        return None
    q = input("\nType the keyword you want to search:").strip().lower()
    decription = input("Type the description of your search:").lower()
    images_no = page_size()
    url = "https://images-api.nasa.gov/search"
    headers ={
    "x-api-key": api
    }
    query = {
        "q": q,
        "description": decription,
        "media_type": media_type,
        "page": "1",
        "page_size": images_no
    }
    return error_check(url,headers,query)


def choice2():# It uses the nasa_search_api data to print the desired results
    data = nasa_search_api()
    if data:
        length = len(data['collection']['items'])
        for i in range(length):
            item = data['collection']['items'][i]
            date_created = item['data'][0].get('date_created') or 'N/A'
            title = item['data'][0].get('title') or 'N/A'
            nasa_id = item['data'][0].get('nasa_id') or 'N/A'
            description = item['data'][0].get('description') or 'N/A'
            media_type = item['data'][0].get('media_type') or 'N/A'
            image = item['links'][0].get('href') or 'N/A'
            print("-"*100)
            print(f"\nTitle: {title}")
            print(f"\nCreation Date: {date_created}")
            print(f"\nMedia Type: {media_type}")
            print(f"Nasa Id: {nasa_id}")
            print(f"\nDescription: {description}")
            print(f"\nImage: {image}")
            print("-"*100)
            
   
while True:
    print()
    print("="*100)
    print("Welcome to my NASA App".center(100))
    print("="*100)
    print("\n1.Astronomy Picture of the Day")
    print("2.NASA Image and Video Library")
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
        if choice1(data) is None:
            continue
    elif choice == 2:
            choice2()
    elif choice == 3:
        print("\nThanks for using the app. Have a nice day\n")
        break

    again =input("\nDo you want to use the app again ? (yes/no):" )
    if again.strip().lower()!= "yes":
        print("\nThanks for using the app, Goodbye!\n")
        break





        
    
