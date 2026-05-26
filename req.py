# import requests
# r = requests.get("https://codeyad.com")
# if r.status_code == 200: print("successfully requested")
# else:
#     print("failed to request")
# print(r.text)


# one = [1, 2, 3]
# iterone = iter(one)
# print(next(iterone))
# print(next(iterone))
# print(next(iterone))
# print("--------------------------------------")
# two = (x for x in range(5))
# itertwo = iter(two)
# print(next(itertwo))
# print(next(itertwo))
# print(next(itertwo))
# print(next(itertwo))
# print(next(itertwo))
# print("--------------------------------------")
# three = range(10)
# iterthree = iter(three)
# print(next(iterthree))
# print(next(iterthree))
# print(next(iterthree))
# print(next(iterthree))
# print(next(iterthree))
# print(next(iterthree))
# print(next(iterthree))
# print(next(iterthree))
# print(next(iterthree))
# print(next(iterthree))
# print("--------------------------------------")
# four = "5"
# iterfour = iter(four)
# print(next(iterfour))



# class Iterer:
#     def __init__(self, number):
#         self.number = number
#     def __iter__(self):
#         self.one = 1
#         return self
#     def __next__(self):
#         if self.one < self.number:
#             x = self.one
#             self.one += 1
#             return x
#         else:
#             raise StopIteration
# i1 = Iterer(10)
# # i1_2 = iter(i1)
# for n in i1:
#     print(n)




# class EvenNum:
#     def __init__(self, number):
#         self.number = number
#     def __iter__(self):
#         self.zero = 0
#         return self
#     def __next__(self):
#         if self.zero < self.number:
#             even = self.zero
#             self.zero += 2
#             return even
#         else:
#             raise StopIteration
# e1 = EvenNum(10)
# for e in e1:
#     print(e)


# def count_up_to(limit):
#     n = 1
#     while n <= limit:
#         yield n
#         n += 1
# for i in count_up_to(10):
#     print(i)


# def even_num(limit):
#     n = 0
#     while n <= limit:
#         yield n
#         n +=2
# for e in even_num(10):
#     print(e)


# def reverse_str(text):
#     for ch in reversed(text):
#         # print(ch)
#         yield ch
# # reverse_str("hello")
# for ch in reverse_str("hello"):
#     print(ch)


# print(list(map((lambda x: x**2),[1,2,3,4])))
# print(list(filter((lambda x: x%2==0),[1,2,3,4])))
# print(dict(zip([1,2,3],["a","b","c"])))



# import random

# for n in iter((lambda: random.randint(1, 10)), 5):
#     print(n)


# nums = [1,2,3,4]
# inum = iter(nums)
# print(next(inum))
# print(next(inum))
# print(next(inum))
# print(next(inum))


# def checker(nums):
#     if 


# try:
#     x = int(input("Enter a number: "))
#     if x < 0:
#         raise ValueError("Negative numbers are not allowed!")
# except ValueError as e:
#     print(f"An error occurred: {e}")



# try:
#     x = int("abc")  # This will raise a ValueError
# except ValueError as e:
#     print("Caught a ValueError!")
#     raise  # Re-raises the same exception
