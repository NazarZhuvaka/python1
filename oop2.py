# Поліморфізм
from turtledemo.penrose import start

from example import figure
from func import summm


# class Rectangle:
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def get_rect_area(self):
#         return self.a * self.b
#
# class Square:
#
#     def __init__(self, a):
#         self.a = a
#
#     def get_sq_area(self):
#         return self.a**2

# __call__

# class Counter:
#
#     def __init__(self):
#         self.counter = 0
#         self.summa = 0
#         self.length = 0
#         print("init object", self)
#
#     def __call__(self, *args, **kwargs):
#         self.counter += 1
#         self.summa += sum(args)
#         self.length += len(args)
#         print(f"object called {self.counter} times")
#
#     def avarege(self):
#         return self.summa / self.length
#
# a = Counter()
# a(3, 4 ,5,1)

# from time import perf_counter
# class Timer:
#     def __init__(self, func):
#         self.fn = func
#
#     def __call__(self, *args, **kwargs):
#         start = perf_counter()
#         print("func called", self.fn.__name__)
#         result = self.fn(*args, **kwargs)
#         finish = perf_counter()
#         print(f"func finished in{finish - start}", self.fn.__name__)
#         return result
#
# @Timer
# def factorial(n):
#     pr = 1
#     for i in range(1, n + 1):
#         pr *= i
#     return pr
#
# def fib(n):
#     if n<=2:
#         return 1
#     return fib(n-1) + fib(n-2)

# factorial = Timer(factorial) = @Timer? decorator

# __getitem__, __setitem__, __delitem__


# class Vector:
#
#     def __init__(self, *args):
#         self.values = list(args)
#
#     def __repr__(self):
#         return str(self.values)
#
#     # def __getitem__(self, item):
#     #     if 0<=item<len(self.values):
#     #         return self.values[item]
#     #     else:
#     #         raise IndexError("Index out of list")
#
#     def __getitem__(self, item):
#         if 1<=item<=len(self.values):
#             return self.values[item-1]
#         else:
#             raise IndexError("Index out of list")
#
#     # def __setitem__(self, key, value):
#     #     if 0<=key<len(self.values):
#     #         self.values[key] = value
#     #     else:
#     #         raise IndexError("Index out of list")
#
#     def __setitem__(self, key, value):
#         if 1<=key<=len(self.values):
#             self.values[key] = value
#         elif key>len(self.values):
#             diff = key - len(self.values)
#             self.values.extend([0]*diff)
#             self.values[key] = value
#         else:
#             raise IndexError("Index out of list")
#
#     def __delitem__(self, key):
#         if 0<=key<len(self.values):
#             del self.values[key]
#         else:
#             raise IndexError("Index out of list")
#
# v1 = Vector(1,2,4,123123)
# print(v1.values)

# __iter__ , __next__