# courses = [
#             {
#                 "title" : "Python",
#                 "teacher" : "Amiri",
#                 "total_time" : "65hr",
#                 "follwing" : 73628
#             },
#             {
#                 "title" : "HTML",
#                 "teacher" : "Bahrami",
#                 "total_time" : "50hr",
#                 "follwing" : 66548
#             },
#             {
#                 "title" : "C++",
#                 "teacher" : "Naseri",
#                 "total_time" : "90hr",
#                 "follwing" : 83838
#             },
#             {
#                 "title" : "Java",
#                 "teacher" : "Mahmodi",
#                 "total_time" : "102hr",
#                 "follwing" : 2021
#                 }
#                 ]

# class User:
#     def __init__(self):
#         self.courses = []
#         self.fname = input("Enter your first name: ")
#         self.lname = input("Enter your last name: ")
#         self.gmail = input("Enter your gmail: ")
#         self.age =int(input("Enter yout age: "))
#         while "@gmail.com" not in self.gmail:
#             self.gmail = input("Enter yout email correctly! Try again: ")
#     def print_fullname(self):
#         print(f"Welcome {self.fname} {self.lname}!\nGmail: {self.gmail}\nAge: {self.age}")
# # u1 = User()
# # u1.print_fullname()

# class Student(User):
#     def __init__(self):
#         super().__init__()
#         self.ID_No = int(input("Enter your ID.No: "))
#         self.courses = []
#     def print_fullname(self):
#         super().print_fullname()
#         print(f"You are a student with No {self.ID_No}")
#     def print_courses(self):
#         self.c = input("Which subject you wanna learn?: ")
#         for i in courses:
#             if i["title"] == self.c:
#                 self.courses.append(i["title"])
#             else:
#                 print("This user has no course.")
#         print(self.courses)

# s1 = Student()
# s1.print_courses()
# # s1.print_fullname()

# class Teacher(User):
#     def __init__(self):
#         super().__init__()
#         self.code = int(input("Enter your code: "))
#     def print_fullname(self):
#         super().print_fullname()
#         print(f"I am a mf Teacher with code: {self.code}")
# t1 = Teacher()
# t1.print_fullname()