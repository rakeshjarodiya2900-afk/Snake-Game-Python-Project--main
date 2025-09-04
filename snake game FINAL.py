import turtle
import random
import time

delay = 0.1
score = 0
highest_score = 0

# Snake bodies
bodies = []

# Getting a screen
s = turtle.Screen()
s.title("Snake Game")
s.bgcolor("light blue")
s.setup(width=600, height=600)
# Create snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.fillcolor("red")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("yellow")
food.fillcolor("green")
food.penup()
food.ht()
food.goto(random.randint(-290, 290), random.randint(-290, 290))
food.st()

# Score board
sb = turtle.Turtle()
sb.shape("square")
sb.fillcolor("black")
sb.penup()
sb.ht()
sb.goto(-250, -250)
sb.write("Score: 0 | Highest Score: 0")

def move_up():
    if head.direction != "down":
        head.direction = "up"

def move_down():
    if head.direction != "up":
        head.direction = "down"

def move_left():
    if head.direction != "right":
        head.direction = "left"

def move_right():
    if head.direction != "left":
        head.direction = "right"

def move_stop():
    head.direction = "stop"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Event handling
s.listen()
s.onkey(move_up, "Up")
s.onkey(move_down, "Down")
s.onkey(move_left, "Left")
s.onkey(move_right, "Right")
s.onkey(move_stop, "space")


def increase_speed():
    global delay
    if score > 0 and score % 5000000000 == 0:
        delay -= 0.015

# Main loop
while True:
    s.update()
    if head.xcor() > 290:
        head.setx(-290)
    if head.xcor() < -290:
        head.setx(290)
    if head.ycor() > 290:
        head.sety(-290)
    if head.ycor() < -290:
        head.sety(290)

    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
        new_body = turtle.Turtle()
        new_body.speed(0)
        new_body.shape("square")
        new_body.color("red")
        new_body.fillcolor("black")
        new_body.penup()
        bodies.append(new_body)
        score += 10
        delay -= 0.001
        if score > highest_score:
            highest_score = score
        sb.clear()
        sb.write("Score: {} Highest Score: {}".format(score, highest_score))
    
    for index in range(len(bodies) - 1, 0, -1):
        x = bodies[index - 1].xcor()
        y = bodies[index - 1].ycor()
        bodies[index].goto(x, y)
    
    if len(bodies) > 0:
        x = head.xcor()
        y = head.ycor()
        bodies[0].goto(x, y)
    
    move()
    
    for body in bodies:
        if body.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            
            for body in bodies:
                body.ht()
            bodies.clear()
            
            score = 0
            delay = 0.1
            
            sb.clear()
            sb.write("Score: {} Highest Score: {}".format(score, highest_score))
    increase_speed()
    time.sleep(delay)
