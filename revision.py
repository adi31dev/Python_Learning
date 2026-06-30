# for i in range(1,21):
#     if i%2 == 0:
#         print(i)


def square_numbers(a,b,c,d):
    return a*a,b*b,c*c,d*d

print(square_numbers(2,3,4,5))

def square_numbers(numbers):
    squared = []
    for i in numbers:
        squared.append(i*i)
    return squared

print(square_numbers([2,3,4,45]))

def odd_numbers(numbers):
        odd = []

        for i in numbers:
            if i % 2 == 1:
             odd.append(i)
        return odd

print(odd_numbers([1,2,3,4,5,6,7,8,9,14])) 

def names(only_a_names):

    Names_with_a = []
    for i in only_a_names:
        if i[0] == "A":
            Names_with_a.append(i)
    return Names_with_a

print(names(["Aditya","Aditee","ankush","suresh"]))

guess = int(input("Guess: "))
while guess != 42:
    print("Wrong!")
    guess = int(input("Guess again: "))
print("Correct!")

number = 0
while number < 5:
    print(number)
    number += 1
print("Done!")

 

