# rock paper scissors
import random

options = ["rock", "paper", "scissors"]
options_dict = {"rock": 1, "paper": 2, "scissors": 3}

def player_choice():
    p_choice = int(input("1) Rock\n2) Paper\n3) Scissors\nI choose: "))
    where_it_is = list(options_dict.keys())[list(options_dict.values()).index(p_choice)]
    if p_choice in options_dict.values():
        options.remove(where_it_is)
        return where_it_is
    else:
        return player_choice()

def pc_choice():
    p_choice = random.choice(options)
    return p_choice


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

    print("\n")
    print(player_move)
    print(pc_move)
    print("\n")

    you_won = winning_move()
    you_draw = draw_move()
    you_lose = lose_move()

    if you_won != None:
        return "player"
    if you_draw != None:
        return "draw"
    if you_lose != None:
        return "lose"

def winner(who_won):
    if who_won == "player":
        print("You won!")
    elif who_won == "lose":
        print("You lost! pc Won!")
    elif who_won == "draw":
        print("It's a draw!")


def main_game():
    player_move = player_choice()
    pc_move = pc_choice()
    who_won = strong_weak(player_move, pc_move)
    winner(who_won)

main_game()