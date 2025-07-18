import requests
def exchange(base,to,amount):
    url = f"https://api.frankfurter.app/latest"
    rate = {
        "from":base,
        "to":to
        }
    try:
        response = requests.get(url,params=rate)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        print("Error, Can't connect to API")
        return None
    data = response.json()
    if not data or to not in data["rates"]:
        print("Error, Exchange rate is not available for this currency")
        return None
    rate = data["rates"][to]
    exchanged_money = rate*amount
    return round(exchanged_money, 3)

while True:
    print("Welcome to Currency Conversion.")
    original = input("Enter the currency you want to exchange(e.g. USD, INR, EUR):").upper().strip()
    exchanged = input("Enter the currency you want(e.g. USD, INR, EUR ):").upper().strip()
    try:
        amount = float(input("Enter the amount:"))
    except ValueError:
        print("Enter a valid amount")
        continue

    result = exchange(original,exchanged,amount)
    if result is not None:
        print(f"{amount} {original} = {result} {exchanged}")

    again =input("Do you want to convert any other currency? (yes/no):" )
    if again.lower().strip()!= "yes":
        print("Thanks for using the app, Goodbye!")
        break
      


