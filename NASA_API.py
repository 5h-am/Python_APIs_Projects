import requests
import os
import json
from dotenv import load_dotenv

# load_dotenv()
# api = os.getenv("NASA_API_KEY")

# url = "https://api.nasa.gov/planetary/apod"

# headers ={
#     "x-api-key": api
# }
# response = requests.get(url, headers=headers)
# data = response.json()
# print(json.dumps(data, indent=4))


def api_work():
    load_dotenv()
    api = os.getenv("NASA_API_KEY")

    url = "https://api.nasa.gov/planetary/apod"

    headers ={
    "x-api-key": api
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error: {e}")
        return
    return response.json()

while True:
    print("="*100)
    print("Welcome to my NASA App".center(100))
    print("="*100)
    choice = int(input("\nWhat do you want to do:"))
    if choice == 1:
        data = api_work()
        copyright = data.get('copyright')or 'N/A'
        name = copyright.replace("\n","")
        print(f"\nCopyright: {name}")
        print(f"Date: {data.get('date')or 'N/A'}")
        print(f"\nTitle: {data.get('title')or 'N/A'}")
        print(f"\nExplanation: {data.get('explanation')or 'N/A'}")
        print(f"\nHD Image: {data.get('hdurl')or 'N/A'}")
        print(f"Image: {data.get('url')or 'N/A'}")

        
    
