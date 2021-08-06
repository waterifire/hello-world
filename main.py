# Adventure game!
# Keep it simple stupid
import tkinter as tk
import sys
import datetime

"""
Going to have repetitive functions that can be done everyday. basically like the sims
no adding extra skills or anything like that. Lets get this working before adding more add ons
"""


"""
Time:  (everything in minutes unless stated otherwise)
snooze = 10 
get ready for day = 30
home to work = 30 
work to home = 30
Work starts = 8 
eat  = 10 
sleep = 8
read = 1 hour
exercise = 1 hour
program = 3 hours
networking = 3 hours
talking = 30 
games = 1 hour


"""

#  ----- VARIABLES -------------------------------------------------
# Globals:
START_GAME = False
current_time = datetime.datetime(2021, 0o1, 0o1, 0o6, 00, 00, 000000)

# Player skills:
player_skill = {
    "programming": 0,
    "networking": 0,
    "typing": 0,
    "smart": 0,
    "exercise": 0,
}

# Display:
DISPLAY_W = 700
DISPLAY_H = 700

# Colors:
BLACK = '#000000'
WHITE = '#ffffff'
BLUE = '#0000ff'
RED = '#ff0000'
GREEN = '#00ff00'

#  ----- TKINTER DISPLAY LAYOUT ----------------------------------------------------------

base_root = tk.Tk()

base_bg = tk.Canvas(base_root, width=DISPLAY_W, height=DISPLAY_H, bg=BLUE)
# base_bg.place(relx=0, rely=0, relwidth=1, relheight=1)
base_bg.pack()

# Frames
frame_interactive = tk.Frame(base_root, bg=BLACK)
frame_interactive.place(relx=0, rely=0, relwidth=1, relheight=0.3)

frame_info = tk.Frame(base_root, bg=GREEN)
frame_info.place(relx=0, rely=0.3, relwidth=0.3, relheight=0.7)

frame_map = tk.Frame(base_root, bg=RED)
frame_map.place(relx=0.3, rely=0.3, relwidth=0.7, relheight=0.7)

# Interactive Area ------------

l_scene = tk.Label(frame_interactive, bg=WHITE, fg=BLACK, text='start')
l_scene.place(relx=0.05, rely=0.05, relwidth=0.6, relheight=0.75)

entry_client = tk.Entry(frame_interactive, bg=WHITE, fg=BLACK)
entry_client.place(relx=0.05, rely=0.82, relwidth=0.6, relheight=0.13)  # only when needed

b_c1 = tk.Button(frame_interactive, bg=WHITE, fg=BLACK, text='START', command=lambda: b1())
b_c1.place(relx=0.67, rely=0.3, relwidth=0.145, relheight=0.2)

b_c2 = tk.Button(frame_interactive, bg=WHITE, fg=BLACK, text='QUIT', command=lambda: b2())
b_c2.place(relx=0.833, rely=0.3, relwidth=0.145, relheight=0.2)

b_c3 = tk.Button(frame_interactive, bg=WHITE, fg=BLACK, text='Choice 1')
# b_choice3.place(relx=0.67, rely=0.52, relwidth=0.145, relheight=0.2)

b_c4 = tk.Button(frame_interactive, bg=WHITE, fg=BLACK, text='Choice 1')
# b_choice4.place(relx=0.833, rely=0.52, relwidth=0.145, relheight=0.2)

l_time = tk.Label(frame_interactive, bg=WHITE, fg=BLACK, text=current_time)
l_time.place(relx=0.67, rely=0.82, relwidth=0.305, relheight=0.13)

# ----- Functions --------------------------------------------------------------
def b1():
    global START_GAME
    if not START_GAME:
        print("Game started")
        START_GAME = True
        l_scene.config(text="Your alarm goes off")
        b_c1.config(text="Get up", command=lambda: wake_up())
        b_c2.config(text="Snooze", command=lambda: snooze())

def b2():
    if not START_GAME:
        print("Game exited")
        sys.exit()


def wake_up():
    print("waking up!")
    l_scene.config(text="You get up. now what?")
    b_c1.config(text="shower", command=lambda: get_ready())
    b_c2.config(text="study", command=lambda: study_what())
    b_c3.config(text="Watch tv", command=lambda: watch_tv())
    b_c4.config(text="Play on the phone", command=lambda: eat_food())
    b_c3.place(relx=0.67, rely=0.52, relwidth=0.145, relheight=0.2)
    b_c4.place(relx=0.833, rely=0.52, relwidth=0.145, relheight=0.2)


def snooze():
    print("Snooze time")
    l_scene.config(text="You sleep in")
    time_increase(10)

def time_increase(minutessss, hoursss=0, daysss=0):
    global current_time
    current_time = current_time + datetime.timedelta(days=daysss, hours=hoursss, minutes=minutessss)
    l_time.config(text=current_time)

# ------------------------------------------------------------------------------
base_root.mainloop()
