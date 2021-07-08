# Dice game
import random
import pygame as py

py.init()

dice_options = [1, 2, 3, 4, 5, 6, 7]

""" -- variables -- """
# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Dimensions
DISPLAY_WIDTH = 500
DISPLAY_HEIGHT = 500

# Images
p1_img = py.image.load("images/X.png")
p1_img = py.transform.scale(p1_img, (50, 50))
p2_img = py.image.load("images/O.png")
p2_img = py.transform.scale(p2_img, (50, 50))

p1_rect = py.Rect(50, 50, 50, 50)
p2_rect = py.Rect(50, 200, 50, 50)
button_rect = py.Rect(200, 400, 100, 50)

speed = 5


DISPLAY = py.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
py.display.set_caption("Dice race game")

button_1 = py.draw.rect(DISPLAY, GREEN, button_rect)

click = False

def main_game():
    game_on = True


    def boundaries_drawn():
        line1 = py.draw.line(DISPLAY, WHITE, (0, DISPLAY_HEIGHT//3), (DISPLAY_WIDTH, DISPLAY_HEIGHT//3), 1)
        line2 = py.draw.line(DISPLAY, WHITE, (0, DISPLAY_HEIGHT//1.5), (DISPLAY_WIDTH, DISPLAY_HEIGHT//1.5), 1)


    def players_draw():
        DISPLAY.blit(p1_img, (p1_rect.x, p1_rect.y))
        DISPLAY.blit(p2_img, (p2_rect.x, p2_rect.y))
        button_1 = py.draw.rect(DISPLAY, GREEN, button_rect)


    def display_update():
        DISPLAY.fill(BLACK)

        players_draw()
        boundaries_drawn()
        py.display.update()

    def move_time():
        p1_roll = (random.choice(dice_options) - 1) * 10
        p2_roll = (random.choice(dice_options) - 1) * 10
        p1_rect.x += p1_roll
        p2_rect.x += p2_roll

    while game_on:
        display_update()


        mx, my = py.mouse.get_pos()

        if button_1.collidepoint((mx, my)):
            if click:
                move_time()

        if p1_rect.x >= (DISPLAY_WIDTH - p1_rect.width):
            print("Player 1 wins!")
            p1_rect.x = (DISPLAY_WIDTH - p1_rect.width) - 1
            p2_rect.x = 10
        if p2_rect.x >= (DISPLAY_WIDTH - p2_rect.width):
            print("Player 2 wins!")
            p2_rect.x = (DISPLAY_WIDTH - p2_rect.width) - 1
            p1_rect.x = 10


        click = False
        for event in py.event.get():
            if event.type == py.QUIT:
                game_on = False

            if event.type == py.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True


main_game()

