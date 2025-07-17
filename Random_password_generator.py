import random
import string
a = string.ascii_letters
b = string.punctuation
c = string.digits
d = a + b + c
while True:
 k = 0
 while k < 12:
     x = random.choice(d)
     print(x,end="")
     k += 1
 ask = input("\nDo you want to generate another password? (Yes/No): ") 
 if ask.lower().strip() != "yes":
    print("Thanks for using the program,Goodbye")
    break    
