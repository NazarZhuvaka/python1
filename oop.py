# # Property. getter-метод і setter-метод
#
# class BankAccount:
#
#     def __init__(self, name, balance):
#         self.name = name
#         self.__balance = balance
#
#     @property
#     def my_balance(self):
#         return self.__balance
#
#     # my_property_balance = my_balance
#     @my_balance.setter
#     def my_balance(self, value):
#         if not isinstance(value, (int,float)):
#             raise ValueError('Balance must be int')
#         self.__balance = value
#
#     # my_balance = my_property_balance.setter(my_balance)
#     @my_balance.deleter
#     def delete_balance(self):
#         del self.__balance
#
#     balance = property(fget=get_balance, fset=set__balance, fdel=delete_balance)
#
#     my_balance = property(my_balance)
#     my_balance = my_balance.setter(set_balance)
#     my_balance = my_balance.deleter(delete_balance)
# #
# a1 = BankAccount('Ivan', 13500)
# a2 = BankAccount('Nazar', 1000000)
#
# print(a2.my_balance)
#
#
#
# # Замикання
#
# # def main_func():
# #     name = "Ivan"
# #     def inner_func():
# #         print("Hello", name)
# #
# #     return inner_func
# #
# # main_func()
#
# # Декоратор
# # from functools import wraps
# #
# # def header(func):
# #
# #     @wraps(func)
# #     def inner(*args,**kwargs):
# #         print("<h1>")
# #         func(*args,**kwargs)
# #         print("</h1>")
# #     # inner.__name__ = func.__name__
# #
# #     return inner
# #
# # def table(func):
# #
# #     def inner(*args,**kwargs):
# #         print("<table>")
# #         func(*args,**kwargs)
# #         print("</table>")
# #     return inner
# #
# # @table
# # @header # say1 = header(say)
# # def say(name,ff):
# #     print(f"hello {name}", ff)
# #
# # # say1 = table(header(say))
# # say("Nazar", 11)
from pickle import PROTO
# Вичисляємі свойства
#
# class Square:
#
#     def __init__(self,s):
#         self.__side = s
#         self.__area = None
#
#     @property
#     def side(self):
#         return self.__side
#
#     @side.setter
#     def side(self, value):
#         self.__side = value
#         self.__area = None
#
#     @property
#     def area(self):
#         if self.__area is None:
#             print('calculate')
#             self.__area = self.side**2
#         return self.__area
#
# a = Square(5)
# print(a.area)
# a.side = 7
# print(a.area)
# from string import digits
#
# # file = open('111.txt', 'a+')
# # print(file.read())
# # a = file.read()
# # print(a)
#
# class User:
#
#     def __init__(self, login , password):
#         self.login = login
#         self.password = password
#
#     # @staticmethod
#     # def open_file(password):
#     #     with open('111.txt', 'r', encoding="utf-8") as file:
#     #         content = file.readlines()
#     #         if content in password:
#     #             raise TypeError("Not strong!")
#     #         print(content)
#
#
#     @staticmethod
#     def is_include_number(password):
#         for digit in digits:
#             if digit in password:
#                 return True
#         return False
#
#     @property
#     def password(self):
#         print('Work getter')
#         return self.__password
#
#     @password.setter
#     def password(self, value):
#         print('Work setter')
#         if not isinstance(value, str):
#             raise TypeError("Passwort must be string")
#         if len(value) < 5:
#             raise ValueError("Password is very short")
#         if len(value) > 12:
#             raise ValueError("Password is too long")
#         if not User.is_include_number(value):
#             raise ValueError("Password must have 1 number")
#
#
#         self.__password = value
#
# u1 = User('Ivan', "help1")
# # User.open_file()
# print(u1.password)
# u1.password = "qwerty1"
# print(u1.password)

# class Example:
#
#     # def hello():
#     #     print("hello")
#
#     def instance_hello(self):
#         print(f"instance_hello {self}")
#
#     @staticmethod
#     def static_hello():
#         print("static_hello ")
#
#     @classmethod
#     def class_hello(cls):
#         print(f"class_hello {cls}")

# Пространство імен в класі
#  Магічні методи __str__ , __repr__

# class Lion():
#     def __init__(self, name):
#        self.name = name
#
#     # def __repr__(self):
#     #     return f"The object Lion - {self.name}"
#
#     def __str__(self):
#         return f"Lion - {self.name}"
#
# s = Lion("Simba")
# print(s)

#  Магічні методи __len__ , __abs__

# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def __len__(self):
#         return len(self.name + self.surname)
#
# class Line:
#     def __init__(self, point1, point2):
#         self.x1 = point1
#         self.x2 = point2
#
#     def __len__(self):
#         print("work len")
#         print(self)
#         return abs(self)
#
#     def __abs__(self):
#         print("work abs")
#         return abs(self.x2 - self.x1)
#
# a = Person("sd", "dasdas")
# print(len(a))
#
# b = Line(12, 5)
# print(len(b))

#  Магічні методи __add__ , __mul__ (множення) , __sub__ (сума), __truediv__ (ділення)

# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#
#     def __add__(self, other):
#         print("method add")
#         if isinstance(other, BankAccount):
#             return self.balance + other.balance
#         if isinstance(other, (int,float)):
#             return self.balance + other
#         raise NotImplemented
#
#     def __radd__(self, other):
#         print("__radd__")
#         return self+other
#
# a = BankAccount("Ivan", 600)
# b = BankAccount("sad", 900)
# print(a+12)

# Магічні методи __eq__(рівність об'єктів) , __hash__

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __eq__(self, other):
#         return isinstance(other , Point) and \
#                 self.x == other.x and self.y == other.y
#
#     def __hash__(self):
#         return hash((self.x, self.y))
#
# p1 = Point()

# метод __bool__
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y