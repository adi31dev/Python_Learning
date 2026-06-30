# Multiplication table progress
# table_number = int(input("table number = "))
# for i in range(0,11):
#   print(i*table_number)

#New code- Random number 

import random
secret_number  = random.randint(1,1000)
count = 0
while True:
    count += 1
    guess = int(input("Guess the number between 1- 1000: "))
    difference = (guess - secret_number) 
    if difference == 0:
        print(f"YOU WON in {count} guesses!")
        break
    elif difference >= 100:
        print("TOO HIGH!")
    elif 0 < difference < 100:
        print("HIGH")

    elif  -100 < difference < 0:
        print("LOW")
    elif difference <= -100:
        print("TOO LOW")

