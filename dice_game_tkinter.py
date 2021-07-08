# Dice game
import random
import tkinter as tk

dice_options = [1, 2, 3, 4, 5, 6, 7]

row1 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
row2 = [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Tkinter time

""" -- variables -- """
# Colors
WHITE = "#ffffff"
BLACK = "#000000"
RED = "#ff0000"
GREEN = "#00ff00"
BLUE = "#0000ff"

# Dimensions
DISPLAY_WIDTH = 500
DISPLAY_HEIGHT = 500


base_root = tk.Tk()


display = tk.Canvas(base_root, width=DISPLAY_WIDTH, height=DISPLAY_HEIGHT, bg=WHITE)
display.place(relx=0, rely=0, relwidth=1, relheight=1)

p1_race_road = tk.Frame(display, bg=BLACK)
p1_race_road.place(relx=0, rely=0, relwidth=1, relheight=0.2)

p2_race_road = tk.Frame(display, bg=BLACK)
p2_race_road.place(relx=0, rely=0.2, relwidth=1, relheight=0.2)

p1_move = tk.Label(p1_race_road, fg=RED, text="")
p1_move.place(relx=0.2, rely=0.2, relwidth=0.6, relheight=0.6)

p2_move = tk.Label(p2_race_road, fg=BLUE, text="")
p2_move.place(relx=0.2, rely=0.2, relwidth=0.6, relheight=0.6)

roll_it = tk.Button(display, bg=GREEN, fg=WHITE, text="Roll dice button", command=lambda: p1_make_move())
roll_it.place(relx=0.4, rely=0.8, relwidth=0.2, relheight=0.1)

winner_label = tk.Label(display, bg=BLACK, fg=WHITE,text="")

def diced_pressed():
    x = random.choice(dice_options) - 1
    return x


def draw_p1():
    p1_text = ""
    for i in row1:
        if i == 0:
            p1_text = p1_text + "..___.."
        if i == 1:
            p1_text = p1_text + "P1"

    p1_move.config(text=p1_text)

def draw_p2():
    p2_text = ""
    for i in row2:
        if i == 0:
            p2_text = p2_text + "..___.."
        if i == 1:
            p2_text = p2_text + "P2"

    p2_move.config(text=p2_text)


def finished(winner):
    roll_it.destroy()
    winner_label.place(relx=0, rely=0.4, relwidth=1, relheight=0.6)
    winner_label.config(text=f"{winner} is the winner!!!")


def p1_make_move():
    p1_roll = random.choice(dice_options) - 1
    if p1_roll == 0:
        p1_roll = 1
    for a, i in enumerate(row1):
        if i == 1:
            row1[a] = 0
            b = a + p1_roll
    if b < 19:
        row1[b] = 1
        draw_p1()
    elif b >= 19:
        row1[19] = 1
        draw_p1()
        winner = "P1"
        finished(winner)

    p2_roll = random.choice(dice_options) - 1
    if p2_roll == 0:
        p2_roll = 1
    for a, i in enumerate(row2):
        if i == 1:
            row2[a] = 0
            b = a + p2_roll
    if b < 19:
        row2[b] = 1
        draw_p2()
    elif b >= 19:
        row2[19] = 1
        draw_p2()
        winner = "P2"
        finished(winner)


base_root.mainloop()
