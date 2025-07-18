import requests
while True:
    city = input("Enter city:").strip()
    country = input("Enter country:").strip()
    query = f"{city.title()}, {country.title()}"
    url = f"https://nominatim.openstreetmap.org/search?q={query}&format=json"
    headers = {
        "User-Agent":"My app/1.0 (sha@gmail.com)" 
    }
    response = requests.get(url,headers=headers)
    if response.status_code != 200:
        print("Error fetching location data")
        break
    data = response.json()
    if not data:
        print("Error fetching location data")
        continue
    latitude = data[0]["lat"]
    longitude = data[0]["lon"]
    url1 = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=True"
    response1 = requests.get(url1)
    if response1.status_code != 200:
        print("Error, Can't connect to weather api")
        break
    data1 = response1.json()
    if "current_weather" not in data1:
        print("Weather data not available for this location")
        continue
    weather = data1["current_weather"]["temperature"]
    unit = data1["current_weather_units"]["temperature"]
    print(f"The temperature in {city} is {weather}{unit}")
    again =input("Do you want to check weather again ? (yes/no):" )
    if again.strip().lower()!= "yes":
        print("Thanks for using the app, Goodbye!")
        break
      