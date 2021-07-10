import pygame as py

py.init()

""" -- Variables -- """
# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


# Display
DISPLAY_WIDTH = 1150
DISPLAY_HEIGHT = 650

# Images
floor_img = py.image.load("../images/room_wooden_floor.png")
floor_img1 = py.image.load("../images/room_wooden_floor1.png")
wall_img = py.image.load("../images/room_walls.png")
wall_img1 = py.image.load("../images/room_walls1.png")
grass_img = py.image.load("../images/grass.png")
grass_img1 = py.image.load("../images/grass1.png")

tile_size = floor_img.get_width()


# Player (its not multi player its just multi clothes
p1 = py.image.load("../images/player.png")
p1.set_colorkey(WHITE)
p2 = py.image.load("../images/player2.png")
p2.set_colorkey(WHITE)
p3 = py.image.load("../images/player3.png")
p3.set_colorkey(WHITE)
p4 = py.image.load("../images/player4.png")
p4.set_colorkey(WHITE)

p_rect = py.Rect(100, 100, tile_size, tile_size)



# Game map
tile_rects = []
poke_rects = []
map_house = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1],
             [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
             [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
             [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 1],
             [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
             [1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1],
             [1, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
             [1, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
             [1, 3, 3, 2, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
             [1, 3, 3, 2, 3, 3, 3, 3, 2, 3, 3, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
             [1, 3, 3, 2, 3, 3, 3, 3, 2, 3, 3, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# ---------------------------

display = py.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
py.display.set_caption("Big Boy Game")


def collision_test(p_rect, tile_rects):
    hit_list = []
    for tile in tile_rects:
        if p_rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list


def move(p_rect, movement, tile_rects):
    # first test x
    p_rect.x += movement[0]
    hit_list = collision_test(p_rect, tile_rects)
    for tile in hit_list:
        if movement[0] > 0:
            p_rect.right = tile.left
        elif movement[0] < 0:
            p_rect.left = tile.right

    p_rect.y += movement[1]
    hit_list = collision_test(p_rect, tile_rects)
    for tile in hit_list:
        if movement[1] > 0:
            p_rect.bottom = tile.top
        if movement[1] < 0:
            p_rect.top = tile.bottom

    return p_rect


# -------------------- Main game function -------------------------------

def main_game():
    game_ongoing = True

# player
    player_speed = 2
    moving_right = False
    moving_left = False
    moving_up = False
    moving_down = False

# Game map
    def map_generate():
        y = 0
        for row in map_house:
            x = 0
            for tile in row:
                if tile == 1:
                    display.blit(wall_img, (x * tile_size, y * tile_size))
                    tile_rects.append(py.Rect(x * tile_size, y * tile_size, tile_size, tile_size))
                if tile == 2:
                    display.blit(floor_img, (x * tile_size, y * tile_size))
                if tile == 3:
                    display.blit(grass_img, (x * tile_size, y * tile_size))
                    poke_rects.append(py.Rect(x * tile_size, y * tile_size, tile_size, tile_size))
                x += 1
            y += 1

    def current_player():  # have more work to do here to change the clothes
        return p4

    def update_display():

        map_generate()
        display.blit(current_player(), (p_rect.x, p_rect.y))
        py.display.update()

    def movements():
        movement = [0, 0]  # not location, x and y movement

        if moving_right:
            movement[0] += player_speed
        if moving_left:
            movement[0] -= player_speed
        if moving_up:
            movement[1] -= player_speed
        if moving_down:
            movement[1] += player_speed

        player_rect = move(p_rect, movement, tile_rects)

# ------------------------ Main loop ------------------------------------
    while game_ongoing:

        movements()
        update_display()

        for event in py.event.get():
            if event.type == py.QUIT:
                game_ongoing = False

            if event.type == py.KEYDOWN:
                if event.key == py.K_UP:
                    moving_up = True
                if event.key == py.K_DOWN:
                    moving_down = True
                if event.key == py.K_RIGHT:
                    moving_right = True
                if event.key == py.K_LEFT:
                    moving_left = True

            if event.type == py.KEYUP:
                if event.key == py.K_UP:
                    moving_up = False
                if event.key == py.K_DOWN:
                    moving_down = False
                if event.key == py.K_RIGHT:
                    moving_right = False
                if event.key == py.K_LEFT:
                    moving_left = False


main_game()

# Start with the pause menu
