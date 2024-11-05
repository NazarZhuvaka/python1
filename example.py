from oop2 import Rectangle, Square

rect1 = Rectangle(3, 4)
rect2 = Rectangle(12, 5)

print(rect1.get_rect_area(),
      rect2.get_rect_area())

sq1 = Square(5)
sq2 = Square(7)
print(sq1.get_sq_area(),
      sq2.get_sq_area())

figures = [rect1, rect2, sq1, sq2]

for figure in figures:
    print()