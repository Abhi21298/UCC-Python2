from graphics import *
from random import randrange
PICWIDTH = 600
PICHEIGHT = 600

win = GraphWin(title = "Studio 6507", width = PICWIDTH, height = PICHEIGHT) 
win.setCoords(0, 0, PICWIDTH - 1, PICHEIGHT - 1)
win.setBackground("white")

color1_cords = [randrange(0,255,1) for i in range(3)]
color2_cords = [randrange(0,255,1) for i in range(3)]
color3_cords = [randrange(0,255,1) for i in range(3)]
r1,g1,b1 = color1_cords
r2,g2,b2 = color2_cords
r3,g3,b3 = color3_cords
col1 = color_rgb(r1,g1,b1)
col2 = color_rgb(r2,g2,b2)
col3 = color_rgb(r3,g3,b3)

rect1 = Rectangle(Point(0, 400), Point(150, 595))
rect1.setFill(col2)
rect1.setWidth(10)
rect1.draw(win)
rect2 = Rectangle(Point(0, 155), Point(150, 395))
rect2.setFill(col2)
rect2.setWidth(10)
rect2.draw(win)
rect3 = Rectangle(Point(152, 152), Point(600, 600))
rect3.setFill(col3)
rect3.setWidth(10)
rect3.draw(win)
rect4 = Rectangle(Point(0, 0), Point(150, 150))
rect4.setFill(col1)
rect4.setWidth(10)
rect4.draw(win)
rect5 = Rectangle(Point(150, 0), Point(550, 150))
rect5.setFill(col2)
rect5.setWidth(10)
rect5.draw(win)
rect6 = Rectangle(Point(550, 0), Point(597, 75))
rect6.setFill(col3)
rect6.setWidth(10)
rect6.draw(win)
rect7 = Rectangle(Point(550, 75), Point(597, 150))
rect7.setFill(col2)
rect7.setWidth(10)
rect7.draw(win)
win.getMouse()
win.close()  