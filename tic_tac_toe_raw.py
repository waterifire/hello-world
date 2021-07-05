# Tic tac toe
import random
import sys

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
def winner_check():
    # check winning options
    def horizontal_win():
        if a == b == c:
            wining_player = a
            winner(wining_player)
        elif d == e == f:
            wining_player = d
            winner(wining_player)
        elif g == h == i:
            wining_player = g
            winner(wining_player)
        else:
            pass

    def vertical_win():
        if a == d == g:
            wining_player = a
            winner(wining_player)
        elif b == e == f:
            wining_player = e
            winner(wining_player)
        elif c == f == i:
            wining_player = c
            winner(wining_player)
        else:
            pass

    def diagonal_win():
        if a == e == i:
            wining_player = a
            winner(wining_player)
        elif c == e == g:
            wining_player = c
            winner(wining_player)
        else:
            pass

    horizontal_win()
    vertical_win()
    diagonal_win()

    # if hor_win is None and vert_win and None and diag_win is None:
    #     pass
    #
    # elif hor_win[0] or vert_win[0] or diag_win[0]:
    #     if hor_win[0]:
    #         if hor_win[1] == "X":
    #             print("You are the winner!")
    #             sys.exit()
    #         else:
    #             print("PC is the winner")
    #             sys.exit()
    #     elif vert_win[0]:
    #         if vert_win[1] == "X":
    #             print("You are the winner!")
    #             sys.exit()
    #         else:
    #             print("PC is the winner")
    #             sys.exit()
    #     elif diag_win[0]:
    #         if diag_win[1] == "X":
    #             print("You are the winner!")
    #             sys.exit()
    #         else:
    #             print("PC is the winner")
    #             sys.exit()


# win/lose
def winner(winning_player):
    if winning_player == "X":
        print("You are the winner!")
        sys.exit()
    else:
        print("PC is the winner")
        sys.exit()

# mainloop
def game_running():

    while GAME_ON:
        p1_move()
        board_show()
        winner_check()
        pc_move()
        board_show()
        winner_check()

game_running()