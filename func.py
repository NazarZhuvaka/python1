from functools import total_ordering


def firstF(text):
    print(f"My first function in python {text}")

firstF("I`m in function!")

# {price:.2f} форматування виводу строк

def pretty_print(qty , item , price):
    print(f"{qty} {item} cost: ${price:.2f}")

pretty_print(price=1.881, qty=16, item="ananas" )

# def add_some(my_list=[]):
#     my_list.append("Something")
#     return my_list
#
# print(add_some())
# print(add_some())

def add_some1(my_list=None):
    if my_list is None:
        my_list = []
    my_list.append("Something_1")
    return my_list

print(add_some1())
# (bool(a) + bool(b))

# пакування кортежу
def avg(*args):
    total = 0
    for i in args:
        print(f"Index : {i}")
        total += i
        print(total)
    return total/len(args)

print(avg(35, 26, 12, ))

t = (1, 3, 1,)
print(avg(*t))

# Словник
def summm(**kwargs):
    print(kwargs)


