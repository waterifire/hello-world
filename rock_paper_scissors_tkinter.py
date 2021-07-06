# rock paper scissors
import random
import tkinter as tk

""" -- Variables -- """
DISPLAY_WIDTH = 750
DISPLAY_HEIGHT = 750

""" -- Colors -- """
BLUE = "#0000ff"
RED = "#ff0000"
GREEN = "#00ff00"
WHITE = "#ffffff"
BLACK = "#000000"

main_base = tk.Tk()


canvas = tk.Canvas(main_base, width=DISPLAY_WIDTH, height=DISPLAY_HEIGHT)
canvas.place(relx=0, rely=0, relwidth=1, relheight=1)

l_title = tk.Label(canvas, bg=WHITE, fg=RED, text="play and show man")
l_title.place(relx=0, rely=0, relwidth=DISPLAY_WIDTH, relheight=0.25)

b_rock = tk.Button(canvas, bg=BLUE, fg=WHITE, text="Rock", command=lambda: made_choice(p_choice="rock"))
b_rock.place(relx=0, rely=0.25, relwidth=DISPLAY_WIDTH, relheight=0.25)

b_paper = tk.Button(canvas, bg=RED, fg=WHITE, text="Paper", command=lambda: made_choice(p_choice="paper"))
b_paper.place(relx=0, rely=0.5, relwidth=DISPLAY_WIDTH, relheight=0.25)

b_scissors = tk.Button(canvas, bg=GREEN, fg=WHITE, text="scissors", command=lambda: made_choice(p_choice="scissors"))
b_scissors.place(relx=0, rely=0.75, relwidth=DISPLAY_WIDTH, relheight=0.25)

l_winner = tk.Label(canvas, bg=WHITE, fg=BLACK)

def made_choice(p_choice):
    options = ["rock", "paper", "scissors"]
    options.remove(p_choice)

    def pc_choice():
        pc_choice = random.choice(options)
        return pc_choice

    player_move = p_choice
    pc_move = pc_choice()
    print(player_move, pc_move)

    def strong_weak(player_move, pc_move):
        def winning_move():
            if player_move == "rock" and pc_move == "scissors":
                return "player"
            if player_move == "paper" and pc_move == "rock":
                return "player"
            if player_move == "scissors" and pc_move == "paper":
                return "player"

        def draw_move():
            if player_move == pc_move:
                return "draw"
            if player_move == pc_move:
                return "draw"
            if player_move == pc_move:
                return "draw"

        def lose_move():
            if player_move == "rock" and pc_move == "paper":
                return "pc"
            if player_move == "paper" and pc_move == "scissors":
                return "pc"
            if player_move == "scissors" and pc_move == "rock":
                return "pc"

        you_won = winning_move()
        you_draw = draw_move()
        you_lose = lose_move()

        if you_won != None:
            return "player"
        if you_draw != None:
            return "draw"
        if you_lose != None:
            return "lose"


    answer = strong_weak(player_move, pc_move)


    if answer == "player":
        b_scissors.destroy()
        b_paper.destroy()
        b_rock.destroy()
        l_title.destroy()
        l_winner.place(relx=0, rely=0, relwidth=1, relheight=1)
        l_winner.config(text="You are the winner!")
    if answer == "draw":
        l_winner.place(relx=0, rely=0, relwidth=1, relheight=1)
        l_winner.config(text="It's a Draw!")
    if answer == "lose":
        l_winner.place(relx=0, rely=0, relwidth=1, relheight=1)
        l_winner.config(text="You lost!")


main_base.mainloop()

