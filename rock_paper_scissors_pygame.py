import pygame as py
import random

py.init()

""" -- Variables -- """
WIDTH = 600
HEIGHT = 600

DISPLAY = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption("Rock Paper Scissors")

""" -- Colors -- """
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


""" -- images -- """
paper_img = py.image.load("images/paper.png")
rock_img = py.image.load("images/rock.png")
scissors_img = py.image.load("images/scissors.png")

rock_img = py.transform.scale(rock_img, (200, 200))
paper_img = py.transform.scale(paper_img, (200, 200))
scissors_img = py.transform.scale(scissors_img, (200, 200))

rock_img = py.transform.scale(rock_img, (198, 200))
paper_img = py.transform.scale(paper_img, (198, 200))
scissors_img = py.transform.scale(scissors_img, (198, 200))

rock_location = (0, 0)
scissor_location = (0, 200)
paper_location = (0, 400)

rock_pc_location = (201, 0)
scissor_pc_location = (201, 200)
paper_pc_location = (201, 400)

rock_winner_location = (401, 0)
scissor_winner_location = (401, 200)
paper_winner_location = (401, 400)

winner_location = ()

def main_game():
    screen_img = [1, 1, 1]  # rock paper scissors
    puter_move = [1, 1, 1]
    winner = [0, 0, 0]
    pc_img = [1, 1, 1]
    game_ongoing = True

    def mouse_clicked():
        mouse_pos = py.mouse.get_pos()
        choices = ["rock", "paper", "scissors"]
        if 0 <= mouse_pos[0] <= 200:
            if 0 <= mouse_pos[1] <= 200:
                computer_choice = random.choice(choices)
                if computer_choice == "paper":
                    return [1, 0, 0], [0, 1, 0], [0, 1, 0]
                if computer_choice == "rock":
                    return [1, 0, 0], [1, 0, 0], [0, 0, 0]
                if computer_choice == "scissors":
                    return [1, 0, 0], [0, 0, 1], [1, 0, 0]
            if 200 <= mouse_pos[1] <= 400:
                choices.remove("scissors")
                computer_choice = random.choice(choices)
                if computer_choice == "paper":
                    return [0, 0, 1], [0, 1, 0], [0, 0, 1]
                if computer_choice == "scissors":
                    return [0, 0, 1], [0, 0, 1], [0, 0, 0]
                if computer_choice == "rock":
                    return [0, 0, 1], [1, 0, 0], [1, 0, 0]
            if 400 <= mouse_pos[1] <= HEIGHT:
                choices.remove("paper")
                computer_choice = random.choice(choices)
                if computer_choice == "rock":
                    return [0, 1, 0], [1, 0, 0], [0, 1, 0]
                if computer_choice == "paper":
                    return [0, 1, 0], [0, 1, 0], [0, 0, 0]
                if computer_choice == "scissors":
                    return [0, 1, 0], [0, 0, 1], [0, 0, 1]
            if mouse_pos[0] > 400:
                return [1, 1, 1], [1, 1, 1], [0, 0, 0]

    def show_img():
        if screen_img[0] == 1:
            DISPLAY.blit(rock_img, rock_location)
        if screen_img[1] == 1:
            DISPLAY.blit(paper_img, paper_location)
        if screen_img[2] == 1:
            DISPLAY.blit(scissors_img, scissor_location)

        if puter_move[0] == 1:
            DISPLAY.blit(rock_img, rock_pc_location)
        if puter_move[1] == 1:
            DISPLAY.blit(paper_img, paper_pc_location)
        if puter_move[2] == 1:
            DISPLAY.blit(scissors_img, scissor_pc_location)

        if winner[0] == 1:
            DISPLAY.blit(rock_img, rock_winner_location)
        if winner[1] == 1:
            DISPLAY.blit(paper_img, paper_winner_location)
        if winner[2] == 1:
            DISPLAY.blit(scissors_img, scissor_winner_location)




    def display_update():
        DISPLAY.fill(WHITE)
        line1 = py.draw.line(DISPLAY, BLUE, (200, 0), (200, HEIGHT), 1)
        line2 = py.draw.line(DISPLAY, BLUE, (400, 0), (400, HEIGHT), 1)
        show_img()
        py.display.update()

    while game_ongoing:


        # clock.tick(FPS)
        display_update()
        for event in py.event.get():
            if event.type == py.QUIT:
                game_ongoing = False

            if event.type == py.MOUSEBUTTONDOWN:
                screen_img, puter_move, winner = mouse_clicked()
                print(f"p1 = {screen_img}, puter={puter_move}, winner = {winner}")


main_game()
