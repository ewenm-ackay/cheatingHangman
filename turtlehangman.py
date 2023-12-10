import turtle
t = turtle.Turtle()
t.ht()
t.pensize(2)
length = 5

# DrawHead draws the head of the hanging man.
def DrawHead():
    t.speed(0)
    for i in range(90):
        t.fd(length)
        t.lt(360//90)

# DrawBody draws the body of the hanging man.
def DrawBody():
    t.speed(2)
    t.rt(90)
    t.fd(150)

# DrawLeftArm draws the left arm of the hanging man.
def DrawLeftArm():
    t.speed(2)
    t.lt(10)
    t.fd(60)
    
# DrawRightArm draws the right arm of the hanging man.
def DrawRightArm():
    t.speed(2)
    t.lt(170)
    t.fd(60)

# DrawLeftLeg draws the left leg of the hanging man.
def DrawLeftLeg():
    t.speed(2)
    t.rt(45)
    t.fd(60)

# DrawRightLeg draws the right leg of the hanging man.
def DrawRightLeg():
    t.speed(2)
    t.rt(135)
    t.fd(60)

# DrawToes draws each toe of the hanging man.
def DrawToes():
    t.speed(2)
    for i in range(5):
        t.fd(30)
        t.bk(30)
        t.rt(20)
        
# DrawFingers draws each finger of the hanging man.
def DrawFingers():
    t.speed(2)
    for i in range(5):
        t.fd(30)
        t.bk(30)
        t.rt(20)

if __name__ == '__main__':
    DrawToes()
    turtle.done()
