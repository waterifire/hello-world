# Tic tac toe
import random
import sys
import tkinter as tk


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



# mainloop
def game_running():

    while GAME_ON:
        p1_move()
        board_show()
        winner_check()
        pc_move()
        board_show()
        winner_check()

# tkinter time!

""" -- Colors -- """
WHITE = "#ffffff"
BLACK = "#000000"
GREEN = "#14ff14"
RED = "#FF3333"
BLUE = "#1919FF"

""" -- variables -- """
WIDTH = 600
HEIGHT = 600

main_base = tk.Tk()

canvas = tk.Canvas(main_base, width=WIDTH, height=HEIGHT)
canvas.place(relx=0, rely=0, relwidth=1, relheight=1)

# First row
pos1 = tk.Button(canvas, bg=WHITE, fg=BLACK, text="1", command=lambda: act1())
pos1.place(relx=0, rely=0, relwidth=0.333, relheight=0.333)

pos2 = tk.Button(canvas, bg=WHITE, fg=BLACK, text="2", command=lambda: act2())
pos2.place(relx=0.333, rely=0, relwidth=0.333, relheight=0.333)

pos3 = tk.Button(canvas, bg=WHITE, fg=BLACK, text="3", command=lambda: act3())
pos3.place(relx=0.6666, rely=0, relwidth=0.333, relheight=0.333)

# Second Row
pos4 = tk.Button(canvas, bg=WHITE, fg=BLACK, text="4", command=lambda: act4())
pos4.place(relx=0, rely=0.333, relwidth=0.333, relheight=0.333)

pos5 = tk.Button(canvas, bg=WHITE, fg=BLACK, text="5", command=lambda: act5())
pos5.place(relx=0.333, rely=0.333, relwidth=0.333, relheight=0.333)

pos6 = tk.Button(canvas, bg=WHITE, fg=BLACK, text="6", command=lambda: act6())
pos6.place(relx=0.6666, rely=0.333, relwidth=0.333, relheight=0.333)

# Third row
pos7 = tk.Button(canvas, bg=WHITE, fg=BLACK, text="7", command=lambda: act7())
pos7.place(relx=0, rely=0.6666, relwidth=0.333, relheight=0.333)

pos8 = tk.Button(canvas, bg=WHITE, fg=BLACK, text="8", command=lambda: act8())
pos8.place(relx=0.333, rely=0.6666, relwidth=0.333, relheight=0.333)

pos9 = tk.Button(canvas, bg=WHITE, fg=BLACK, text="9", command=lambda: act9())
pos9.place(relx=0.6666, rely=0.6666, relwidth=0.333, relheight=0.333)


label_list = []

turn = 1

def turn_switch(turn):
    turn += 1
    turn = turn % 2
    print(turn)
    return turn


def act1():
    global a, turn
    if turn == 0:
        pos1.destroy()
        lab1 = tk.Label(canvas, bg=RED, fg=WHITE, text="X")
        lab1.place(relx=0, rely=0, relwidth=0.333, relheight=0.333)
        a = "X"
        label_list.append(lab1)
    else:
        pos1.destroy()
        lab1 = tk.Label(canvas, bg=BLUE, fg=WHITE, text="O")
        lab1.place(relx=0, rely=0, relwidth=0.333, relheight=0.333)
        a = "O"
        label_list.append(lab1)
    turn = turn_switch(turn)
    winner_check()

def act2():
    global b, turn
    if turn == 0:
        pos2.destroy()
        lab2 = tk.Label(canvas, bg=RED, fg=WHITE, text="X")
        lab2.place(relx=0.333, rely=0, relwidth=0.333, relheight=0.333)
        b = "X"
        label_list.append(lab2)
    else:
        pos2.destroy()
        lab2 = tk.Label(canvas, bg=BLUE, fg=WHITE, text="O")
        lab2.place(relx=0.333, rely=0, relwidth=0.333, relheight=0.333)
        b = "O"
        label_list.append(lab2)
    turn = turn_switch(turn)
    winner_check()


def act3():
    global c, turn
    if turn == 0:
        pos3.destroy()
        lab3 = tk.Label(canvas, bg=RED, fg=WHITE, text="X")
        lab3.place(relx=0.6666, rely=0, relwidth=0.333, relheight=0.333)
        c = "X"
        label_list.append(lab3)
    else:
        pos3.destroy()
        lab3 = tk.Label(canvas, bg=BLUE, fg=WHITE, text="O")
        lab3.place(relx=0.6666, rely=0, relwidth=0.333, relheight=0.333)
        c = "O"
        label_list.append(lab3)
    turn = turn_switch(turn)
    winner_check()


def act4():
    global d, turn
    if turn == 0:
        pos4.destroy()
        lab4 = tk.Label(canvas, bg=RED, fg=WHITE, text="X")
        lab4.place(relx=0, rely=0.333, relwidth=0.333, relheight=0.333)
        d = "X"
        label_list.append(lab4)
    else:
        pos4.destroy()
        lab4 = tk.Label(canvas, bg=BLUE, fg=WHITE, text="O")
        lab4.place(relx=0, rely=0.333, relwidth=0.333, relheight=0.333)
        d = "O"
        label_list.append(lab4)
    turn = turn_switch(turn)
    winner_check()


def act5():
    global e, turn
    if turn == 0:
        pos5.destroy()
        lab5 = tk.Label(canvas, bg=RED, fg=WHITE, text="X")
        lab5.place(relx=0.333, rely=0.333, relwidth=0.333, relheight=0.333)
        e = "X"
        label_list.append(lab5)
    else:
        pos5.destroy()
        lab5 = tk.Label(canvas, bg=BLUE, fg=WHITE, text="O")
        lab5.place(relx=0.33, rely=0.333, relwidth=0.333, relheight=0.333)
        e = "O"
        label_list.append(lab5)
    turn = turn_switch(turn)
    winner_check()


def act6():
    global f, turn
    if turn == 0:
        pos6.destroy()
        lab6 = tk.Label(canvas, bg=RED, fg=WHITE, text="X")
        lab6.place(relx=0.6666, rely=0.333, relwidth=0.333, relheight=0.333)
        f = "X"
        label_list.append(lab6)
    else:
        pos6.destroy()
        lab6 = tk.Label(canvas, bg=BLUE, fg=WHITE, text="O")
        lab6.place(relx=0.6666, rely=0.333, relwidth=0.333, relheight=0.333)
        f = "O"
        label_list.append(lab6)
    turn = turn_switch(turn)
    winner_check()

def act7():
    global g, turn
    if turn == 0:
        pos7.destroy()
        lab7 = tk.Label(canvas, bg=RED, fg=WHITE, text="X")
        lab7.place(relx=0, rely=0.6666, relwidth=0.333, relheight=0.333)
        g = "X"
        label_list.append(lab7)
    else:
        pos7.destroy()
        lab7 = tk.Label(canvas, bg=BLUE, fg=WHITE, text="O")
        lab7.place(relx=0, rely=0.6666, relwidth=0.333, relheight=0.333)
        g = "O"
        label_list.append(lab7)
    turn = turn_switch(turn)
    winner_check()


def act8():
    global h, turn
    if turn == 0:
        pos8.destroy()
        lab8 = tk.Label(canvas, bg=RED, fg=WHITE, text="X")
        lab8.place(relx=0.333, rely=0.6666, relwidth=0.333, relheight=0.333)
        h = "X"
        label_list.append(lab8)
    else:
        pos8.destroy()
        lab8 = tk.Label(canvas, bg=BLUE, fg=WHITE, text="O")
        lab8.place(relx=0.333, rely=0.6666, relwidth=0.333, relheight=0.333)
        h = "O"
        label_list.append(lab8)
    turn = turn_switch(turn)
    winner_check()


def act9():
    global i, turn
    if turn == 0:
        pos9.destroy()
        lab9 = tk.Label(canvas, bg=RED, fg=WHITE, text="X")
        lab9.place(relx=0.6666, rely=0.6666, relwidth=0.333, relheight=0.333)
        i = "X"
        label_list.append(lab9)
    else:
        pos9.destroy()
        lab9 = tk.Label(canvas, bg=BLUE, fg=WHITE, text="O")
        lab9.place(relx=0.6666, rely=0.6666, relwidth=0.333, relheight=0.333)
        i = "O"
        label_list.append(lab9)
    turn = turn_switch(turn)
    winner_check()


# win/lose
def winner(winning_player):
    for lab in label_list:
        lab.destroy()
    label_winner = tk.Label(canvas, bg=GREEN, fg=WHITE)
    label_winner.place(relx=0, rely=0, relwidth=1, relheight=1)
    if winning_player == "X":
        label_winner.config(text="PLAYER 1 WINS!")
    else:
        label_winner.config(text="PC WINS!")





main_base.mainloop()

