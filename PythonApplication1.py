from turtle import*
import keyboard
shape("turtle")
color("red")
step = 1;
w = 1
c = 0
while True:
    if keyboard.is_pressed('w'):
       forward(step)
    if keyboard.is_pressed('a'):
        left(10)
    if keyboard.is_pressed('d'):
        right(10)
    if keyboard.is_pressed('s'):
        left(180)
    if keyboard.is_pressed('z'):
        step = step + 1
    if keyboard.is_pressed('x'):
        step = step - 1
        if step <= 0:
            step = 0
    if keyboard.is_pressed('p'):
        w = w + 1
        width(w)
    if keyboard.is_pressed('o'):
        w = w - 1
        if w <= 0:
            w = w + 1
        width(w)
    if c<25 :
       pencolor(((c*10)/255, 0, (255-c*10)/255))
    if keyboard.is_pressed('c'):
        clearscreen()
        shape("turtle")
        pencolor(((c*10)/255, 0, (255-c*10)/255))
        width(w)
    if keyboard.is_pressed('m'):
        c = c + 1
        if c>25 :
            c = 25
    if keyboard.is_pressed('n'):
        c = c - 1
        if c < 0:
            c = 0
    if keyboard.is_pressed('q'):
        penup()
    if keyboard.is_pressed('e'):
        pendown()
