import random
secret_number = random.randint(1,1000)

count = 0
hints = [
    "HINT: It is a whole number 😇",
    "HINT: It is not a decimal 😇",
    "HINT: It exists somewhere between 1 and 1000 😇",
    "HINT: It was chosen randomly 😇",
    "HINT: It is not a letter 😇"
    "HINT: It is more than the money in your pocket😇"
    "HINT: It is not infinity 😇"
    "HINT: It is higher than your IQ 😇" 
    "HINT: Even I don't know what it is 😇"
 ]
print(random.choice(hints))
while True:
    count += 1
    Guess = int(input("🐍 Guess the number between 1 to 1000 = "))
    if Guess < 1 or Guess > 1000:
        print("Please Enter a number between 1 and 1000🚫")
        count -= 1 #dont count invalid guess
        continue
    difference = (Guess - secret_number) 
    if difference == 0:
        print(f"YOU WON in {count} counts")
        break
    elif difference >= 100:
        print("TOO HIGH🍆")
    elif 10 < difference  < 100:
        print("STILL HIGH😵")
    elif 0 < difference  < 10:
        print("You're close but go LOWER!💦")
    elif -10 < difference < 0:
        print("You're close but go HIGHER!💦")
    elif -100 < difference < -10:
        print("CLOSER THAN YOUR IQ😵")
    elif difference <= -100:
        print("TOO LOW🍆")

# def greet(name):
#     print("Hello " + name)

# greet("Aditya")
# greet("Python")
# def multiply(a,b=2):
#     return a * b

# result = multiply(4,3)
# print(result)
# number = (4,5,6)
# print(min(number))
# print(max(number))

# def min_max(a ,b ,c):
#     return min(a,b,c), max(a,b,c)

# small,large = min_max(5,2,8)
# print(small)
# print(large)
# def greet(name,age):
#     print(f"Hello {name} ,You are {age} years old" )

# greet("Aditya",17)

# def calculator(a,b):
#     return a+b,a-b,a*b,a/b
    
# print(calculator(10,2))

# def is_even_odd(numbers):
#     evens = []
#     odds = []
#     for number in numbers:
#      if number % 2 == 0:
#           evens.append(number)
#      elif number % 2== 1:
#           odds.append(number)
#     return evens, odds
# print(is_even_odd([1,2,3,4,5,6]))
          

