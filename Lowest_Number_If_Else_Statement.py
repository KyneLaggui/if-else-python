import colorama
colorama.init()

print(colorama.Fore.YELLOW + "Welcome to KDNL Programming")
print(colorama.Fore.CYAN + "This program displays the lowest number among the three numbers")

User_First_Number= float(input(colorama.Fore.GREEN + "First Number: "))
User_Second_Number= float(input(colorama.Fore.BLUE +  "Second Number: "))
User_Third_Number= float(input(colorama.Fore.MAGENTA + "Third Number: "))

if User_First_Number < User_Second_Number and User_First_Number < User_Third_Number :
    lowest_number = User_First_Number

elif User_Second_Number < User_First_Number and User_Second_Number < User_Third_Number:
    lowest_number = User_Second_Number

elif User_Third_Number < User_First_Number and User_Third_Number < User_Second_Number:
    lowest_number = User_Third_Number

print(colorama.Fore.YELLOW + "The lowest number is",lowest_number)