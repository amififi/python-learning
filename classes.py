# class Yasi:
    # def init(self):
    #     pass
    # x=12
    # y=23
    # def sum(self):
    #     return self.x + self.y
# print(Yasi().sum())
# class My_class:
#     def init(self,x,y):
#         self.x = x
#         self.y = y
#     def sum(self):
#         return self.x + self.y
# print(My_class(12,23).sum())

# class MyClass:
#     def init(self, value):
#         self.value = value  # attribute

#     def show(self):  # method
#         print(f"Value is {self.value}")
# MyClass(10).show()


# class Car:
#     def init(self,speed,brand):
#         self.brand = brand
#         self.speed = speed
#     def accelerate(self):
#         self.speed += 10
#         print(f"{self.brand} speed is {self.speed} km/h")
# Car(12,"bmw").accelerate()



# class Info:
#     def init(self,name,age):
#         self.name=name
#         self.age=age
#     def printing(self):
#         print("Name:",self.name, "Age:",self.age)
# Info("fifi",13).printing()
# print(hasattr(Info("fifi",12),"car"))
# print(getattr(Info("fifi",12),"name"))



# class Rectangle:
#     def init(self,width, height):
#         self.width=width
#         self.height=height
#     def area(self):
#         return self.width * self.height
# print(Rectangle(5,3).area())


# class BankAcount:
#     def init(self,n2,n1):
#         self.n2=n2
#         self.n1=n1
#     def difference(self):
#         return self.n2 - self.n1
# print(BankAcount(30,14).difference())



# class Dog:
#     def init(self,name,breed):
#         self.name=name
#         self.breed=breed
#     def bark(self):
#         self.breed="says woof!"
#         print(self.name,self.breed)
# Dog("Rex","speak").bark()


# class BankAccount:
#     def init(self, deposit, withdraw, limit_check):
#         self.deposit=deposit
#         self.withdraw=withdraw
#         self.limit_check=limit_check
#     def limit_of_balance(self):
#         if self.balance_check < -500:
#             return "you have passed your limit!"
    # def str(self):
    #     pass


# class Car:
#     def init(self, brand, model, year):
#         self.brand=brand
#         self.model=model
#         self.year=year
#     def str(self):
#         return "Brand:",self.brand,"Model:",self.model,"Year:",self.year
# print(Car("pride","725",1404).str())


# class Rectangle:
#     def init(self,width,height):
#         self.width=width
#         self.height=height
#     def area(self):
#         return self.width * self.height
#     def perimeter(self):
#         return 2*(self.height+self.width)
# print(Rectangle(2,3).perimeter())


# class Counter:
#     def init(self,num=0):
#         self.num=num
#     def increment(self):
#         self.num +=1
#         return self.num
#     def decrement(self):
#         self.num -=1
#         return self.num
#     def reset(self):
#         while self.num!=0:
#             self.num-=1
#         return self.num
#     def get_value(self):
#         return self.num
# print(Counter(2).get_value())


# class ShoppingCart:
#     # cart={}
#     def init(self,name,price,quantity=1):
#         self.name=name
#         self.price=price
#         self.quantity=quantity
#     def add_item(self):
#         self.quantity+=self.name
#     def remove_item(self):
#         del self.name
#     def total_price(self):
#         total_price=0
#         total_price+=self.price
#     def str(self):
#         return "name:",self.name,"total price:",self.price
# print(ShoppingCart("krm",33).str())


# class ShoppingCart:
#     def init(self):
#         self.items = {}  # {name: [price, quantity]}

#     def add_item(self, name, price, quantity=1):
#         if name in self.items:
#             self.items[name][1] += quantity
#         else:
#             self.items[name] = [price, quantity]

#     def remove_item(self, name):
#         if name in self.items:
#             del self.items[name]

#     def total_price(self):
#         return sum(price * qty for price, qty in self.items.values())


#     def str(self):
#         cart_str = "Shopping Cart:\n"
#         for name, (price, qty) in self.items.items():
#             cart_str += f"{name} - {qty} x ${price}\n"
#         cart_str += f"Total: ${self.total_price():.2f}"
#         return cart_str
# print(ShoppingCart().str())
        



# class Student:
#     count=0
#     def init(self,name,gpa):
#         self.name=name
#         self.gpa=gpa
#         Student.count+=1                #???
#     def get_info(self):
#         return f"{self.name} {self.gpa}"
#     @classmethod
#     def get_count(cls):
#         return f"total # of students: {cls.count}"
    
# student1 = Student("gozo", 9.8)
# student2 = Student("ano", 7.8)
# student3 = Student("kono", 11.0)
# print(Student.get_count())

# import datetime
# class User:
#     '''just collecting the fullname and age of the user'''
#     def init(self, full_name, birthday):
#         self.name= full_name
#         self.birthday=birthday          #yyyymmdd
        
#         name_pieces= full_name.split(" ")
#         self.first_name = name_pieces[0]
#         self.last_name = name_pieces[-1]

#     def age(self):
#         today = datetime.date(2025, 8, 17)
#         yyyy = str(self.birthday[:4])
#         mm = str(self.birthday[4:6])
#         dd = str(self.birthday[6:8])
#         bod = datetime.date(yyyy, mm, dd)
#         age_in_days = (today - bod).days
#         age_in_year = age_in_days / 365
#         return int(age_in_year)
        

# # help(User)

# user1= User("fatemeh shafiee","20090617")
# # print(user1.name)
# # print(user1.birthday)
# # print(user1.first_name)
# # print(user1.last_name)
# print(user1.age())






# class ShoppingChart:
#     count = 0
#     def init(self, items, price):
#         self.items = items
#         self.price = price
#         ShoppingChart.count+=self.price
#     def chart(self):
#         print(f"you bought {self.items} and the price is {self.price}")
#     @classmethod
#     def total(cls):
#         print(f"the total price of shit you bought is {cls.count}")
# item1 = ShoppingChart("bag", 12)
# item2 = ShoppingChart("hat", 8)
# item3 = ShoppingChart("neckless", 5)
# item4 = ShoppingChart("bracelet", 5)
# item5 = ShoppingChart("car", 100)
# item1.chart()
# item2.chart()
# item3.chart()
# item4.chart()
# item4.total()


# class BankAccount:
#     deposit_amount=0
#     withdraw_amount=0
#     def init(self,owner,balance):
#         self.owner = owner
#         self.balance = balance
#         BankAccount.deposit_amount+=self.balance
#     # @classmethod
#     def deposit(self,amount):
#         self.balance+=amount
#         BankAccount.deposit_amount+=amount
#         print(f"Dear {self.owner}, the deposit that you made is {amount}, your new balance is {self.balance}")
#     def withdraw(self,amount):
#         self.balance-=amount
#         BankAccount.withdraw_amount-=amount
#         print(f"and the withdraw is {amount}")
# account = BankAccount("fifi",2000)
# account.withdraw(100)

        


# class Rectangle:
#     def init(self, width=int, height=int):
#         self.width=width
#         self.height=height
#     def area(self):
#         area=self.width * self.height
#         print(f"the area of rectangle is {self.width} * {self.height} = {area}")
#     def premeter(self):
#         premeter=2*(self.width + self.height)
#         print(f"the area of rectangle is 2({self.width} + {self.height}) = {premeter}")
#     def is_square(self):
#         if self.width==self.height:
#             print(True)
#         else:print(False)
# rec1= Rectangle(4,4)
# rec1.area()
# rec1.premeter()
# rec1.is_square()


# class Book:
#     def init(self, title, auther, pages):
#         self.title = title
#         self.auther = auther
#         self.pages = pages
# class Library:
#     def init(self):
#         self.book = Book()
#     # def add_book(self,title):
#     #     Book.list_of_book.append(title)
#     # def list_books(self):
#     #     print(self.list_of_book)
#     # def find_by_auther(self,auther):
# # b1 = Book("the end", "abas", 365)
# # b2 = Book("the star", "mohsen", 290)
# b1 = Library()
# # print(b1.init)
# # b1.add_book("the end")
# # b2.add_book("stars")
# # b2.list_books()
# # b1 = Book()







# class Book:
#     def init(self, title), auther, pages):
#         self.title) = title)
#         self.auther = auther
#         self.pages = pages
#         # self.the_list = the_list
#     def str(self):
#         print(f"Name:{self.title}, auther:{self.auther}, pages:{self.pages}")

# class Library:
#     def init(self):
#         self.all_books = []
#     def add_book(self,book):
#         self.all_books.append(book)

# b1 = Book("The stars", "Fatemeh", 98)
# b1.book_info()




# class Car:
#     def init(self, name, price):
#         self.name = name
#         self.price = price
#         self.status = False
#     def start(self):
#         if self.status == False:
#             self.status=True
#             print(f"{self.name} is starting")
#         else:
#             print(f"{self.name} is already on")
#     def turn_off(self):
#         if self.status:
#             self.status=False
#             print(f"{self.name} is turning off")
#         else:
#             print(f"{self.name} is already off!")
# c1 = Car("BMW",110000000)
# c1.start()
# c1.start()
# c1.turn_off()
# c1.turn_off()




# class Person:
#     def init(self, fname, lname):
#         self.fname = fname
#         self.lname = lname
#     def info(self):
#         print(f"Welcome {self.fname} {self.lname}")
# p1 = Person("Fatemeh","Shafiee")
# # p1.info()        
# class Student(Person):
#     def init(self, fname, lname, age, ID_Number, grade):
#         Person.init(self, fname, lname)
#         self.age = age
#         self.ID_Number = ID_Number
#         self.grade = grade
#     def child_info(self):
#         print(f"student full name: {self.fname} {self.lname}\nstudnet age: {self.age}\nstudent ID number: {self.ID_Number}\nstudent grade: {self.grade}")
# s1 = Student("Fatemeh", "Shafiee", 16, 203801293, "11th")
# s1.info()
# s1.child_info()


# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         self.available = True
#     def borrow(self):
#         if self.available == True:
#             self.available = False
#             print("you borrowed the book.")
#         elif self.available == False:
#             print("Not available.")
#     def return_book(self):
#         if self.available == False:
#             self.available = True
#             print("you returned the book.")
#         elif self.available == True:
#             print("you already retruned the book.")
# b1 = Book("Stars", "Me")
# b1.borrow()
# b1.borrow()
# b1.borrow()
# b1.return_book()
# b1.return_book()
# b1.borrow()



# Create a class Student with attributes: name and grades (a list).

# Add methods:

# add_grade(grade)

# get_average() → returns the average of all grades.

# Create a few students, add grades, and print their averages


# class Student:
#     average = []
#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade
#     def add_grade(self):
#         Student.average.append(self.grade)
#         print(self.average)
#     def get_average(self):
#         print(sum(self.average) // len(self.average))

# s1 = Student("fifi",9)
# s2 = Student("zahra",11)
# s3 = Student("riri",7)
# s1.add_grade()
# s2.add_grade()
# s3.add_grade()
# s1.get_average()



# class Cart:
#     item_price = {}
#     def __init__(self,item, price):
#         self.item = item
#         self.price = price
#     def add_items(self):
#         Cart.item_price[self.item]=self.price
#         return Cart.item_price
#     def remove_items(self):
#         del Cart.item_price[self.item]
#         return Cart.item_price
#     def total(self):
#         return sum(Cart.item_price.values())

# C1 = Cart("hat", 8)
# C2 = Cart("milk", 4)
# C3 = Cart("skirt", 6)
# C3.add_items()
# C1.add_items()
# print(Cart.item_price)
# # C1.remove_items()
# # print(Cart.item_price)
# # C1.add_items()
# print(Cart.item_price)
# print(C3.total())

# C2.add_items()
# print(C1.add_items())



# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#     def give_raise(self, amount):
#         amount += self.salary
#         return f"{self.name}'s new salary is {amount}"
# e1 = Employee("angy", 20)
# e2 = Employee("fifi", 30)
# print(e1.give_raise(90))
# print(e2.give_raise(19))






# class Book:
#     def __init__(self, name, auther):
#         self.name = name
#         self.auther = auther
#     def __str__(self):
#         return(f"Name: {self.name}, Auther: {self.auther}")
# b1 = Book("Star", "KOP")
# # b1.__str__()
# class Library:
#     def __init__(self):
#         self.book = []
#     def add_book(self,book):
#         self.book.append(book)
#     def list_of_book(self):
#         if not self.book:
#             print("there is no book here")
#         else:
#             print("books in the library:")
#             for book in self.book:
#                 print("-", book)
# l1 = Library()
# l1.add_book(b1)
# l1.list_of_book()





# class Student:
#     student_grade = {}
#     def __init__(self, name, grade):
#         self.name =name
#         self.grade = grade
#         Student.student_grade[self.name] = self.grade
#     def __str__(self):
#         return (f"{self.name} in grade {self.grade}")
#         # return self.student_grade
#     def add_grade(self):
#         l_of_g=list(self.student_grade.values())
#         return l_of_g
#     def average(self):
#         for _ in list(self.student_grade.values()):
#             k=sum(list(self.student_grade.values()))//len((list(self.student_grade.values())))
#         print(k)
# s1 = Student("ng",9)
# s2 = Student("september", 11)
# # print(s1.__str__())
# # s1.add_grade()
# # s1.average()
# class School:
#     def __init__(self):
#         self.student = []
#     def add_student(self, student):
#         self.student.append(student)
#     def list_of_student(self):
#         # print(s for s in self.student)
#         if not self.student:
#             print("the list is empty")
#         else:
#             print("the students are: ")
#             for i in self.student:
#                 print(i.name)
# school = School()
# school.add_student(s2)
# school.add_student(s1)
# school.list_of_student()




# class Course:
#     def __init__(self, name, professor, *e_s):
#         self.name = name
#         self.professor = professor
#         self.enrolled_students = e_s
#     def __str__(self):
#         return (f"-Name of the course: {self. name}\n"
#                f"-Professor: {self.professor}\n"
#                f"-The enrolled student: {self.enrolled_students}")
# c1 = Course("Art", "Mrs.Jamshidnia", "Fifi", "Zahra", "Ng", "Yasi")
# c2 = Course("Mathematics", "Miss Rivi", "Fifi", "Melike") 
# c3 = Course("Science", "Miss Anne", "Zahre", "Riri") 
# # print(c1.enrolled_students)
# print(c1.__str__())
# print(c3.__str__())
# # print(type(c1.enrolled_students))
# class Professor:
#     def __init__(self):
#         self.course = []
#     def teaching_cs(self, courses):
#         self.course.append(courses)
#     def showing_tch_cs(self):
#         if not self.course:
#             print("There is no course here.")
#         else:
#             print(f"The courses are being tought are: ")
#             for c in self.course:
#                 print(f"{c.name} by {c.professor}")
# professor = Professor()
# # professor.teaching_cs(c1)
# # professor.teaching_cs(c2)
# # professor.showing_tch_cs()
# # A Student can enroll in multiple courses and has grades per course
# class Student:
#     def __init__(self):
#         self.enrolled_courses = []
#     def enrolling(self, courses):
#         self.enrolled_courses.append(courses)
#     def showing_en_cs(self):
#         if not self.enrolled_courses:
#             print("There is no course here.")
#         else:
#             print(f"The enrollled courses are: ")
#             for c in self.enrolled_courses:
#                 print(f"{c.name} by {c.enrolled_students}") 
# student = Student()  
# # student.enrolling(c1)
# # student.enrolling(c3)
# # student.showing_en_cs()       
# # The University should be able to:
# # Add students, professors, and courses.
# # Print each student’s GPA across all courses.
# # Print which professor teaches the most students.
# class University:
#     def __init__(self):
#         self.students = []
#         self.professors = []
#         self.courses = []

#     def add_students(self, st):
#         self.students.append(st)
#     def print_student(self):
#         for s in self.students:
#             print(s.enrolled_students)

#     def add_professor(self, ph):
#         self.professors.append(ph)
#     def print_proferssor(self):
#         for p in self.professors:
#             print(p.professor)

#     def add_courses(self, cr):
#         self.courses.append(cr)
#     def print_courses(self):
#         for c in self.courses:
#             print(c.name)
    
#     def most_pro(self):
#         most = max(self.courses, key=lambda c: len(c.enrolled_students))
#         print(f"The professor with the most students is {most.professor}, "
#         f"teaching {len(most.enrolled_students)} students in {most.name}.")
#         print(most)
# university = University()
# # university.add_students(c1)
# # university.print_student()
# # university.add_professor(c2)
# # university.add_professor(c3)
# # university.print_proferssor()
# university.add_courses(c3)
# university.add_courses(c1)
# # university.print_courses()
# university.most_pro()





# Classes: Flight, Passenger, Reservation, Airline.
# A flight has a flight number, destination, seats, and booked passengers.
# A passenger can book a flight (creating a Reservation).
# The airline should:
# Add flights.
# Book passengers into flights (if seats available).
# Print a passenger’s reservations.
# Find which flight has the highest occupancy rate.


# class Passengers:
#     def __init__(self, passenger):
#         self.passenger = passenger
#     def __str__(self):
#         return "kjmd"
# p1 = Passengers("Fatemeh")
# p2 = Passengers("Yasamin")
# p3 = Passengers("Angy")
# p4 = Passengers("Gazal")
# p5 = Passengers("Maysam")

# class Flight:
#     def __init__(self, flight_no, destination):
#         self.flight_no = flight_no
#         self.destinatin = destination
#         self.available_seats = ["The unavailable seats are: "]
#         self.booked_passengers = []
#     def add_available_seats(self, seat):
#         self.available_seats.append(seat)
#     def add_to_booked(self, passenger):
#         self.booked_passengers.append(passenger)
#     def print_booked(self):
#         print("The list of booked passenger includes:")
#         for p in self.booked_passengers:
#             print("-",p.passenger)
#     def __str__(self):
#         return f"Flight_no: {self.flight_no}, destination: {self.destinatin}, seats: {self.seats}, booked_passengers: {self.booked_passengers}"

# f1 = Flight(123455, "Tehran")
# f2 = Flight(667788, "Canada")
# f2.add_available_seats(23)
# f2.add_available_seats(29)
# f2.add_available_seats(18)
# f2.add_available_seats(21)
# f2.add_available_seats(30)
# f2.add_available_seats(9)
# f2.add_available_seats(15)
# f2.add_available_seats(12)
# print(f2.available_seats)
# f1.add_to_booked(p1)
# f1.add_to_booked(p2)
# f1.print_booked()
# # print(f1.__str__())

# class Reservation(Passengers):
#     def __init__(self, passenger):
#         super().__init__(passenger)
#         self.book_flight = []
#         self.passenger_in_a_flight = []
#     def booking(self, flight):
#         self.book_flight.append(flight)
#     def printing_info(self):
#         for b in self.book_flight:
#             self.passenger_in_a_flight.append(self.passenger)
#             print(f"Mr/Miss {self.passenger} booked the {b.flight_no} flight.")
#     def printinig_passenger_in_a_flight(self):
#         print("the passengers for the flight are:")
#         print(self.passenger)
#     # def occupancy_rate(self):


# r1 = Reservation(p1.passenger)
# r2 = Reservation(p2.passenger)
# r3 = Reservation(p3.passenger)
# r2.__str__()
# r1.booking(f1)
# r2.booking(f2)
# r3.booking(f2)
# r1.printing_info()
# r2.printing_info()
# r3.printing_info()
# r3.printinig_passenger_in_a_flight()

# class Airlines:
#     def __init__(self):
#         self.flights = []
#     def add_flight(self,flight):
#         self.flights.append(flight)
#     def print_flights(self):
#         print("The list of flights are:")
#         for f in self.flights:
#             print("-",f.flight_no)
#     def booking_seat(self,available_seats ,seat):
#         if seat in available_seats:
#             print("Unavailable")
#         else:
#             print("Available")

# airline = Airlines()
# airline.add_flight(f2)
# airline.print_flights()
# airline.booking_seat(f2.available_seats,17)






# class MenuItem:
#     menu = {}
#     def __init__(self, name, price, category):
#         self.name = name
#         self.price = price
#         self.category = category
#         MenuItem.menu[self.name] = f"RM{self.price}, {self.category}"
#     def __str__(self):
#         return MenuItem.menu
# item1 = MenuItem("Kokosabzi", 33, "Food")
# item2 = MenuItem("Noodle", 20, "Food")
# item3 = MenuItem("Ghormeh Sabzi", 45, "Food")
# item4 = MenuItem("Ghaimeh", 50, "Food")
# item5 = MenuItem("Kabab", 60, "Food")
# item6 = MenuItem("Makarani", 17, "Food")
# item7 = MenuItem("Jelly", 6, "Dessert")
# item8 = MenuItem("Yogert", 5, "Dessert")
# item9 = MenuItem("Salsd", 7, "Dessert")
# item10 = MenuItem("CheesCake", 6, "Dessert")
# item11 = MenuItem("Ice Cream", 3, "Dessert")
# item12 = MenuItem("Macha", 6, "Drink")
# item13 = MenuItem("Nescafe", 4, "Drink")
# item14 = MenuItem("Dogh", 3, "Drink")
# item15 = MenuItem("Soda", 2, "Drink")
# item16 = MenuItem("Milk", 5, "Drink")
# item17 = MenuItem("Tea", 5, "Drink")
# print(item17.__str__())

# class Order:
#     def __init__(self):
#         self.ordered_items = []
#     def adding_item(self, oredered_i):
#         if oredered_i not in MenuItem.menu:
#             print("The items are not avaliable")
#         else:
#             self.ordered_items.append(oredered_i)
#     def printing_items(self):
#         print(self.ordered_items)
    

#     def total(self):
#         print()




# o1 = Order()
# o1.adding_item("Dogh")
# o1.adding_item("Kabab")
# o1.adding_item("Kokosabzi")
# # o1.adding_item("Kkosbzi")
# o1.printing_items()
# # o1.total()


# class Restaurent:
#     pass



# item = " "
# price = 0
# basement = {}
# while item != "":
#     item = input("Items: ")
#     if item == "":
#         break
#     price = int(input("Its price: "))
#     basement[item]=price
# print(basement)
# print(sum(basement.values()))
# x = 10
# while x != 5:
#     x-=1
#     print(x)
#     if x ==5:
#         break

import random
import time
class Pet:
    def __init__(self, name, hunger, happiness, energy):
        self.name = name
        self.hunger = hunger
        self.happiness = happiness
        self.energy = energy
        self.statusbool = True
    def feed(self):
        phrases_hunger = ["GIrl..?", "ExCusE Me?", "N^%&O...", "doN:t DOthIS", "enoUGH"]
        print("-HUNGER:")
        if self.hunger == 100:
            print(f"{self.name} is full!")
        elif 100 > self.hunger >= 90:
            print(f"{self.name} is not that hungery, you can make them full with a strawberry")
        elif 90 > self.hunger >= 60:
            print(f"you can make {self.name} full with something delicious like cake")
        elif 60 > self.hunger >= 30:
            print(f"{self.name} needs food real bad!")
        elif 30 > self.hunger >= 0:
            print(f"{self.name} is starving!!!")
        else:
            print(random.choice(phrases_hunger))
    def play(self):
        phrases_happiness = [f"do you wanna make {self.name} sad?", "CRUEL.", "dont do this..", "plEasSe.."]
        print("-HAPPINESS:")
        if self.happiness == 100:
            print(f"{self.name}, is really happy now!!!")
        elif 100 > self.happiness >= 90:
            print(f"let's play {self.name}! yay!")
        elif 90 > self.happiness >= 60:
            print(f"{self.name} needs some happiness..")
        elif 60 > self.happiness >= 30:
            print(f"{self.name} is bored...")
        elif 30 > self.happiness >= 0:
            print(f"{self.name} is depressed...")
        else:
            print(random.choice(phrases_happiness))
    def sleep(self):
        phrases_sleep = ["are you cRaZY?", "no", "it is now right..", "stop"]
        print("-ENERGY:")
        if self.energy == 100:
            print(f"{self.name} does not wanna sleep now, let's play instead!")
        elif 100 > self.energy >= 90:
            print(f"Fine. but just for a few hours.")
        elif 90 > self.energy >= 60:
            print(f"maybe {self.name} can sleep now.")
        elif 60 > self.energy >= 30:
            print(f"okay, let let {self.name} take some rest.")
        elif 30 > self.energy >= 0:
            print(f"{self.name} is dying, please give them this chance...")
        else:
            print(random.choice(phrases_sleep))
    def status(self):
        gradient = [self.energy,self.happiness,self.hunger]
        avarage = sum(gradient)/ len(gradient)
        print("STATUS: ")
        if 100 >= avarage >= 80:
            print(f"{self.name} is PERFECT.")
        if 79 >= avarage >= 60:
            print(f"{self.name} wants you to be with them!!")
        if 59 >= avarage >= 40:
            print(f"HEy... {self.name} is sad...")
        if 39 >= avarage >= 20:
            print(f"UmMMm... HeLLo?")
        if 19 >= avarage >= 0:
            print("$#@^&*(&^%$H$!!2e34l)*^%p:!~")
    # def death(self):
        # while self.hunger > 10 and self.energy < 50:
# p1 = Pet("Puppet", 9, 83,3)
# p1.feed()
# p1.play()
# p1.sleep()
# p1.status()




import time
class Pet:
    def __init__(self,name):
        self.name = name
        self.happiness = 100
        self.energy = 100
        self.hunger = 100
    def feed(self):
        time.sleep(120)
        self.hunger - 10
        print(self.hunger)
p1 = Pet("Lou")
p1.feed()









    