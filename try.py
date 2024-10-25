# Перехват виключень
# def fetcher(obj, ind):
#     return obj[ind]
#
#
# class MyException(Exception):
#     pass
#
# if __name__ == "__main__":
#     try:
#         x = input("input string: ")
#         assert len(x) < 20 , "too long object ..."
#         i = int(input("input index please: "))
#         print(fetcher(x ,i))
#         # if len(x) > 20:
#         #     raise MyException
#     except IndexError:
#         print("asd")


#__

# file = open('111.txt', 'r' encoding='utf-8')
# file = open('111.txt', 'w', encoding='utf-8')
# file = open('111.txt', 'a', encoding='utf-8')
# file = open('111.txt', 'a+', encoding='utf-8')

# s = file.readlines()

# print(s)
#
# print(file.read(5))
# file.seek(0)
# print(file.readline())
# file.seek(0)
# print(file.read(2))

# for row in file:
#     print(row)
    # for letter in row:
    #     print(letter)


# file.write("111111sda\n")
# file.write("sda\n")
# file.write("sda\n")

# file = open('111.txt', 'r', encoding='utf-8')
# file.write("I am new in Python\n")
# file.write("I am new in Java\n")
# print(file.readline())
#
# for row in file:
#     print(row)
#
# file.seek(0)
# s = file.readlines()
# print(s)

# обработка
# помилка

# file.close()

# file = open('func.py')
#
# for row in file:
#     print(row)
