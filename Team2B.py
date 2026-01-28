import turtle
import tkinter.font as tkfont  

screen = turtle.Screen()
screen.bgcolor("white")
screen.title("UniSoc Turtle Logo")

screen.setup(1000, 600)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)


TEAL = "#39c6c3"
PURPLE = "#5e2b7e"
BLUE = "#1E90FF"
WHITE = "white"


def filled_circle(x, y, r, color):
    t.penup()
    t.goto(x, y - r)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(r)
    t.end_fill()


def filled_square(x, y, size, color):
    t.penup()
    t.goto(x - size/2, y + size/2)  
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.right(90)
    t.end_fill()


def filled_speech_bubble(x, y, r, color, tail_dir='right'):
   
    t.penup()
    t.goto(x, y - r)
    t.pendown()
    t.fillcolor(color)
    t.pencolor(color)
    t.begin_fill()
    t.circle(r)
    t.end_fill()

    tail_w = r * 0.95
    tail_h = r * 0.8
    base_x_offset = r * 0.55
    base_y = y - r * 0.55
    if tail_dir == 'right':
        p1 = (x + base_x_offset, base_y - tail_h * 0.3)
        p3 = (x + base_x_offset, base_y + tail_h * 0.3)
        p2 = (x + base_x_offset + tail_w, base_y)
    else:
        p1 = (x - base_x_offset, base_y - tail_h * 0.3)
        p3 = (x - base_x_offset, base_y + tail_h * 0.3)
        p2 = (x - base_x_offset - tail_w, base_y)

    t.penup()
    t.goto(p1)
    t.pendown()
    t.fillcolor(color)
    t.pencolor(color)
    t.begin_fill()
    t.goto(p2)
    t.goto(p3)
    t.goto(p1)
    t.end_fill()

    t.pencolor(color)

filled_circle(0, 40, 40, WHITE)

tk_font = tkfont.Font(root=screen._root, family="Arial", size=120, weight="bold")
uni_w = tk_font.measure("Uni")
soc_w = tk_font.measure("Soc")

uni_x = -soc_w / 2
soc_x = uni_w / 2
text_y = -40

t.penup()
t.goto(uni_x, text_y)
t.color(PURPLE)
t.write("Uni", align="center", font=("Arial", 120, "bold"))

t.penup()
t.goto(soc_x, text_y)
t.color(BLUE)
t.write("Soc", align="center", font=("Arial", 120, "bold"))


filled_speech_bubble(-360, -40, 60, BLUE, tail_dir='right')

filled_speech_bubble(380, -40, 55, PURPLE, tail_dir='left')

turtle.done()
