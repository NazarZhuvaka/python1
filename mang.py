# file = open('111.txt', 'w', encoding='utf-8')
#
# file.close()

# lst = []

# for i in range(10000):
#     with open('111.txt', 'w', encoding='utf-8') as fileN:
#         fileN.write('1213')
#         lst.append(fileN)
#     # file.close()

# with open('111.txt', 'w', encoding='utf-8') as fileN:
#     fileN.write('1213')
#     fileN.write('qwweq')
# print(fileN)

# import os
#
# with os.scandir(".") as entries:
#     for entry in entries:
#         print(entry.name, "->", entry.stat().st_size, "bytes")

# class Car:
#     model = "Audi"
#     engine = 1.6
#
# a = Car() -- екземпляр класа?
# b = Car()
# c = b
# print(a , b, c)
#
# class Person:
#     name = "Ivan"
#     age = 30

# class Car:
#     model = "Audi"
#     engine = 1.6
#
#     def drive():
#         print("let`s go")



# магічні методи

# class Cat:
#
#     def __init__(self, name, breed, age, color):
#         print("My cat is:", self, name, breed, age, color)
#         self.name = name
#         self.breed = breed
#         self.age = age
#         self.color = color
#
# Cat("Marry", "siam", 15, "red")
#
# jon = Cat("Jon", "siam", 7, "white")

# Class Point
# from math import sqrt
#
# class Point:
#
#     list_points = []
#
#     def __init__(self, coord_x=0, coord_y=0):
#         self.move_to(coord_x, coord_y)
#         Point.list_points.append(self)
#         print(Point.list_points)
#
#     def move_to(self, new_x, new_y):
#         self.x = new_x
#         self.y = new_y
#
#     def go_home(self):
#         self.move_to(0, 0)
#
#     def print_point(self):
#         print(f"Point with coord: {self.x},{self.y}")
#
#     def calc_distance(self, another_point):
#         if not isinstance(another_point, Point):
#             raise ValueError("Bad argument")
#
#         return sqrt((self.x - another_point.x)**2 + (self.y - another_point.y)**2)
#
#
# p1 = Point()
# p1.move_to(3,5)
# p2 = Point()
# p2.move_to(79,12)
#
# print(p1.calc_distance(p2))



# class Cat:
#     __shared_attr = {
#         'breed': 'pers',
#         'color': 'black'
#     }
#
#     def __init__(self):
#         self.__dict__ = Cat.__shared_attr


class BankAccount:

    def __init__(self, name, balance, passport):
        self.__name = name
        self.__balance = balance
        self.__passport = passport

    # def print_publick_data(self):
    #     print(self.name, self.balance, self.passport)

    def print_protected_data(self):
        print(self._name, self._balance, self._passport)

    def print_private_data(self):
        print(self.__name, self.__balance, self.__passport)


a1 = BankAccount("Nazar", 12321, "G131231")
a1.print_private_data()
print(a1.__name)









