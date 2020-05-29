
from shapes import Triangle, Rectangle, Oval, Paper

rect1 = Rectangle()
rect2 = Rectangle()

rect1.set_width(200)
rect1.set_height(100)
rect1.set_color("blue")


rect2.set_width(50)
rect2.set_height(150)
rect2.set_color("yellow")
rect2.set_x(0)
rect2.set_y(0)


rect1.draw()
rect2.draw()

Paper.display()
