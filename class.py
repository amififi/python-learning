
# class Pasur:
#     def __init__(self):
#         self.khaj = ["gishniz", "peak", "kheshte", "del"]
#         self.value = ["1", "shah", "bibi","sarbaz", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
#         self.cards = [f"{k} {v}" for k in self.khaj for v in self.value]
#     def __getitem__(self, index_card):
#         if index_card >= 52:
#             raise Exception("Sorry, no numbers below 52")
#         return self.cards[index_card]
#     def __len__(self):
#         return len(self.cards)
#     def value_checker(self, index1, index2):
#         print(self[index1])
#         print(self[index2])
#         k1 ,v1 = self[index1].split()
#         k2 ,v2 = self[index2].split()
#         if k1 != k2:
#             raise Exception("Sorry, not equal khal")
#         else:
#             if self.value.index(v1) > self.value.index(v2):
#                 print(f"{self[index2]} is more than {self[index1]}")
#             else:
#                 print(f"{self[index1]} is more than {self[index2]}")
# p1 = Pasur()
# print(len(p1))
# print(p1[5])
# p1.value_checker(9, 9)



# class MyDict:
#     def __init__(self):
#         self.dict = {"a":1, "b":2, "c":3}
#     def __getitem__(self, key):
#         if key in self.dict:
#             return self.dict[key]
#         else: raise KeyError(f"Key '{key}' not found.")
# m1 = MyDict()
# print(m1["b"])


# for number in range(10):
#     if number == 5:
#         break 
#     print(number)

# for number in range(10):
#     if number % 2 == 0:
#         continue
#     print(number)


# class Counter:
#     def __init__(self):
#         self.items = {}
#     def buying(self):
        


# class MyStack:
#     def __init__(self):
#         self.stack = []
#         self.min_stack = []

#     def push(self, item):
#         self.item = item
#         self.stack.append(item)
#         if len(self.min_stack) == 0:
#             self.min_stack.append(item)
#         else:
#             if item < self.min_stack[-1]:
#                 self.min_stack.append(item)
#         print(self.stack)

#     def pop(self):
#         if len(self.stack) == 0:
#             raise Exception("There is no item!")
#         else:
#             i = self.stack.pop()
#             print(f"the deleted item : {i}")
#             if i == self.min_stack[-1]:
#                 self.min_stack.pop()

#     def peak(self):
#         print(f"The last item is {self.stack[-1]}")

#     def __iter__(self):
#         # i= iter(self.stack)
#         for i in self.stack:
#             yield i


#     def __len__(self):
#         return len(self.stack)
    
#     def get_min(self):
#         print(self.min_stack[-1])
    # def get_min(self):
    #     min = self.stack[0]
    #     for s in self.stack[0:]:
    #         if min > s:
    #             min = s
    #     print(f"{min} is the minimum")

# m1 = MyStack()
# m1.push(4)
# m1.push(2)
# m1.push(3)
# m1.pop()
# m1.get_min()
# m1.push(3)
# m1.push(2)
# m1.pop()
# m1.get_min()
# m1.push(5)
# for i 
# print("--------------------------")
# m1.peak()
# print("--------------------------")
# for i in m1:
#     print(i)
# print("--------------------------")
# print(len(m1))
# print("--------------------------")

# m1.get_min()




# class Person:
#     def __init__(self, fname, lname, id, age):
#         self.fname = fname
#         self.lname = lname 
#         self.id = id
#         self.age = age
#     def __str__(self):
#         return f"firstname: {self.fname}, lastname: {self.lname}, ID: {self.id}, age: {self.age}"
    
# class Teacher(Person):
#     def __init__(self, fname, lname, id, age, subject):
#         super().__init__(fname, lname, id, age)
#         self.subject = subject
#     def __str__(self):
#         return f"{super().__str__()}, subject: {self.subject}"
    
# class Student(Person):
#     def __init__(self, fname, lname, id, age, major, grade):
#         super().__init__(fname, lname, id, age)
#         self.major = major
#         self.grade = grade
#     def __str__(self):
#         return f"{super().__str__()}, major: {self.major}, self: {self.grade}"

# t1 = Teacher("Zohreh", "Najaf", 873245, 48, "physics")
# print(t1)
# s1 = Student("Fatemeh", "Shafiee", 392067, 16, "math", "11th")
# print(s1)






# class Shape:
#     def area(self):
#         return f"Shape area: 0"
# s1 = Shape()
# print(s1.area())

# class Rectangle(Shape):
#     def __init__(self, width, height):
#         super().__init__()
#         self.width = width
#         self.hight = height
#     def area(self):
#         return f"Rectangle area: {self.width * self.hight}"
# r1 = Rectangle(10, 2)
# print(r1.area())

# import math
# class Circle(Shape):
#     def __init__(self, radius):
#         super().__init__()
#         self.radius = radius
#     def area(self):
#         return f"Circle area: {self.radius * 2 * math.pi}"
# c1 = Circle(12.5)
# print(c1.area())




# class BankAccount():
#     def __init__(self, balance):
#         self.__balance = balance
#     @property
#     def balance(self):
#         return self.__balance
#     def deposit(self, amount):
#         if amount < 0:
#             raise ValueError("Value must be non-negative")
#     def withdraw(self, amount):
#         if amount > self.__balance:
#             raise ValueError("Value must be smaller")
# acc = BankAccount(1000)
# acc.deposit(500)
# print(acc.balance)
# acc.withdraw(2000)



# class Employee:
#     def __init__(self, name, salary, role):
#         self._name = name
#         self.__salary = salary
#         self.role = role
#         self.idcard = self.IDCard(name, role)
#     @property
#     def salary(self):
#         return self.__salary
#     def work(self):
#         return "working"
#     class IDCard:
#         def __init__(self, name, role):
#             self.name = name
#             self.role = role
#         def display(self):
#             print(self.name, self.role)
# e1 = Employee("yasamin",2000, "developer")
# print(e1.salary)
# e1.idcard.display()
# class Developer(Employee):
#     def __init__(self, name, salary):
#         super().__init__(name, salary)
#     def work(self):
#         return "coding"

# d1 = Developer("ALice", 3000)
# print(d1.work())
# class Manager(Employee):
#     def __init__(self, name, salary):
#         super().__init__(name, salary)
#     def work(self):
#         return "managing"

# import random
# Posibilities = ["Rock", "Paper", "Scissors"]
# UserChoice = input("Rock, Paper or Scissors?\nYour Choice: ")
# ComputerChoice = random.choice(Posibilities)
# print(f"Computer Choice: {ComputerChoice}")
# if ComputerChoice == Posibilities[0]:
#     print("yay")
# if 
# class Rules:


# import random
# class Guess_the_number:

#     def __init__(self):
#         self.point = 10
#         self.rand = random.randint(1, 100)

#     def play(self):
        
#         while self.point > 0:
#             self.user_guess = int(input("guess: "))
            
#             if self.user_guess == self.rand:
#                 print("you won!")
#                 print(f"your point: {self.point}")
#                 return
            
#             elif self.user_guess > self.rand:
#                 print("the number you guessed is bigger")
#                 self.point -= 1
#                 print(f"your point: {self.point}")

#             else:
#                 print("the number you guessed is smaller")
#                 self.point -= 1
#                 print(f"your point: {self.point}")
            
#         print("game over!")
#         print(f"the number was {self.rand}")


    

# g1 = Guess_the_number()
# g1.play()

# l = [1,2,4,5,5,6]
# print(l.index(4))

import random
class Rock_scissors_paper:
    def __init__(self):
        self.choices = ["rock", "scissors", "paper"]
        self.urpoint = 0
        self.cpoint = 0

    def play(self):
        while self.urpoint != 3 or self.cpoint != 3:
            self.user = input("rock, scissors or paper?: " )
            if self.user not in self.choices:
                raise Exception("Sorry, your answer should be from the expected values")
            print(f"computer choice: {random.choice(self.choices)}")
            if self.choices.index(self.user) == "paper" and self.choices.index(random.choice(self.choices)) == "rock":
                print("W")
                if  self.choices.index(self.user) > self.choices.index(random.choice(self.choices)):
                    print("L")
                    self.cpoint =+ 1
                    print(f"computer point: {self.cpoint}")
                    print(f"your point: {self.urpoint}")
                elif self.choices.index(self.user) < self.choices.index(random.choice(self.choices)):
                    print("W")
                    self.urpoint =+ 1
                    print(f"computer point: {self.cpoint}")
                    print(f"your point: {self.urpoint}")
                elif self.choices.index(self.user) == self.choices.index(random.choice(self.choices)):
                    print("T")
                    print(f"computer point: {self.cpoint}")
                    print(f"your point: {self.urpoint}")

                    self.urpoint =+ 1
                    print(f"computer point: {self.cpoint}")
                    print(f"your point: {self.urpoint}")


p = Rock_scissors_paper()
p.play()

        




















