# Introduction
print("Welcome to the Maths Quiz!")

print(" ") #GAP

print("Guide:\n- Answer questions correctly\n- Enter numbers only\n- Have patience for code execution(execution speed depends on device specs)")

print(" ") #GAP

input("Press ENTER to continue")

# Fixed Variables
score = 0
questions = 5

print(" ") #GAP

# Question 1
ans1 = int(input("Question 1: What is 3 + 6\nYour answer: "))
if ans1 == 9:
    print("Correct!")
    score += 1
else:
    print("Wrong answer!")

print(" ") #GAP

# Question 2
ans2 = int(input("Question 2: What is 5 x 7?\nYour answer: "))
if ans2 == 35:
    print("Correct!")
    score +=1
else:
    print("Wrong answer!")

print(" ") #GAP

# Question 3
ans3 = int(input("Question 3: What is 34-13?\nYour answer: "))
if ans3 == 21:
    print("Correct!")
    score +=1
else:
    print("Wrong answer!")

print(" ") #GAP

# Question 4
ans4 = int(input("Question 4: What is 90/3?\nYour answer: "))
if ans4 == 30:
    print("Correct!")
    score +=1
else:
    print("Wrong answer!")

print(" ") #GAP

# Question 5
ans5 = int(input("Question 5: What is 5 x (10-6)?\nYour answer: "))
if ans5 == 20:
    print("Correct!")
    score +=1
else:
    print("Wrong answer!")

print(" ") #GAP

# Final Score
print("You attempted " + str(score) + " questions correctly")
final = (score/questions) * 100
print("You earned " + str(final) + " marks")
