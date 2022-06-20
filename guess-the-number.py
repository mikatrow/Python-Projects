import random

print("Welcome to the Guess the Number Game!")

print(" ")

print("GUIDE:\n- You have 5 chances to guess the correct number\n- Enter integer numbers only\n- Have patience for code execution(execution speed depends on device specs)")
input("Press ENTER to continue")

print(" ")

generated = random.randint(1, 100)

guess1 = int(input("Guess a number between 1 - 100: "))
if guess1 == generated:
    print("Damn! you gussed in 1st attempt!")
    quit()
elif guess1 > generated:
    print("Too high!")
elif guess1 < generated:
    print("Too low!")
elif guess1 > 100 or guess1 < 0 or guess1 == float:
    print("Bruh, you can only enter integer number between 1 and 100")
else:
    print("Wrong input! try again later")
    quit()

print(" ")

guess2 = int(input("Guess: "))
if guess2 == generated:
    print("Congo! you gussed in 2nd attempt!")
    quit()
elif guess2 > generated:
    print("Too high!")
elif guess2 < generated:
    print("Too low!")
elif guess2 > 100 or guess2 < 0 or guess2 == float:
    print("Bruh, you can only enter integer number between 1 and 100")
else:
    print("Wrong input! try again later")
    quit()

print(" ")

guess3 = int(input("Guess: "))
if guess3 == generated:
    print("Cool! you gussed in 3nd attempt!")
    quit()
elif guess3 > generated:
    print("Too high!")
elif guess3 < generated:
    print("Too low!")
elif guess3 > 100 or guess3 < 0 or guess3 == float:
    print("Bruh, you can only enter integer number between 1 and 100")
else:
    print("Wrong input! try again later")
    quit()

print(" ")

guess4 = int(input("Guess: "))
if guess4 == generated:
    print("Nice! you gussed in 4th attempt!")
    quit()
elif guess4 > generated:
    print("Too high!")
elif guess4 < generated:
    print("Too low!")
elif guess4 > 100 or guess4 < 0 or guess4 == float:
    print("Bruh, you can only enter integer number between 1 and 100")
else:
    print("Wrong input! try again later")
    quit()

print(" ")

guess5 = int(input("Guess: "))
if guess5 == generated:
    print("Good! you gussed in 5th attempt!")
    quit()
elif guess5 > generated:
    print("Shame! you lost the game even after 5 chances")
    print("The correct guess was " + str(generated))
elif guess5 < generated:
    print("Shame! you lost the game even after 5 chances")
    print("The correct guess was " + str(generated))
elif guess5 > 100 or guess5 < 0 or guess5 == float:
    print("Shame! you lost the game even after 5 chances")
    print("The correct guess was " + str(generated))
else:
    print("Shame! you lost the game even after 5 chances")
    print("The correct guess was " + str(generated))
    quit()
