import turtle

t = turtle.Turtle()
##t.forward(100)
##t.left(45)
##t.forward(100)
##t.right(90)
##t.forward(100)

##t.color("black","brown")
##t.begin_fill()
##for i in range(4):
##    t.forward(100)
##    t.left(90)
##
##
##t.right(90)
##t.penup()
##t.forward(100)
##t.pendown()
##
##for i in range(4):
##    t.forward(100)
##    t.left(90)
##    
##t.end_fill()
def UpDireita(a):
    for i in range(a):
        t.forward(10)
        t.right(2)
def UpEsquerda(a):
    for i in range(a):
        t.forward(10)
        t.left(2)

def Serrado(a):
    for i in range(a):
        t.right(90)
        t.forward(7)
        t.left(90)
        t.forward(7)

def Serrado2(a):
    for i in range(a):
        t.right(90)
        t.forward(7)
        t.left(90)
        t.forward(10)

def Serrado1():
    t.right(90)
    t.forward(5)
    t.left(90)
    t.forward(5)

def Serrado12():
    t.left(90)
    t.forward(5)
    t.right(90)
    t.forward(5)

def UpDireitaSerrada(a):
    for i in range(a):
        t.forward(10)
        t.right(4)
        Serrado1()

def UpEsquerdaSerrada(a):
    for i in range(a):
        t.forward(10)
        t.left(4)
        Serrado12()


turtle.Screen().bgcolor("red")
posicao = t.pos()
t.color("#ecf0f1","#2c3e50")
t.begin_fill()
turtle.Screen().setup(width=0.99, height=0.99)
t.pensize(10)
t.forward(20)


UpEsquerda(20)
t.left(220)
UpDireita(8)
UpDireitaSerrada(12)

t.setheading(90)
t.left(20)
t.forward(30)
t.setheading(90)

t.forward(45)
t.end_fill()

t.color("#2c3e50","#ecf0f1")


t.pensize(10)
t.penup()
t.goto(posicao)
t.pendown()
t.color("#2c3e50","#ecf0f1")
t.begin_fill()
t.setheading(180)
t.forward(20)
UpDireita(20)
t.right(220)
UpEsquerda(8)
UpEsquerdaSerrada(12)
t.setheading(90)
t.right(20)
t.forward(30)
t.setheading(90)

t.forward(45)
t.end_fill()
t.hideturtle()


cv = turtle.getcanvas()
cv.postscript(file="file_name.ps", colormode='color')
turtle.done()

