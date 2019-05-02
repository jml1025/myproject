# Import Turtle
import random
import turtle
import time
import winsound


score = 0
lives = 3
font = ("Courier", 24, "normal")

# set up main window
wn = turtle.Screen()
wn.title("HUFS SPACE ADVENTURE GAME By Ishanga & JungMin")
wn.setup(width=800, height=600)
wn.bgpic("BG.gif")
wn.tracer(0)

# Shape Register
wn.register_shape("diamond.gif")
wn.register_shape("rock2.gif")
wn.register_shape("spaceship.gif")

# Add player
player = turtle.Turtle()
player.penup()
player.speed(0)
player.shape("spaceship.gif")
player.goto(0, -250)
player.direction = "stop"
player.place= 0

# Create a list of gems
gemList = []
# Add a gem
for _ in range(3):
    gem = turtle.Turtle()
    gem.penup()
    gem.speed(0)
    gem.shape("diamond.gif")
    gem.speed = random.randint(1, 3)
    gem.goto(random.randint(-380, 380), 250)
    gemList.append(gem)

# Create a list of rocks
rockList = []
# Add a rock
for _ in range(6):
    rock = turtle.Turtle()
    rock.penup()
    rock.speed(0)
    rock.shape("rock2.gif")
    rock.speed = random.randint(1, 3)
    rock.goto(random.randint(-380, 380), 250)
    rockList.append(rock)

# Add Score to screen
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.color("black")
pen.goto(0, 260)
pen.write("Score : {}   Lives : {}".format(score, lives), align="center", font=font)


# Set key press
def go_left():
    player.direction = "left"


def go_right():
    player.direction = "right"


def stop_now():
    player.direction = "stop"


# Game over
def stop_game(s):
    game_over = turtle.Turtle()
    game_over.hideturtle()
    game_over.penup()
    game_over.color("red")
    game_over.goto(0, 0)
    game_over.write("Game Over! Your Score : {}".format(s), align="center", font=font)


# Get key press
wn.listen()
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")
wn.onkeypress(stop_now, "Down")

start = 0
# Main game loop
while True:
    # Update window
    wn.update()
    if start == 0:
        pen.goto(0, 0)
        pen.color("blue")
        pen.write("Welcome to HUFS SPACE ADVENTURE.", align="center", font=font)
        time.sleep(2)
        pen.clear()
        pen.color("black")
        pen.goto(0, 260)
        pen.write("Score : {}   Lives : {}".format(score, lives), align="center", font=font)
        start = 1

    if player.direction == "left":
        x = player.xcor()
        x -= 1
        player.setx(x)

    if player.direction == "right":
        x = player.xcor()
        x += 1
        player.setx(x)

    if player.direction == "stop":
        player.setx(player.xcor())

    # Move gems
    for gem in gemList:
        gem.sety(gem.ycor() - gem.speed)

        # Check off screen
        if gem.ycor() < -300:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            gem.goto(x, y)

        # Check collision
        if gem.distance(player) < 20:
            winsound.PlaySound("bloop_x.wav", winsound.SND_ASYNC)
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            gem.goto(x, y)
            score += 10
            pen.clear()
            pen.write("Score : {}   Lives : {}".format(score, lives), align="center", font=font)

    # Move rocks
    for rock in rockList:
        rock.sety(rock.ycor() - rock.speed)

        # Check off screen
        if rock.ycor() < -300:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            rock.goto(x, y)

        # Check collision
        if rock.distance(player) < 20:
            winsound.PlaySound("blip.wav", winsound.SND_ASYNC)
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            rock.goto(x, y)
            player.goto(player.xcor(), player.ycor() + 20)
            time.sleep(0.2)
            lives -= 1
            pen.clear()
            pen.write("Score : {}   Lives : {}".format(score, lives), align="center", font=font)

    if lives == 0:
        stop_game(score)
        break

wn.mainloop()