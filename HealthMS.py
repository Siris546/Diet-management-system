names = ['Rohan','Harry','Hamaad']

def getdate():
    import datetime
    return datetime.datetime.now()

def lock():
    print("Who do you want to lock for ? ")
    print("1. Rohan")
    print("2. Harry")  
    print("3. Hamaad")
    n=int(input())
    print("Do you want to lock food or exercise?")
    print("1. food")
    print("2. exercise")
    choice = int(input("Enter your choice: "))
    if choice == 1 and n==1:
        food1 = input("Enter the food Rohan ate: ")
        with open("Rohanfood.txt", "a") as f1:
            f1.write("Rohan ate at " + str(getdate()) + " : " + food1+"\n")
        print("Successfully written")
    elif choice == 1 and n==2:
        food2 = input("Enter the food Harry ate: ")
        with open("Harryfood.txt", "a") as f2:
            f2.write("Harry ate at " + str(getdate()) + " : " + food2+"\n")
        print("Successfully written")
    elif choice == 1 and n==3:
        food3 = input("Enter the food Hamaad ate: ")
        with open("Hamaadfood.txt", "a") as f3:
            f3.write("Hamaad ate at " + str(getdate()) + " : " + food3+"\n")
        print("Successfully written")
    elif choice ==2 and n==1:
        exercise1 = input("Enter the exercise Rohan did: ")
        with open("Rohanexercise.txt", "a") as fe4:
            fe4.write("Rohan did at " + str(getdate()) + " : " + exercise1+"\n")
        print("Successfully written")
    elif choice ==2 and n==2:
        exercise2 = input("Enter the exercise Harry did: ")
        with open("Harryexercise.txt", "a") as fe5:
            fe5.write("Harry did at " + str(getdate()) + " : " + exercise2+"\n")
        print("Successfully written")
    elif choice ==2 and n==3:
        exercise3 = input("Enter the exercise Hamaad did: ")
        with open("Hamaadexercise.txt", "a") as fe6:
            fe6.write("Hamaad did at " + str(getdate()) + " : " + exercise3+"\n")
        print("Successfully written")
    else:
        print("Invalid Input!!☠️💀")

def retrieve():
    print("Whoose data do you want to retrieve ? ")
    print("1. Rohan")
    print("2. Harry")  
    print("3. Hamaad")
    n=int(input())
    if n == 1:
        with open("Rohanfood.txt") as f1:
            print(f1.read())
        with open("Rohanexercise.txt") as fe4:
            print(fe4.read())
    elif n == 2:
        with open("Harryfood.txt") as f2:
            print(f2.read())
        with open("Harryexercise.txt") as fe5:
            print(fe5.read())
    elif n == 3:
        with open("Hamaadfood.txt") as f3:
            print(f3.read())
        with open("Hamaadexercise.txt") as fe6:
            print(fe6.read())
    else:
        print("Invalid Input!!☠️💀")
while(True):
    print("Do you want to lock or retrieve ?")
    print("1. Lock")
    print("2. Retrieve")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        lock()
    elif choice == 2:
        retrieve()
    else:
        print("Invalid Input!!☠️💀")
    print("Do you want to continue ?")
    print("1. Yes")
    print("2. No")
    continuation = int(input("Enter your choice: "))
    if continuation == 1:
        continue
    elif continuation == 2:
        break
    else:
        print("Invalid Input!!☠️💀")
