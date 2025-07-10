import random
import string
a = string.ascii_letters
b = string.punctuation
c = string.digits
characters = a + b + c
while True:
 pass_len = 12
 password = ""
 for i in range(pass_len):
   password += random.choice(characters)
 print("The generated password:",password) 
 ask = input("Do you want to generate another password? (Yes/No): ") 
 if ask.lower().strip() != "yes":
    print("Thanks for using the program,Goodbye")
    break    