import requests

def error_check(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None
    return response.json()

def categories():
    url = "https://api.chucknorris.io/jokes/categories"
    return error_check(url)
    
def category_jokes():
    category = categories()
    if category is not None:
        for option in category :
            print(option)
        try:
            choose = input("\nEnter the category whose joke you want:").lower().strip()
            if choose not in category:
                raise ValueError
        except:
            print("Sorry we can't get a joke of this category. Enter a valid category")
            return None
        url = f"https://api.chucknorris.io/jokes/random?category={choose}"
        joke = error_check(url)
        if joke:
            print(f"\nCategory : {joke['categories'][0]}")
            print(f"\nJoke : {joke.get('value') or 'N/A'}\n")
        
while True:
    print("=" * 50)
    print("Welcome to Chuck Norris Jokes".center(100))
    print("=" * 50)
    consent = input("\nDo you want a joke?(Yes/No):").lower().strip()
    print()
    if consent == "yes":
        category_jokes()
    elif consent == "no":
        print("\nThanks for using the app. Have a nice day\n")
        break
    else :
        print("\nError, Enter a valid command\n")
        break











    