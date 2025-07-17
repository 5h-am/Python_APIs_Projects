import random
while True:
 x = random.randint(1,100)
 while True:
  a = input("Guess the number(Just type 'stop' to end,type 'answer' to reveal): ")
  if a.lower() == "stop":
        print("You lost")
        break
  if a.lower() == "answer":
        print("The correct number is",x)
        break
  if not a.isdigit():
        print("Please enter a valid number")
        continue
  elif x == int(a) :
         print("You guessed right")
         break
  elif x < int(a):
        print("Wrong, It is a smaller number than your guess")
  elif x > int(a) :
        print("Wrong, It is a larger number than your guess")
 ask = input("Do you want to play again?(Yes/No):")
 if ask.lower().strip()!="yes":
      print("Thanks for playing")
      break