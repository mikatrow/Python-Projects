# Introduction
print("Welcome to the calcuator!")

print(" ") # GAP

print("GUIDE:\n- Enter correct numbers\n- Use numbers only(when asked, else it will jist die -)\n- Have patience for code execution(execution speed depends on device specs)")
input("Press ENTER to continue")

print(" ") # GAP

# Requests for number
num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))

print(" ") #GAP

# Requests for type of operatorto be used
operator = int(input("1 = Add[+]\n2 = Subtract[-]\n3 = Multiplication[*]\n4 = Division[/]\n5 = Modulus[%]\n6 = Exponentiation[**]\n7 = Floor division[//]\nEnter the type of operator to use: "))
if operator >= 8 or operator <= 0:
    print("Wrong input! please try again later") #If wrong number provided
    quit() #Terminate code execution

print(" ") #GAP

# Requests for type of output
type = int(input("1 = Integer[5]\n2 = Float[5.0]\nEnter the the type of result you want: "))
if type >= 3 or type <= 0:
    print("Wrong input! please try again later") #If wrong number provided
    quit() #Terminate code execution

print(" ")

# Addition
if operator == 1:
    int = int(num1 + num2)
    float = float(num1 + num2)
    if type == 1:
        print("Your answer is: " + str(int))
    elif type == 2:
        print("Your answer is: " + str(float))

# Subtraction
elif operator == 2:
    int = int(num1 - num2)
    float = float(num1 - num2)
    if type == 1:
        print("Your answer is: " + str(int))
    elif type == 2:
        print("Your answer is: " + str(float))

# Multiplication
elif operator == 3:
    int = int(num1 * num2)
    float = float(num1 * num2)
    if type == 1:
        print("Your answer is: " + str(int))
    elif type == 2:
        print("Your answer is: " +str(float))

# Division
elif operator == 4:
    int = int(num2 / num2)
    float = float(num1 / num2)
    if type == 1:
        print("Your answer is: " + str(int))
    elif type == 2:
        print("Your answer is: " + str(float))

# Modulus
elif operator == 5:
    int = int(num1 % num2)
    float = float(num1 % num2)
    if type == 1:
        print("Your answer is: " + str(int))
    elif type == 2:
        print("Your answer is: " + str(float))

# Exponentiation
elif operator == 6:
    int = int(num1 ** num2)
    float = float(num1 ** num2)
    if type == 1:
        print("Your answer is: " + str(int))
    elif type == 2:
        print("Your answer is: " + str(float))

# Floor Division
elif operator == 7:
    int = int(num1 // num2)
    float = float(num1 // num2)
    if type == 1:
        print("Your answer is: " + str(int))
    elif type == 2:
        print("Your answer is: " + str(float))
