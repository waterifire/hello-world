# Conversions between binary, decimal, octal, hexadecimal
import tkinter.ttk
import tkinter as tk
import pyperclip


# -------------------- Binary to everything ----------------------------
def binary_to_decimal(invariable):
    binary_number = list(invariable)  # 1010101010 => 10
    binary_number.reverse()
    new_list = []
    result = 0

    for a, i in enumerate(binary_number):
        i = int(i)
        if i == 0:
            pass
        if i == 1:
            answer = i * 2 ** a
            new_list.append(answer)

    for i in new_list:
        result = result + i

    return result


def binary_to_octal(in_variable):
    binary_number = list(in_variable)  # 1010101010 =>
    correct_binary = False
    while not correct_binary:
        if len(binary_number) % 3 != 0:
            binary_number.insert(0, "0")
        if len(binary_number) % 3 == 0:
            correct_binary = True
    count = 0
    count2 = 0
    new_ls = []
    answer = 0
    final_ls = []
    result = ""

    for i in binary_number:
        if i == "0":
            new_ls.append(0)
        if i == "1":
            if count == 0:
              new_ls.append(4)
            if count == 1:
                new_ls.append(2)
            if count == 2:
                new_ls.append(1)

        count += 1
        if count >= 3:
            count = 0

    for i in new_ls:
        answer = answer + i

        count2 += 1
        if count2 == 3:
            answer = str(answer)
            final_ls.append(answer)
            count2 = 0
            answer = 0
    for i in final_ls:
        result += i
        result = result

    return result


def binary_to_hexadecimal(in_variable):
    correct_binary = False
    ls1 = []
    ls2 = []
    ans1 = 0
    result = ""
    count1 = 0
    count2 = 0
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    binary_number = list(in_variable)

    while not correct_binary:
        if len(binary_number) % 4 != 0:
            binary_number.insert(0, "0")
        if len(binary_number) % 4 == 0:
            correct_binary = True

    for i in binary_number:
        if i == "0":
            ls1.append(0)
        elif i == "1":
            if count1 == 0:
                ls1.append(8)
            elif count1 == 1:
                ls1.append(4)
            elif count1 == 2:
                ls1.append(2)
            elif count1 == 3:
                ls1.append(1)

        count1 += 1
        if count1 == 4:
            count1 = 0

    for i in ls1:
        ans1 += i

        count2 += 1
        if count2 == 4:
            count2 = 0
            ls2.append(ans1)
            ans1 = 0

    for i in ls2:
        if i in number_list:
            i = str(i)
            result += i
        elif i not in number_list:
            if i == 10:
                i = "A"
            elif i == 11:
                i = "B"
            elif i == 12:
                i = "C"
            elif i == 13:
                i = "D"
            elif i == 14:
                i = "E"
            elif i == 15:
                i = "F"
            result += i

    return result


# -------------------- Decimal to everything ----------------------------
def decimal_to_binary(in_variable):
    done_with_you = False
    ls1 = []
    result = ""


    dec_number = int(in_variable)  # 348

    while not done_with_you:
        if dec_number > 1:
            dec_number = float(dec_number) / 2.0
            if dec_number - int(dec_number) == 0:
                ls1.append(0)
            elif dec_number - int(dec_number) != 1:
                ls1.append(1)

            if dec_number == 1.0:
                num = dec_number / 2
                ls1.append(1)
                done_with_you = True

            if dec_number < 1.0:
                done_with_you = True

            dec_number = int(dec_number)

    ls1.reverse()

    for i in ls1:
        result = result + str(i)

    result = int(result)
    return result


def decimal_to_octal(in_variable):
    done_with_you = False
    dec_number = int(in_variable)
    ls1 = [dec_number]
    ls2 = []
    result = ""

    while not done_with_you:
        for i in ls1:
            num = i / 8
            num1 = num - int(num)
            ls1.append(int(num))

            num2 = num1 * 8

            num2 = int(num2)

            if i == 0:
                done_with_you = True
                break
            else:
                ls2.append(num2)

    ls2.reverse()

    for i in ls2:
        i = str(i)
        result += i

    result = int(result)
    return result


def decimal_to_hexadecimal(in_variable):
    done_with_you = False
    dec_number = int(in_variable)
    ls1 = [dec_number]
    ls2 = []
    result = ""

    while not done_with_you:
        for i in ls1:
            num = i / 16
            num1 = num - int(num)
            ls1.append(int(num))

            num2 = num1 * 16

            num2 = int(num2)

            if i == 0:
                done_with_you = True
                break
            else:
                ls2.append(num2)

    ls2.reverse()

    for i in ls2:

        if i < 10:
            i = str(i)
            result += i
        elif i >= 10:
            if i == 10:
                result += "A"
            elif i == 11:
                result += "B"
            elif i == 12:
                result += "C"
            elif i == 13:
                result += "D"
            elif i == 14:
                result += "E"
            elif i == 15:
                result += "F"

    return result


# -------------------- Octal to everything ----------------------------
def octal_to_binary(in_variable):
    oct_number = list(in_variable)  # 213
    ls1 = []
    result = ""

    for i in oct_number:
        i = int(i)
        if 4 == i:
            ls1.append(1)
            ls1.append(0)
            ls1.append(0)
        elif 2 == i:
            ls1.append(0)
            ls1.append(1)
            ls1.append(0)
        elif 1 == i:
            ls1.append(0)
            ls1.append(0)
            ls1.append(1)
        elif (4+1+2) == i:
            ls1.append(1)
            ls1.append(1)
            ls1.append(1)
        elif (4+2) == i:
            ls1.append(1)
            ls1.append(1)
            ls1.append(0)
        elif (4+1) == i:
            ls1.append(1)
            ls1.append(0)
            ls1.append(1)
        elif (2+1) == i:
            ls1.append(0)
            ls1.append(1)
            ls1.append(1)

    for f, g in enumerate(ls1):
        if g == 0:
            ls1.pop(f)
        elif g == 1:
            break
        break

    for b in ls1:
        b = str(b)
        result += b

    result = int(result)
    return result


def octal_to_hexadecimal(in_variable):
    oct_number = list(in_variable)  # 213
    ls1 = []
    ls2 = []
    ls3 = []
    num = 0
    result = ""
    count1 = 0
    correct_number = False

    for i in oct_number:
        i = int(i)
        if 4 == i:
            ls1.append(1)
            ls1.append(0)
            ls1.append(0)
        elif 2 == i:
            ls1.append(0)
            ls1.append(1)
            ls1.append(0)
        elif 1 == i:
            ls1.append(0)
            ls1.append(0)
            ls1.append(1)
        elif (4+2+1) == i:
            ls1.append(1)
            ls1.append(1)
            ls1.append(1)
        elif (4+2) == i:
            ls1.append(1)
            ls1.append(1)
            ls1.append(0)
        elif (4+1) == i:
            ls1.append(1)
            ls1.append(0)
            ls1.append(1)
        elif (2+1) == i:
            ls1.append(0)
            ls1.append(1)
            ls1.append(1)
        elif 0 == i:
            ls1.append(0)
            ls1.append(0)
            ls1.append(0)

    while not correct_number:
        if len(ls1) % 4 == 0:
            correct_number = True
        elif len(ls1) % 4 != 0:
            ls1.insert(0, 0)

    for i in ls1:
        if i == 0:
            ls2.append(0)
        elif i == 1 and count1 == 0:
            ls2.append(8)
        elif i == 1 and count1 == 1:
            ls2.append(4)
        elif i == 1 and count1 == 2:
            ls2.append(2)
        elif i == 1 and count1 == 3:
            ls2.append(1)

        count1 += 1
        if count1 == 4:
            count1 = 0

            for a in ls2:
                num += a

            ls3.append(num)
            num = 0
            ls2.clear()

    for b in ls3:
        if b == 0:
            b = str(b)
            result += b
        elif b < 10:
            b = str(b)
            result += b
        elif b >= 10:
            if b == 10:
                result += "A"
            elif b == 11:
                result += "B"
            elif b == 12:
                result += "C"
            elif b == 13:
                result += "D"
            elif b == 14:
                result += "E"
            elif b == 15:
                result += "F"

    return result


def octal_to_decimal(in_variable):
    binary_number = list(in_variable)  # 1657 => 943
    binary_number.reverse()
    new_list = []
    result = 0

    for a, i in enumerate(binary_number):
        i = int(i)
        answer = i * 8 ** a
        new_list.append(answer)

    for i in new_list:
        result = result + i

    return result


# -------------------- Hexadecimal to everything ----------------------------
def hexadecimal_to_binary(in_variable):
    hexa_number = list(in_variable)
    ls1 = []
    ls2 = []
    result = ""
    int_ls = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    for i in hexa_number:
        if i not in int_ls:
            i = i.capitalize()
            if i == "A" or i == "a":
                ls2.append(10)
            elif i == "B":
                ls2.append(11)
            elif i == "C":
                ls2.append(12)
            elif i == "D":
                ls2.append(13)
            elif i == "E":
                ls2.append(14)
            elif i == "F":
                ls2.append(15)
        elif i in int_ls:
            i = int(i)
            ls2.append(i)

    for i in ls2:
        if 15 == i:
            ls1.append(1)
            ls1.append(1)
            ls1.append(1)
            ls1.append(1)
        elif 14 == i:
            ls1.append(1)
            ls1.append(1)
            ls1.append(1)
            ls1.append(0)
        elif 13 == i:
            ls1.append(1)
            ls1.append(1)
            ls1.append(0)
            ls1.append(1)
        elif i == 12:
            ls1.append(1)
            ls1.append(1)
            ls1.append(0)
            ls1.append(0)
        elif 11 == i:
            ls1.append(1)
            ls1.append(0)
            ls1.append(1)
            ls1.append(1)
        elif i == 10:
            ls1.append(1)
            ls1.append(0)
            ls1.append(1)
            ls1.append(0)
        elif 9 == i:
            ls1.append(1)
            ls1.append(0)
            ls1.append(0)
            ls1.append(1)
        elif 8 == i:
            ls1.append(1)
            ls1.append(0)
            ls1.append(0)
            ls1.append(0)
        elif 7 == i:
            ls1.append(0)
            ls1.append(1)
            ls1.append(1)
            ls1.append(1)
        elif 6 == i:
            ls1.append(0)
            ls1.append(1)
            ls1.append(1)
            ls1.append(0)
        elif 5 == i:
            ls1.append(0)
            ls1.append(1)
            ls1.append(0)
            ls1.append(1)
        elif 4 == i:
            ls1.append(0)
            ls1.append(1)
            ls1.append(0)
            ls1.append(0)
        elif 3 == i:
            ls1.append(0)
            ls1.append(0)
            ls1.append(1)
            ls1.append(1)
        elif 2 == i:
            ls1.append(0)
            ls1.append(0)
            ls1.append(1)
            ls1.append(0)
        elif 1 == i:
            ls1.append(0)
            ls1.append(0)
            ls1.append(0)
            ls1.append(1)
        elif (4 + 2) == i:
            ls1.append(0)
            ls1.append(1)
            ls1.append(1)
            ls1.append(0)
        elif (4 + 1) == i:
            ls1.append(0)
            ls1.append(1)
            ls1.append(0)
            ls1.append(1)
        elif (2 + 1) == i:
            ls1.append(0)
            ls1.append(0)
            ls1.append(1)
            ls1.append(1)

    for f, g in enumerate(ls1):
        if g == 0:
            ls1.pop(f)
        elif g == 1:
            break
        break

    for b in ls1:
        b = str(b)
        result += b

    result = int(result)
    return result


def hexadecimal_to_decimal(in_variable):
    hexa_number = list(in_variable)  # 1657 => 943
    hexa_number.reverse()
    new_list = []
    result = 0
    ls2 = []
    int_ls = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    for i in hexa_number:
        if i not in int_ls:
            i = i.capitalize()
            if i == "A":
                ls2.append(10)
            elif i == "B":
                ls2.append(11)
            elif i == "C":
                ls2.append(12)
            elif i == "D":
                ls2.append(13)
            elif i == "E":
                ls2.append(14)
            elif i == "F":
                ls2.append(15)
        elif i in int_ls:
            i = int(i)
            ls2.append(i)

    for a, i in enumerate(ls2):
        i = int(i)
        answer = i * 16 ** a
        new_list.append(answer)

    for i in new_list:
        result = result + i
    return result


def hexadecimal_to_octal(in_variable):
    hexa_number = list(in_variable)
    answer = 0
    ls1 = []
    ls2 = []
    ls3 = []
    final_ls = []
    correct_binary = False
    result = ""
    count = 0
    count2 = 0
    int_ls = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    for i in hexa_number:
        if i not in int_ls:
            i = i.capitalize()
            if i == "A":
                ls2.append(10)
            elif i == "B":
                ls2.append(11)
            elif i == "C":
                ls2.append(12)
            elif i == "D":
                ls2.append(13)
            elif i == "E":
                ls2.append(14)
            elif i == "F":
                ls2.append(15)
        elif i in int_ls:
            i = int(i)
            ls2.append(i)

    for i in ls2:
        if 15 == i:
            ls1.append(1)
            ls1.append(1)
            ls1.append(1)
            ls1.append(1)
        elif 14 == i:
            ls1.append(1)
            ls1.append(1)
            ls1.append(1)
            ls1.append(0)
        elif 13 == i:
            ls1.append(1)
            ls1.append(1)
            ls1.append(0)
            ls1.append(1)
        elif i == 12:
            ls1.append(1)
            ls1.append(1)
            ls1.append(0)
            ls1.append(0)
        elif 11 == i:
            ls1.append(1)
            ls1.append(0)
            ls1.append(1)
            ls1.append(1)
        elif i == 10:
            ls1.append(1)
            ls1.append(0)
            ls1.append(1)
            ls1.append(0)
        elif 9 == i:
            ls1.append(1)
            ls1.append(0)
            ls1.append(0)
            ls1.append(1)
        elif 8 == i:
            ls1.append(1)
            ls1.append(0)
            ls1.append(0)
            ls1.append(0)
        elif 7 == i:
            ls1.append(0)
            ls1.append(1)
            ls1.append(1)
            ls1.append(1)
        elif 6 == i:
            ls1.append(0)
            ls1.append(1)
            ls1.append(1)
            ls1.append(0)
        elif 5 == i:
            ls1.append(0)
            ls1.append(1)
            ls1.append(0)
            ls1.append(1)
        elif 4 == i:
            ls1.append(0)
            ls1.append(1)
            ls1.append(0)
            ls1.append(0)
        elif 3 == i:
            ls1.append(0)
            ls1.append(0)
            ls1.append(1)
            ls1.append(1)
        elif 2 == i:
            ls1.append(0)
            ls1.append(0)
            ls1.append(1)
            ls1.append(0)
        elif 1 == i:
            ls1.append(0)
            ls1.append(0)
            ls1.append(0)
            ls1.append(1)
        elif (4 + 2) == i:
            ls1.append(0)
            ls1.append(1)
            ls1.append(1)
            ls1.append(0)
        elif (4 + 1) == i:
            ls1.append(0)
            ls1.append(1)
            ls1.append(0)
            ls1.append(1)
        elif (2 + 1) == i:
            ls1.append(0)
            ls1.append(0)
            ls1.append(1)
            ls1.append(1)

    while not correct_binary:
        if len(ls1) % 3 != 0:
            ls1.insert(0, 0)
        if len(ls1) % 3 == 0:
            correct_binary = True

    for i in ls1:
        if i == 0:
            ls3.append(0)
        if i == 1:
            if count == 0:
                ls3.append(4)
            if count == 1:
                ls3.append(2)
            if count == 2:
                ls3.append(1)

        count += 1
        if count >= 3:
            count = 0

    for i in ls3:
        i = i
        answer = answer + i
        count2 += 1
        if count2 == 3:
            answer = str(answer)
            final_ls.append(answer)
            count2 = 0
            answer = 0

    for f, g in enumerate(final_ls):
        g = int(g)
        if g == 0:
            final_ls.pop(f)
        elif g > 1:
            break

    for i in final_ls:
        result += i
        result = result

    return result

############################# TKINTER TIME #################################################

base_root = tk.Tk()

""" -- Variables -- """
# Colors
WHITE = "#ffffff"
BLACK = "#000000"
RED = "#ff0000"
GREEN = "#00ff00"
BLUE = "#0000ff"

GREYISH0 = "#c2d6d6"
GREYISH = "#a3c2c2"
GREYISH1 = "#85adad"
GREYISH2 = "#669999"
GREYISH3 = "#527a7a"
GREYISH4 = "#3d5c5c"

# display
DISPLAY_W = 500
DISPLAY_H = 500

canvas = tk.Canvas(base_root, width=DISPLAY_W, height=DISPLAY_H)
canvas.pack()

# ----------------------------- Frames -------------------------------------------------
frame_bg = tk.Frame(base_root, bg=BLACK)
frame_bg.place(relx=0, rely=0, relwidth=1, relheight=1)

frame_action_bg = tk.Frame(frame_bg, bg=GREYISH0)
frame_action_bg.place(relx=0, rely=0, relwidth=1, relheight=0.3)

frame_where_you_from = tk.Frame(frame_bg, bg=GREYISH1)
frame_where_you_from.place(relx=0, rely=0.3, relwidth=0.5, relheight=0.7)

frame_where_you_going = tk.Frame(frame_bg, bg=GREYISH2)
frame_where_you_going.place(relx=0.5, rely=0.3, relwidth=0.5, relheight=0.7)

# ----------------------------- Action Area -------------------------------------------------
e_input = tk.Entry(frame_action_bg, bg=WHITE, fg=BLACK, justify="center"
                                                                "")
e_input.place(relx=0.03, rely=0.2, relwidth=0.6, relheight=0.2)

l_output = tk.Label(frame_action_bg, bg=WHITE, fg=BLACK, text="")
l_output.place(relx=0.03, rely=0.6, relwidth=0.6, relheight=0.2)

b_search = tk.Button(frame_action_bg, bg=GREYISH1, fg=WHITE, text="Convert", command=lambda: search_it())
b_search.place(relx=0.66, rely=0.2, relwidth=0.3, relheight=0.2)

b_copy = tk.Button(frame_action_bg, bg=GREYISH1, fg=WHITE, text="Copy", command=lambda: copy_it())
b_copy.place(relx=0.66, rely=0.6, relwidth=0.3, relheight=0.2)

# ----------------------------- Dropdown box --------------------------------------------
from_title = tk.Label(frame_where_you_from, bg=GREYISH1, fg=WHITE, text="Converting from:")
from_title.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.1)

to_title = tk.Label(frame_where_you_going, bg=GREYISH2, fg=WHITE, text="Converting to:")
to_title.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.1)

from_what = tkinter.ttk.Combobox(frame_where_you_from, value=["Binary", "Decimal", "Octal", "Hexadecimal"])
from_what.place(relx=0.01, rely=0.12, relwidth=0.98, relheight=0.1)

to_what = tkinter.ttk.Combobox(frame_where_you_going, value=["Binary", "Decimal", "Octal", "Hexadecimal"])
to_what.place(relx=0.01, rely=0.12, relwidth=0.98, relheight=0.1)


# ----------------------------- Function -------------------------------------------------
ls_state = []

def copy_it():
    copied = l_output.cget("text")
    pyperclip.copy(copied)

def search_it():
    in_variable = e_input.get()
    coming_in = from_what.get()
    going_out = to_what.get()

    if coming_in == "Binary" and going_out == "Decimal":
        answer = binary_to_decimal(in_variable)
        l_output.config(text=answer)
    if coming_in == "Binary" and going_out == "Octal":
        answer = binary_to_octal(in_variable)
        l_output.config(text=answer)
    if coming_in == "Binary" and going_out == "Hexadecimal":
        answer = binary_to_hexadecimal(in_variable)
        l_output.config(text=answer)
    if coming_in == "Decimal" and going_out == "Binary":
        answer = decimal_to_binary(in_variable)
        l_output.config(text=answer)
    if coming_in == "Decimal" and going_out == "Octal":
        answer = decimal_to_octal(in_variable)
        l_output.config(text=answer)
    if coming_in == "Decimal" and going_out == "Hexadecimal":
        answer = decimal_to_hexadecimal(in_variable)
        l_output.config(text=answer)
    if coming_in == "Octal" and going_out == "Binary":
        answer = octal_to_binary(in_variable)
        l_output.config(text=answer)
    if coming_in == "Octal" and going_out == "Decimal":
        answer = octal_to_decimal(in_variable)
        l_output.config(text=answer)
    if coming_in == "Octal" and going_out == "Hexadecimal":
        answer = octal_to_hexadecimal(in_variable)
        l_output.config(text=answer)
    if coming_in == "Hexadecimal" and going_out == "Binary":
        answer = hexadecimal_to_binary(in_variable)
        l_output.config(text=answer)
    if coming_in == "Hexadecimal" and going_out == "Decimal":
        answer = hexadecimal_to_decimal(in_variable)
        l_output.config(text=answer)
    if coming_in == "Hexadecimal" and going_out == "Octal":
        answer = hexadecimal_to_octal(in_variable)
        l_output.config(text=answer)
    if coming_in == "Binary" and going_out == "Binary":
        answer = e_input.get()
        l_output.config(text=answer)
    if coming_in == "Decimal" and going_out == "Decimal":
        answer = e_input.get()
        l_output.config(text=answer)
    if coming_in == "Octal" and going_out == "Octal":
        answer = e_input.get()
        l_output.config(text=answer)
    if coming_in == "Hexadecimal" and going_out == "Hexadecimal":
        answer = e_input.get()
        l_output.config(text=answer)

base_root.mainloop()

