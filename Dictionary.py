import requests
import playsound
import tempfile

def api_work(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        print("\nError, Can't get definition of your word. Either you typed a wrong word or we can't find that word.")
        return None
    data = response.json() 
    return data
  
def audio(data, word):
    phonetics = data[0].get('phonetics',[])
    if phonetics:    
        print(f"Phonetic: {data[0]['phonetics'][0].get('text') or 'N/A'}")
        audio_url = data[0]['phonetics'][0]['audio']
        try:
            audio_response = requests.get(audio_url)
            with tempfile.NamedTemporaryFile(delete=True, suffix=".mp3")as f:
                f.write(audio_response.content)
                f.flush()
                print(f"Playing {word}")
                playsound.playsound(f.name)
        except Exception as e:
            print(f"Audio error: {e}")
                    
    else:
        print("No phonetics available for this word")


def meaning(data):
    meanings = data[0].get('meanings',[])
    if meanings:
        result = []
        no_of_partofspeech = len(data[0]['meanings'])
        for i, k in enumerate(range (no_of_partofspeech), 1):
            part_of_speech = data[0]['meanings'][k]['partOfSpeech']
            result.append(part_of_speech)
            print(f"{i}.Part of speech: {part_of_speech}")
            
        select = input("\nEnter the part of speech to get definition for that part of speech:").lower().strip()
        if select not in result:
            print("\nError, Enter a valid command")
            return 
        else:
            x = result.index(select)
            definition = data[0]['meanings'][x]['definitions'][0].get('definition') or 'N/A'
            example = data[0]['meanings'][x]['definitions'][0].get('example') or 'N/A'
            print()
            print(f"Definition: {definition}")
            print(f"Example: {example}")
    else:
        print("No definitions available")

def output(choice,data,word):
    data = api_work(word)
    if data is not None:
        if choice == 1:
            return audio(data,word)
        elif choice == 2:
            return meaning(data)
        else:
            print("Error,Enter a valid command")
            return
        
        
while True:
    print(f"{'='*30}Welcome to Dictionary{'='*30}")
    print("1.Phonetic and hear the word")
    print("2.Get the definition of the word according to part of speech")

    word = input("\nEnter the word:").lower().strip()
    feature = int(input("\nEnter the feature you want to use:"))
    data = api_work(word)
    
    if data:
        print("="*50)
        print(f"\nWord: {word}")
        output(feature,data,word)

    again= input("Do you want to search other words?, (Yes/No):")
    if again.lower()!= "yes":
        print("Thanks for using the dictionary, Goodbye")
        break


    

    

    
