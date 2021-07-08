# Dice game
import random


dice_options = [1, 2, 3, 4, 5, 6, 7]

row1 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
row2 = [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def race_show():
    print(row1)
    print(row2)

def dice_roll():
    r = input("press enter to roll the dice")
    roll = random.choice(dice_options) - 1
    if roll == 0:
        roll = 1
    print(f"roll = {roll}")
    for a, i in enumerate(row1):
        if i == 1:
            row1[a] = 0
            b = a + roll
    if b < 19:
        row1[b] = 1
        return True
    elif b >= 19:
        row1[19] = 1
        print("Player1 wins!")
        return False
def pc_roll():
    r = input("press enter for the pc to roll")
    roll = random.choice(dice_options) - 1
    if roll == 0:
        roll = 1
    print(f"roll = {roll}")
    for v, f in enumerate(row2):
        if f == 2:
            row2[v] = 0
            na = v + roll
    if na < 19:
        row2[na] = 2
        return True
    elif na >= 19:
        row2[19] = 2
        print("PC wins!")
        return False


def main_going():
    ongoing = True
    race_show()
    while ongoing:
        ongoing = dice_roll()
        if not ongoing:
            race_show()
            break
        ongoing = pc_roll()
        race_show()

main_going()