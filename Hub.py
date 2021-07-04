import pygame as py
import os
import time
import random

py.init()  # get pygame ready because i'm going to use it
py.font.init()  # gets fonts ready because i'm going to use it

DISPLAY_SIZE = (750, 750)

DISPLAY = py.display.set_mode(DISPLAY_SIZE)
py.display.set_caption("space shooter")


""" -- Images -- """

# Enemy ships
RED_SPACE_SHIP = py.image.load("assets/pixel_ship_red_small.png")
GREEN_SPACE_SHIP = py.image.load("assets/pixel_ship_green_small.png")
BLUE_SPACE_SHIP = py.image.load("assets/pixel_ship_blue_small.png")

# Player ship
YELLOW_SPACE_SHIP = py.image.load("assets/pixel_ship_yellow.png")

# Lazers
RED_LASER = py.image.load("assets/pixel_laser_red.png")
GREEN_LASER = py.image.load("assets/pixel_laser_green.png")
BLUE_LASER = py.image.load("assets/pixel_laser_blue.png")
YELLOW_LASER = py.image.load("assets/pixel_laser_yellow.png")

# Background
BG = py.image.load("assets/background-black.png")
BG = py.transform.scale(BG, DISPLAY_SIZE)

""" -- Colors -- """
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


""" -- Classes -- """


class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = py.mask.from_surface(self.img)

    def draw(self, surface):
        DISPLAY.blit(self.img, (self.x, self.y))

    def move(self, vel):
        self.y += vel

    def off_screen(self, height):
        return self.y <= height and self.y >= 0

    def collision(self, obj):
        return collide(obj, self)  # is object overlapping with self


class Ship:
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self, surface):
        DISPLAY.blit(self.ship_img, (self.x, self.y))

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()


class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)  # this inherits all the things from Ship
        self.ship_img = YELLOW_SPACE_SHIP
        self.laser_img = YELLOW_LASER
        self.mask = py.mask.from_surface(self.ship_img)  # This is for pixel perfect collisions
        self.max_health = health  # What the player starts with is the max health they can have


class Enemy(Ship):
    COLOR_MAP = {"red": (RED_SPACE_SHIP, RED_LASER),
                 "green": (GREEN_SPACE_SHIP, GREEN_LASER),
                 "blue": (BLUE_SPACE_SHIP, BLUE_LASER)}

    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = py.mask.from_surface(self.ship_img)

    def move(self, vel):
        self.y += vel


def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y = obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None  # is obj1 overlapping obj2 and can't = None

def main():
    run = True
    FPS = 60  # checks events every fps
    clock = py.time.Clock()
    level = 0
    lives = 5
    player_speed = 5
    main_font = py.font.SysFont("comicsans", 50)
    lost_font = py.font.SysFont("comicsans", 70)

    enemies = []
    wave_length = 5
    enemy_vel = 5

    lost = False
    lost_count = 0


    player = Player(300, 650)

    def redraw_window():  # This is going to draw everything we need drawn
        DISPLAY.blit(BG, (0, 0))

        # draw text
        lives_label = main_font.render(f"lives: {lives}", 1, WHITE)
        level_label = main_font.render(f"level: {level}", 1, WHITE)
        DISPLAY.blit(lives_label, (10, 10))
        DISPLAY.blit(level_label, (DISPLAY_SIZE[0] - level_label.get_width() - 10, 10))

        # draw ships
        for enemy in enemies:
            enemy.draw(DISPLAY)

        player.draw(DISPLAY)

        if lost:
            lost_label = lost_font.render("You Lost", 1, RED)
            DISPLAY.blit(lost_label, (DISPLAY_SIZE[0]/2 - lost_label.get_width()/2, DISPLAY_SIZE[1]/2 - lost_label.get_height()/2))

        py.display.update()

    while run:
        clock.tick(FPS)

        redraw_window()

        if lives <= 0 or player.health <= 0:
            lost = True
            lost_count += 1

        if lost:
            if lost_count > FPS * 5:  # 60 fps = 1 second therefore its 3 seconds
                run = False
            else:
                continue  # don't do anything below go back to "while run"

        if len(enemies) == 0:
            level += 1
            wave_length += 5
            for i in range(wave_length):
                enemy = Enemy(random.randrange(50, DISPLAY_SIZE[0]-100), random.randrange(-1500, -100), random.choice(["red", "green", "blue"]))
                enemies.append(enemy)

        for event in py.event.get():
            if event.type == py.QUIT:
                run = False

        keys = py.key.get_pressed()
        if keys[py.K_a] and player.x - player_speed > 0:  # left
            player.x -= player_speed
        if keys[py.K_d] and player.x + player_speed + player.get_width() < DISPLAY_SIZE[0]:  # right
            player.x += player_speed
        if keys[py.K_s] and player.y + player_speed + player.get_height() < DISPLAY_SIZE[1]:  # down
            player.y += player_speed
        if keys[py.K_w] and player.y - player_speed > 0:  # up
            player.y -= player_speed

        for enemy in enemies[:]:  # [:] - he does that to make a copy of the list because he doesn't want to delete items from a list his using because it could cause problems
            enemy.move(enemy_vel)
            if enemy.y + enemy.get_height() > DISPLAY_SIZE[1]:
                lives -= 1
                enemies.remove(enemy)



main()





# lazy person needs to be supervised
# lazy person doesn't plan for the future
# lazy person sleeps a lot
# lazy people can't be counted on
# lazy people is wasteful
# lazy people always has an excuse
# lazy people have no ambition
# lazy people don't get promoted
# lazy people does not take care of things (his environment or items)
# lazy people will be poor
