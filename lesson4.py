a = "Hello world"
result = ""

for char in a:
    if char == "o":
        result = result + "a"
    elif char == "l":
        result = result + "e"
    else:
        result = result + char

print(result)

