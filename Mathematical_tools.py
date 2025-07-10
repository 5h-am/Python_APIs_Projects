while True:
 print("Welcome to mathematicals tools")
 print("Select a tool")
 print("1.Calculator")
 print("2.Divisibility checker")
 print("3.Odd even detector")
 print("4.Finding the greatest number")
 features = int(input("What do you want to use (1 / 2 / 3 / 4) : "))
 if features == 3 :
    number = float(input("Enter the number : "))
    if number % 2 == 0 :
       print("It is a even number")
    else : 
       print("It is a odd number")
 elif features == 2 :
    k = int(input("Enter the number whose divisibility you want to check : "))
    l = int(input("Enter the divisor : "))
    if l == 0 : 
       print('Division by zero is not allowed')
    elif k%l == 0 : 
       print(f"{k} is divisible by {l}")
    else : 
       print(f"{k} is not divisible by {l}")
 elif features == 4 :
    x = float(input("Enter 1st number: "))
    y = float(input("Enter 2nd number: "))
    z = float(input("Enter 3rd number: "))
    greatest = max(x , y , z)
    print("The greatest number is ", greatest)
 elif features == 1 :
    num1=float(input("Enter first number:"))
    op=input("Enter operations(+, -, *, /, ^):")
    num2=float(input("Enter second number:"))
    if op== "+":
       result= num1+num2
    elif op== "-":
       result= num1-num2
    elif op== '*':
       result= num1*num2
    elif op== "/":
       if num2==0:
          print("Error:cannot be divided by zero")
          result=None
       else:
          result= num1/num2
    elif op=="^":
       result=num1**num2
    else:
       print("invalid operator")
       result=None 
    if result is not None:
       print("Result:", result)
 again =input("Do you want to use this app again ? (yes/no):" )
 if again.lower()!= "yes":
       print("Thanks for using the app, Goodbye!")
       break
    
