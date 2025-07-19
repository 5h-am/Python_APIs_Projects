import requests           
from dotenv import load_dotenv
import os

def api_work():
    load_dotenv()
    api= os.getenv("API_KEY")
    valid_countries = ['in', 'us', 'gb', 'au', 'ca', 'fr', 'de']
    country = input("Enter the country code whose news you want to check(in, us, gb, au, ca, fr, de):").lower().strip()
    if country not in valid_countries:
        print("Invalid country code.")
        return None
    category = input("Enter the news category:").lower().strip()
    q = input("Enter the keyword regarding which you want the news:").lower().strip()

    url = "https://newsapi.org/v2/top-headlines"
    
    query = {
        "country": country,
        "category": category,
    }

    if q :
        query["q"]= q
    headers = {
        "x-api-key": api
    }
    try:
        response = requests.get(url,headers=headers,params=query)
        response.raise_for_status()
    except requests.RequestException:
        print("Error, Can't connect to API")
        return None
    data = response.json()
    if data["status"] == "ok" and len(data["articles"]) > 0:
        return data
    else:
        return None
    
def loop():
    data1 = api_work()
    if data1 is not None:
        no_of_articles = len(data1["articles"])
        i = 0
        while i < no_of_articles:
            article = data1['articles'][i]
            print("\n" + "="*50)
            print(f"Channel: {article['source'].get('name') or 'N/A'}")
            print(f"Author: {article.get('author') or 'N/A'}")
            print(f"Published At: {article.get('publishedAt') or 'N/A'}")
            print(f"Title: {article.get('title', 'N/A')}")
            print(f"Description: {article.get('description') or 'N/A'}")
            print(f"Content: {article.get('content') or 'N/A'}")
            print(f"URL: {article.get('url') or 'N/A'}")
            print("="*50)
            option = input("\nType next to see other news and close to close the app:").strip().lower()

            if option == "close":
                print(f"\nThanks for viewing the news")
                break
            elif option == "next":
                i += 1
                print("\nNext news\n")
            else:
                print("\nError,Enter a valid command\n")
                continue
    else:
        print("Sorry, Can't fetch this news")

while True:
    print("Hello, Welcome to SNews app")
    print("Type these details to see the news\n")
    loop()
    again =input("\nDo you want to see any other news? (yes/no):" )
    if again.lower().strip()!= "yes":
        print("\nThanks for using the app, Have a nice day!")
        break
      
    
        

  





