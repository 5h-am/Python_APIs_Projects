while True:
    a = int(input("1.View task/2.Add task/3.Replace task/4.Delete task:"))
    open("To do List.txt","a").close()

    if a == 1:
        with open("To Do List.txt","r") as f:
            data = f.read()
            print(data)

    if a == 2:
        add = input("Add task:").strip()
        with open("To Do List.txt","a") as f:
            f.write(add+"\n")

    if a == 3:
        replace = int(input("Enter the line no:"))
        task = input("Enter the new task:")
        with open("To Do List.txt","r+") as f:
            data1 = f.readlines()
            if replace > 0 and replace <= len(data1):
                data1[replace-1] = task+"\n"
                print("Task replaced")
            else:
                print("Invalid line no")
        with open("To Do List.txt","w") as f:
            f.writelines(data1)
      
    if a == 4:
        delete = int(input("Enter the line no:"))
        with open("To Do List.txt","r") as f:
            data2 = f.readlines()
            if delete > 0 and delete <= len(data2):
                del data2[delete-1]
                print("Task deleted")
            else:
                print("Invalid line no")
        with open("To Do List.txt","w") as f:
            f.writelines(data2)
    again =input("Do you want to use any other feature ? (yes/no):" )
    if again.lower()!= "yes":
        print("Thanks for using the app, Goodbye!")
        break
      

      
      
   

         
            

      
   

