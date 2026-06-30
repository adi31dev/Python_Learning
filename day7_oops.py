# class Car:
#     def __init__(self,brand,color):
#             self.brand = brand
#             self.color = color
#             self.speed = 0

#     def start(self):
#           print(f"{self.brand} is starting!")

#     def accelerate(self,amount):
#           self.speed += amount
#           print(f"{self.brand} is now {self.speed}")

#     def brake(self):
#           self.speed = 0
#           print(f"{self.brand} has stopped")

    

# car1 = Car("Toyota", "Red")
# car1.start()
# car1.accelerate(30)
# car1.accelerate(20)
# car1.brake()

# class Phone:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
#         self.battery = 100

#     def turn_on(self):
#         print(f"{self.brand} is turning on!")

#     def use_battery(self,amount):
#         self.battery -= amount
#         print(f"{self.brand} battery is now at {self.battery}")

#     def charge(self):
#         self.battery = 100
#         print(f"{self.brand} is Fully Charged")

# my_phone = Phone("Samsung", "S24")
# my_phone.turn_on()
# my_phone.use_battery(30)
# my_phone.use_battery(20)
# my_phone.charge()


# class Animal():
#     def __init__(self,name):
#         self.name = name

#     def breathe(self):
#         print(f"{self.name} is breathing")

#     def eat(self):
#         print(f"{self.name} is eating")

# class Dog(Animal):
#     def bark(self):
#         print(f"{self.name} says Woof!")

# class Cat(Animal):
#     def meow(self):
#         print(f"{self.name} says Meow")

# dog = Dog("Bruno")
# cat = Cat("Whiskers")


# dog.breathe()
# dog.bark()
# cat.eat()
# cat.meow()


class BankAccount:
    def __init__(self,balance):
        self.__balance = balance #__ will make it private

    def deposit(self,amount):
            self.__balance += amount
            print(f"Deposited {amount} . Balance: {self.__balance}")

    def withdraw(self,amount):
            if amount <= self.__balance:
             self.__balance -= amount
             print(f"Withdrawn {amount} . Balance: {self.__balance}")
            
            else:
               print("Insufficient funds")

    def get_balance(self):
       return self.__balance
    
account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)

print(f"Your balance {account.get_balance()}")

