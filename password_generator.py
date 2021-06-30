## Password generator

# Requirements
# 8+ characters
# 1 uppercase
# 1 lowercase
# number
# special character
# no name or common word
# no previous passwords
# not the same as your previous passwords

import random
import tkinter as tk
import clipboard


def generate_password():
    upper_letters = ["A", "B", "C", "D", "E", "F", "G", "H",
                     "I", "J", "K", "L", "M", "N", "O", "P",
                     "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    lower_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                     "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    special_characters = ["!", "@", "#", "%", "^", "&", "*", "(", ")", "_", "+", "<",
                          ">", "?", "{", "}", "|", "/", "[", "]", "-", "="]

    password_length = random.randint(10, 20)
    options = {"uppercase_letter": 0, "lowercase_letter": 0, "number": 0, "special_character": 0}
    password = ""

    for i in range(password_length):
        chosen_choice = random.choice(list(options.keys()))
        if chosen_choice == "uppercase_letter":
            character = random.choice(upper_letters)
            password = password + character
        elif chosen_choice == "lowercase_letter":
            character = random.choice(lower_letters)
            password = password + character
        elif chosen_choice == "number":
            character = random.choice(numbers)
            password = password + character
        elif chosen_choice == "special_character":
            character = random.choice(special_characters)
            password = password + character
    update_label_password(password)
    keep_password(password)

    return password

password_safe = []
def keep_password(password):
    if len(password_safe) > 0:
        password_safe.clear()
        password_safe.append(password)
    elif len(password_safe) == 0:
        password_safe.append((password))

# password = generate_password()


# GUI's
# Tkinter
# pyQT
# Kivy
# WxPython
# pyside

# tkinter ----------




# display
display_width = 400
display_height = 400

# Color
WHITE = "#ffffff"
BLUE = "#0066ff"
BLUE1 = "#3385ff"
BLUE2 = "#66a3ff"
BLUE5 = "#003380"
BLUE6 = "#0047b3"

base = tk.Tk()

canvas = tk.Canvas(base, width=display_width, height=display_height)
canvas.pack()

frame_bg = tk.Frame(canvas, bg=BLUE)
frame_bg.place(relx=0, rely=0, relwidth=1, relheight=1)

frame_password_border = tk.Frame(frame_bg, bg=BLUE1)
frame_password_border.place(relx=0.2, rely=0.2, relwidth=0.62, relheight=0.12)

frame_password = tk.Frame(frame_password_border, bg=BLUE2)
frame_password.place(relx=0.02, rely=0.1, relwidth=0.96, relheight=0.8)

frame_generate_password_border = tk.Frame(frame_bg, bg=BLUE2)
frame_generate_password_border.place(relx=0.2, rely=0.35, relwidth=0.3, relheight=0.06)

button_generate_password = tk.Button(frame_generate_password_border, bg=BLUE5, fg=WHITE, text="Generate", command=lambda: generate_password())
button_generate_password.place(relx=0.02, rely=0.07, relwidth=0.96, relheight=0.86)

frame_copy_border = tk.Frame(frame_bg, bg=BLUE2)
frame_copy_border.place(relx=0.68, rely=0.35, relwidth=0.14, relheight=0.06)

button_copy = tk.Button(frame_copy_border, bg=BLUE5, fg=WHITE, text="Copy", command=lambda: copy_password())
button_copy.place(relx=0.02, rely=0.07, relwidth=0.96, relheight=0.86)

label_password = tk.Label(frame_password, fg="#000000", text="")
label_password.place(relx=0, rely=0, relwidth=1, relheight=1)



def update_label_password(password):
    label_password.config(text=password)
    return password



def copy_password():
    clipboard.copy(password_safe[0])




base.mainloop()