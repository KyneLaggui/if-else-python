Input_Grade_of_User = float(input("Input Grade: "))


def Grade_User_(User_Grade):

    if float(User_Grade) >=97:
        print("Your Grade/Mark is 1.00")
        print("You're Excellent")

    elif 94<= float(User_Grade) < 96:
        print("Your Grade/Mark is 1.25")
        print("You're Excellent")

    elif 91<= float(User_Grade) < 93:
        print("Your Grade/Mark is 1.5")
        print("You're Very Good")
    
    elif 88<= float(User_Grade) < 90:
        print("Your Grade/Mark is 1.75")
        print("You're Very Good")

    elif 83<= float(User_Grade) < 85:
        print("Your Grade/Mark is 2.0")
        print("You're Good")

    elif 82<= float(User_Grade) < 84:
        print("Your Grade/Mark is 2.25")
        print("You're Good")

    elif 79<= float(User_Grade) < 81:
        print("Your Grade/Mark is 2.5")
        print("You're Satisfactory")

    elif 76<= float(User_Grade) < 78:
        print("Your Grade/Mark is 2.75")
        print("You're Satisfactory")
    
    elif 75== float(User_Grade) :
        print("Your Grade/Mark is 3.00")
        print("You're Passing")

    elif 65 <= float(User_Grade) < 74:
        print("Your Grade/Mark is 5.00")
        print("Sorry you failed")
    elif 64 <= float(User_Grade):

        def User_Choices(): 
             print("[1] Incomplete")
             print("[2] Withdrawn")
             print("[3] Dropped")

        User_Choices()       
        User_Choices_F= int(input("Are you: "))

        if User_Choices_F ==1:
            print("You are incomplete, you need to pass your requirements")
        elif User_Choices_F ==2:
            print("You are withdrawn, you're no longer part of PUP ")
        elif User_Choices_F ==3:
            print("You are dropped, you're no longer part of PUP ")

Grade_User_(Input_Grade_of_User)
