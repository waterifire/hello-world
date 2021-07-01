"""import pygame as py
import sys


py.init()

# Global variables
GAME_ONGOING = True

# Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 255)
BLUE = (0, 0, 255)


# display
screen_display = (700, 700)
display = py.display.set_mode(screen_display)
py.display.set_caption("Collect and escape")



def display_update():
    py.display.update()

while GAME_ONGOING:
    display.fill(WHITE)


    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()


    display_update()

"""
import tkinter as tk
import random

correct_number = random.randint(1, 20)

up2 = correct_number + 2
down2 = correct_number - 2
up5 = correct_number + 5
down5 = correct_number - 5
up10 = correct_number + 10
down10 = correct_number - 10

count = 10

clue1 = f"The correct number is \n" \
        f"between {down10} and {up10}"
clue2 = f"The correct number is \n" \
        f"between {down5} and {up5}"
clue3 = f"The correct number is \n" \
        f"between {down2} and {up2}"
clue = ["", clue1, clue2, clue3]

not_won = False


def start(*args):
    global count
    answer = args[0]

    if not not_won:
        if answer == correct_number:
            winner()

        elif answer != correct_number:

            count -= 1
            if 9 >= count >= 7:
                if not not_won:
                    label_clue.config(text=f"Clue:\n{clue[1]}")
                else:
                    pass
            elif 6 >= count >= 4:
                if not not_won:
                    label_clue.config(text=f"Clue:\n{clue[2]}")
                else:
                    pass
            elif 3 >= count >= 1:
                if not not_won:
                    label_clue.config(text=f"Clue:\n{clue[3]}")
                else:
                    pass
            elif count == 0:
                lost()
        label_count.config(text=f"Tries:\n {count}")


def winner():
    global not_won
    not_won = True
    label_clue.config(text="")
    label_guide.config(text="Congratulations you won!")


def lost():
    if not not_won:
        label_clue.config(text="")
        label_guide.config(text="You lost!")
        tkinter_base.quit()
    else:
        pass


# Display
DISPLAY_WIDTH = 500
DISPLAY_HEIGHT = 500

# color
GREEN0 = "#80ff80"
GREEN = "#00ff00"
GREEN1 = "#00e600"
GREEN2 = "#00cc00"
GREEN3 = "#00b300"
WHITE = "#ffffff"
BLACK = "#000000"
BLUE0 = "#3333ff"
BLUE = "#0000ff"
BLUE1 = "#0000e6"
BLUE2 = "#0000b3"
RED0 = "#ff4d4d"
RED1 = "#ff0000"
RED2 = "#e60000"
RED3 = "#cc0000"

# buttons
button_height = 25
button_width = 25

options = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
           11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

tkinter_base = tk.Tk()

canvas0 = tk.Canvas(tkinter_base, bg=GREEN1)
canvas0.pack()

canvas = tk.Canvas(canvas0, bg=GREEN1)
canvas.place(relx=0, rely=0, relwidth=1, relheight=1)

b1 = tk.Button(canvas, bg=BLUE, fg=WHITE, text="1", command=lambda: pressed1())
b1.place(relx=0, rely=0.70, relwidth=0.1, relheight=0.15)

b2 = tk.Button(canvas, bg=BLUE, fg=WHITE, text="2", command=lambda: pressed2())
b2.place(relx=0.1, rely=0.70, relwidth=0.1, relheight=0.15)

b3 = tk.Button(canvas, bg=BLUE, fg=WHITE, text="3", command=lambda: pressed3())
b3.place(relx=0.2, rely=0.70, relwidth=0.1, relheight=0.15)

b4 = tk.Button(canvas, bg=BLUE, fg=WHITE, text="4", command=lambda: pressed4())
b4.place(relx=0.3, rely=0.70, relwidth=0.1, relheight=0.15)

b5 = tk.Button(canvas, bg=BLUE, fg=WHITE, text="5", command=lambda: pressed5())
b5.place(relx=0.4, rely=0.70, relwidth=0.1, relheight=0.15)

b6 = tk.Button(canvas, bg=BLUE, fg=WHITE, text="6", command=lambda: pressed6())
b6.place(relx=0.5, rely=0.70, relwidth=0.1, relheight=0.15)

b7 = tk.Button(canvas, bg=BLUE, fg=WHITE, text="7", command=lambda: pressed7())
b7.place(relx=0.6, rely=0.70, relwidth=0.1, relheight=0.15)

b8 = tk.Button(canvas, bg=BLUE, fg=WHITE, text="8", command=lambda: pressed8())
b8.place(relx=0.7, rely=0.70, relwidth=0.1, relheight=0.15)

b9 = tk.Button(canvas, bg=BLUE, fg=WHITE, text="9", command=lambda: pressed9())
b9.place(relx=0.8, rely=0.70, relwidth=0.1, relheight=0.15)

b10 = tk.Button(canvas, bg=BLUE, fg=WHITE, text="10", command=lambda: pressed10())
b10.place(relx=0.9, rely=0.70, relwidth=0.1, relheight=0.15)

b11 = tk.Button(canvas, bg=RED1, fg=WHITE, text="11", command=lambda: pressed11())
b11.place(relx=0, rely=0.85, relwidth=0.1, relheight=0.15)

b12 = tk.Button(canvas, bg=RED1, fg=WHITE, text="12", command=lambda: pressed12())
b12.place(relx=0.1, rely=0.85, relwidth=0.1, relheight=0.15)

b13 = tk.Button(canvas, bg=RED1, fg=WHITE, text="13", command=lambda: pressed13())
b13.place(relx=0.2, rely=0.85, relwidth=0.1, relheight=0.15)

b14 = tk.Button(canvas, bg=RED1, fg=WHITE, text="14", command=lambda: pressed14())
b14.place(relx=0.3, rely=0.85, relwidth=0.1, relheight=0.15)

b15 = tk.Button(canvas, bg=RED1, fg=WHITE, text="15", command=lambda: pressed15())
b15.place(relx=0.4, rely=0.85, relwidth=0.1, relheight=0.15)

b16 = tk.Button(canvas, bg=RED1, fg=WHITE, text="16", command=lambda: pressed16())
b16.place(relx=0.5, rely=0.85, relwidth=0.1, relheight=0.15)

b17 = tk.Button(canvas, bg=RED1, fg=WHITE, text="17", command=lambda: pressed17())
b17.place(relx=0.6, rely=0.85, relwidth=0.1, relheight=0.15)

b18 = tk.Button(canvas, bg=RED1, fg=WHITE, text="18", command=lambda: pressed18())
b18.place(relx=0.7, rely=0.85, relwidth=0.1, relheight=0.15)

b19 = tk.Button(canvas, bg=RED1, fg=WHITE, text="19", command=lambda: pressed19())
b19.place(relx=0.8, rely=0.85, relwidth=0.1, relheight=0.15)

b20 = tk.Button(canvas, bg=RED1, fg=WHITE, text="20", command=lambda: pressed20())
b20.place(relx=0.9, rely=0.85, relwidth=0.1, relheight=0.15)

label_guide = tk.Label(canvas, bg=GREEN0, fg=BLACK, text="Guess a number 1-20")
label_guide.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.2)

label_count = tk.Label(canvas, bg=GREEN2, fg=WHITE, text=10)
label_count.place(relx=0.02, rely=0.22, relwidth=0.48, relheight=0.48)

label_clue = tk.Label(canvas, bg=GREEN3, fg=WHITE, text=clue[0])
label_clue.place(relx=0.5, rely=0.22, relwidth=0.48, relheight=0.48)


def pressed1():
    if 1 in options:
        option_chosen = 1
        start(option_chosen)
        options.remove(1)
        b1.config(bg=WHITE)
    else:
        pass


def pressed2():
    if 2 in options:
        option_chosen = 2
        options.remove(2)
        start(option_chosen)
        b2.config(bg=WHITE)
    else:
        pass


def pressed3():
    if 3 in options:
        option_chosen = 3
        options.remove(3)
        start(option_chosen)
        b3.config(bg=WHITE)
    else:
        pass


def pressed4():
    if 4 in options:
        option_chosen = 4
        options.remove(4)
        start(option_chosen)
        b4.config(bg=WHITE)
    else:
        pass


def pressed5():
    if 5 in options:
        option_chosen = 5
        options.remove(5)
        start(option_chosen)
        b5.config(bg=WHITE)
    else:
        pass


def pressed6():
    if 6 in options:
        option_chosen = 6
        options.remove(6)
        start(option_chosen)
        b6.config(bg=WHITE)
    else:
        pass


def pressed7():
    if 7 in options:
        option_chosen = 7
        options.remove(7)
        start(option_chosen)
        b7.config(bg=WHITE)
    else:
        pass


def pressed8():
    if 8 in options:
        option_chosen = 8
        options.remove(8)
        start(option_chosen)
        b8.config(bg=WHITE)
    else:
        pass


def pressed9():
    if 9 in options:
        option_chosen = 9
        options.remove(9)
        start(option_chosen)
        b9.config(bg=WHITE)
    else:
        pass


def pressed10():
    if 10 in options:
        option_chosen = 10
        options.remove(10)
        start(option_chosen)
        b10.config(bg=WHITE)
    else:
        pass


def pressed11():
    if 11 in options:
        option_chosen = 11
        options.remove(11)
        start(option_chosen)
        b11.config(bg=WHITE)
    else:
        pass


def pressed12():
    if 12 in options:
        option_chosen = 12
        options.remove(12)
        start(option_chosen)
        b12.config(bg=WHITE)
    else:
        pass


def pressed13():
    if 13 in options:
        option_chosen = 13
        options.remove(13)
        start(option_chosen)
        b13.config(bg=WHITE)
    else:
        pass


def pressed14():
    if 14 in options:
        option_chosen = 14
        options.remove(14)
        start(option_chosen)
        b14.config(bg=WHITE)
    else:
        pass


def pressed15():
    if 15 in options:
        option_chosen = 15
        options.remove(15)
        start(option_chosen)
        b15.config(bg=WHITE)
    else:
        pass


def pressed16():
    if 16 in options:
        option_chosen = 16
        options.remove(16)
        start(option_chosen)
        b16.config(bg=WHITE)
    else:
        pass


def pressed17():
    if 17 in options:
        option_chosen = 17
        options.remove(17)
        start(option_chosen)
        b17.config(bg=WHITE)
    else:
        pass


def pressed18():
    if 18 in options:
        option_chosen = 18
        options.remove(18)
        start(option_chosen)
        b18.config(bg=WHITE)
    else:
        pass


def pressed19():
    if 19 in options:
        option_chosen = 19
        options.remove(19)
        start(option_chosen)
        b19.config(bg=WHITE)
    else:
        pass


def pressed20():
    if 20 in options:
        option_chosen = 20
        options.remove(20)
        start(option_chosen)
        b20.config(bg=WHITE)
    else:
        pass


tkinter_base.mainloop()