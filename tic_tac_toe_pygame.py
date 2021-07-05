# Tic tac toe
import random
import sys
import pygame as py
import time


""" -- globals -- """
GAME_ON = True


a = 1
b = 2
c = 3
d = 4
e = 5
f = 6
g = 7
h = 8
i = 9
optional_choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# player input
def p1_move():
    global a, b, c, d, e, f, g, h, i
    correct_move = False

    while not correct_move:
        move = int(input("Your turn to play. Input number 1 - 9: "))
        if move in optional_choices:
            correct_move = True
        else:
            pass

    if move == 1:
        a = "X"
        optional_choices.remove(1)
        print(a)
    elif move == 2:
        b = "X"
        optional_choices.remove(2)
    elif move == 3:
        c = "X"
        optional_choices.remove(3)
    elif move == 4:
        d = "X"
        optional_choices.remove(4)
    elif move == 5:
        e = "X"
        optional_choices.remove(5)
    elif move == 6:
        f = "X"
        optional_choices.remove(6)
    elif move == 7:
        g = "X"
        optional_choices.remove(7)
    elif move == 8:
        h = "X"
        optional_choices.remove(8)
    elif move == 9:
        i = "X"
        optional_choices.remove(9)

# pc input
def pc_move():
    global a, b, c, d, e, f, g, h, i

    pc_choosing = True
    while pc_choosing:
        pc_choice = random.choice(optional_choices)
        pc_choosing = False

        if pc_choice == 1:
            a = "O"
            optional_choices.remove(1)
            print(a)
        elif pc_choice == 2:
            b = "O"
            optional_choices.remove(2)
        elif pc_choice == 3:
            c = "O"
            optional_choices.remove(3)
        elif pc_choice == 4:
            d = "O"
            optional_choices.remove(4)
        elif pc_choice == 5:
            e = "O"
            optional_choices.remove(5)
        elif pc_choice == 6:
            f = "O"
            optional_choices.remove(6)
        elif pc_choice == 7:
            g = "O"
            optional_choices.remove(7)
        elif pc_choice == 8:
            h = "O"
            optional_choices.remove(8)
        elif pc_choice == 9:
            i = "O"
            optional_choices.remove(9)
    print("pc moves...")

# board
def board_show():
    board = f"{a} | {b} | {c}\n" \
            f"{d} | {e} | {f}\n" \
            f"{g} | {h} | {i}"
    print(board)




# turns

# check for win
# def winner_check():
#     # check winning options
#     def horizontal_win():
#         if a == b == c:
#             wining_player = a
#             winner(wining_player)
#         elif d == e == f:
#             wining_player = d
#             winner(wining_player)
#         elif g == h == i:
#             wining_player = g
#             winner(wining_player)
#         else:
#             pass
#
#     def vertical_win():
#         if a == d == g:
#             wining_player = a
#             winner(wining_player)
#         elif b == e == f:
#             wining_player = e
#             winner(wining_player)
#         elif c == f == i:
#             wining_player = c
#             winner(wining_player)
#         else:
#             pass
#
#     def diagonal_win():
#         if a == e == i:
#             wining_player = a
#             winner(wining_player)
#         elif c == e == g:
#             wining_player = c
#             winner(wining_player)
#         else:
#             pass
#
#     horizontal_win()
#     vertical_win()
#     diagonal_win()
#
#     # if hor_win is None and vert_win and None and diag_win is None:
#     #     pass
#     #
#     # elif hor_win[0] or vert_win[0] or diag_win[0]:
#     #     if hor_win[0]:
#     #         if hor_win[1] == "X":
#     #             print("You are the winner!")
#     #             sys.exit()
#     #         else:
#     #             print("PC is the winner")
#     #             sys.exit()
#     #     elif vert_win[0]:
#     #         if vert_win[1] == "X":
#     #             print("You are the winner!")
#     #             sys.exit()
#     #         else:
#     #             print("PC is the winner")
#     #             sys.exit()
#     #     elif diag_win[0]:
#     #         if diag_win[1] == "X":
#     #             print("You are the winner!")
#     #             sys.exit()
#     #         else:
#     #             print("PC is the winner")
#     #             sys.exit()



# mainloop
# def game_running():
#
#     while GAME_ON:
#         p1_move()
#         board_show()
#         winner_check()
#         pc_move()
#         board_show()
#         winner_check()

# pygame time

py.init()

WIDTH = 600
HEIGHT = 600

DISPLAY = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption("Tic Tac Toe")


""" -- Images -- """
x_img = py.image.load("images/X.png")
o_img = py.image.load("images/O.png")
x_img = py.transform.scale(x_img, (WIDTH//3, HEIGHT//3))
o_img = py.transform.scale(o_img, (WIDTH//3, HEIGHT//3))


""" -- Colors -- """
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


""" -- Variables -- """
clock = py.time.Clock()
FPS = 60
turn = 1
locations = {"one": "", "two": "", "three": "", "four": "", "five": "", "six": "", "seven": "",
             "eight": "", "nine": ""}

""" -- Square Location -- """
s1 = [0, WIDTH//3, 0, HEIGHT//3]
s2 = [WIDTH//3, WIDTH//1.5, 0, HEIGHT//3]
s3 = [WIDTH//1.5, WIDTH, 0, HEIGHT//3]
s4 = [0, WIDTH//3, HEIGHT//3, HEIGHT//1.5]
s5 = [WIDTH//3, WIDTH//1.5, HEIGHT//3, HEIGHT//1.5]
s6 = [WIDTH//1.5, WIDTH, HEIGHT//3, HEIGHT//1.5]
s7 = [0, WIDTH//3, HEIGHT//1.5, HEIGHT]
s8 = [WIDTH//3, WIDTH//1.5, HEIGHT//1.5, HEIGHT]
s9 = [WIDTH//1.5, WIDTH, HEIGHT//1.5, HEIGHT]



def winner_check():
    # check winning options
    def horizontal_win():
        if locations["one"] == locations["two"] == locations["three"] != "":
            wining_player = a
            winner(wining_player)
        elif locations["four"] == locations["five"] == locations["six"] != "":
            wining_player = d
            winner(wining_player)
        elif locations["seven"] == locations["eight"] == locations["nine"] != "":
            wining_player = g
            winner(wining_player)
        else:
            pass

    def vertical_win():
        if locations["one"] == locations["four"] == locations["seven"] != "":
            wining_player = a
            winner(wining_player)
        elif locations["two"] == locations["five"] == locations["eight"] != "":
            wining_player = e
            winner(wining_player)
        elif locations["three"] == locations["six"] == locations["nine"] != "":
            wining_player = c
            winner(wining_player)
        else:
            pass

    def diagonal_win():
        if locations["one"] == locations["five"] == locations["nine"] != "":
            wining_player = a
            winner(wining_player)
        elif locations["three"] == locations["five"] == locations["seven"] != "":
            wining_player = c
            winner(wining_player)
        else:
            pass

    horizontal_win()
    vertical_win()
    diagonal_win()


# win/lose
def winner(turn):
    global GAME_ON
    py.display.update()
    time.sleep(2)
    if turn == 1:
        winner_img = py.transform.scale(x_img, (WIDTH, HEIGHT))
        DISPLAY.blit(winner_img, (0, 0))
        py.display.update()
        time.sleep(2)
        GAME_ON = False
    if turn == 0:
        winner_img = py.transform.scale(o_img, (WIDTH, HEIGHT))
        DISPLAY.blit(winner_img, (0, 0))
        py.display.update()
        time.sleep(2)
        GAME_ON = False

def game_lines():
    line1 = py.draw.line(DISPLAY, WHITE, (WIDTH//3, 0), (WIDTH//3, HEIGHT))
    line2 = py.draw.line(DISPLAY, WHITE, (WIDTH//1.5, 0), (WIDTH//1.5, HEIGHT))
    line3 = py.draw.line(DISPLAY, WHITE, (0, HEIGHT//3), (WIDTH, HEIGHT//3))
    line4 = py.draw.line(DISPLAY, WHITE, (0, HEIGHT//1.5), (WIDTH, HEIGHT//1.5))


def who_turn():
    global turn
    turn += 1
    turn = turn % 2
    return turn


def mouse_pressed():
    mouse_location = py.mouse.get_pos()
    turn = who_turn()

    if s1[0] <= mouse_location[0] <= s1[1] and s1[2] <= mouse_location[1] <= s1[3]:  # square 1
        if 1 in optional_choices and turn == 0:
            locations["one"] = "a"
            optional_choices.remove(1)
        if 1 in optional_choices and turn == 1:
            locations["one"] = "b"
            optional_choices.remove(1)
        else:
            pass
    if s2[0] <= mouse_location[0] <= s2[1] and s2[2] <= mouse_location[1] <= s2[3]:  # square 1
        if 2 in optional_choices and turn == 0:
            locations["two"] = "a"
            optional_choices.remove(2)
        if 2 in optional_choices and turn == 1:
            locations["two"] = "b"
            optional_choices.remove(2)
        else:
            pass
    if s3[0] <= mouse_location[0] <= s3[1] and s3[2] <= mouse_location[1] <= s3[3]:  # square 1
        if 3 in optional_choices and turn == 0:
            locations["three"] = "a"
            optional_choices.remove(3)
        if 3 in optional_choices and turn == 1:
            locations["three"] = "b"
            optional_choices.remove(3)
        else:
            pass
    if s4[0] <= mouse_location[0] <= s4[1] and s4[2] <= mouse_location[1] <= s4[3]:  # square 1
        if 4 in optional_choices and turn == 0:
            locations["four"] = "a"
            optional_choices.remove(4)
        if 4 in optional_choices and turn == 1:
            locations["four"] = "b"
            optional_choices.remove(4)
        else:
            pass
    if s5[0] <= mouse_location[0] <= s5[1] and s5[2] <= mouse_location[1] <= s5[3]:  # square 1
        if 5 in optional_choices and turn == 0:
            locations["five"] = "a"
            optional_choices.remove(5)
        if 5 in optional_choices and turn == 1:
            locations["five"] = "b"
            optional_choices.remove(5)
        else:
            pass
    if s6[0] <= mouse_location[0] <= s6[1] and s6[2] <= mouse_location[1] <= s6[3]:  # square 1
        if 6 in optional_choices and turn == 0:
            locations["six"] = "a"
            optional_choices.remove(6)
        if 6 in optional_choices and turn == 1:
            locations["six"] = "b"
            optional_choices.remove(6)
        else:
            pass
    if s7[0] <= mouse_location[0] <= s7[1] and s7[2] <= mouse_location[1] <= s7[3]:  # square 1
        if 7 in optional_choices and turn == 0:
            locations["seven"] = "a"
            optional_choices.remove(7)
        if 7 in optional_choices and turn == 1:
            locations["seven"] = "b"
            optional_choices.remove(7)
        else:
            pass
    if s8[0] <= mouse_location[0] <= s8[1] and s8[2] <= mouse_location[1] <= s8[3]:  # square 1
        if 8 in optional_choices and turn == 0:
            locations["eight"] = "a"
            optional_choices.remove(8)
        if 8 in optional_choices and turn == 1:
            locations["eight"] = "b"
            optional_choices.remove(8)
        else:
            pass
    if s9[0] <= mouse_location[0] <= s9[1] and s9[2] <= mouse_location[1] <= s9[3]:  # square 1
        if 9 in optional_choices and turn == 0:
            locations["nine"] = "a"
            optional_choices.remove(9)
        if 9 in optional_choices and turn == 1:
            locations["nine"] = "b"
            optional_choices.remove(9)
        else:
            pass


def images_on_screen():
    if locations["one"] == "a":
        DISPLAY.blit(x_img, (s1[0], s1[2]))
    if locations["two"] == "a":
        DISPLAY.blit(x_img, (s2[0], s2[2]))
    if locations["three"] == "a":
        DISPLAY.blit(x_img, (s3[0], s3[2]))
    if locations["four"] == "a":
        DISPLAY.blit(x_img, (s4[0], s4[2]))
    if locations["five"] == "a":
        DISPLAY.blit(x_img, (s5[0], s5[2]))
    if locations["six"] == "a":
        DISPLAY.blit(x_img, (s6[0], s6[2]))
    if locations["seven"] == "a":
        DISPLAY.blit(x_img, (s7[0], s7[2]))
    if locations["eight"] == "a":
        DISPLAY.blit(x_img, (s8[0], s8[2]))
    if locations["nine"] == "a":
        DISPLAY.blit(x_img, (s9[0], s9[2]))

    if locations["one"] == "b":
        DISPLAY.blit(o_img, (s1[0], s1[2]))
    if locations["two"] == "b":
        DISPLAY.blit(o_img, (s2[0], s2[2]))
    if locations["three"] == "b":
        DISPLAY.blit(o_img, (s3[0], s3[2]))
    if locations["four"] == "b":
        DISPLAY.blit(o_img, (s4[0], s4[2]))
    if locations["five"] == "b":
        DISPLAY.blit(o_img, (s5[0], s5[2]))
    if locations["six"] == "b":
        DISPLAY.blit(o_img, (s6[0], s6[2]))
    if locations["seven"] == "b":
        DISPLAY.blit(o_img, (s7[0], s7[2]))
    if locations["eight"] == "b":
        DISPLAY.blit(o_img, (s8[0], s8[2]))
    if locations["nine"] == "b":
        DISPLAY.blit(o_img, (s9[0], s9[2]))
    winner_check()

def no_winner():
    if "" not in locations.values():
        DISPLAY.fill(WHITE)
        py.display.update()
        time.sleep(3)
        GAME_ON = False
    else:
        GAME_ON = True
    return GAME_ON

def display_update():
    DISPLAY.fill(BLACK)
    images_on_screen()
    game_lines()


    py.display.update()

while GAME_ON:
    clock.tick(FPS)

    display_update()

    GAME_ON = no_winner()

    for event in py.event.get():
        if event.type == py.QUIT:
            GAME_ON = False


        if event.type == py.MOUSEBUTTONDOWN:
            mouse_pressed()











