import pygame as pyg
from CarNN.game.car import Car

# settings
SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 1080
BG_COLOUR = (0, 0, 0)

# initialize the display window
pyg.display.init()
window = pyg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pyg.display.set_caption("Self-Learning AI Simulation")

# initialize game variables
all_sprites = pyg.sprite.Group()
car = Car(500, 500, 0)
all_sprites.add(car)


# main loop
run = True
while run:
    turn = 0
    acceleration = 0

    keys = pyg.key.get_pressed()
    if keys[pyg.K_RIGHT]:
        turn = 1
    elif keys[pyg.K_LEFT]:
        turn = -1
    if keys[pyg.K_UP]:
        acceleration = 0.5
    elif keys[pyg.K_DOWN]:
        acceleration = -0.25

    car.update(turn, acceleration)
    window.fill(BG_COLOUR)
    all_sprites.draw(window)
    pyg.display.update()

    # stop loop if we want to quit
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            run = False
            break
    pyg.time.wait(6)
