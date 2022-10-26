import turtle

win=turtle.Screen()

def curve():
    for i in range(200):
        heart.right(1)
        heart.forward(1)

heart=turtle.Turtle()

heart.fillcolor("red")
heart.begin_fill()
heart.left(140)
heart.forward(120)
curve()
heart.left(125)
curve()
heart.forward(120)
heart.end_fill()
heart.hideturtle()
turtle.done()




win.mainloop()
