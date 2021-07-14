# Conversions between binary, decimal, octal, hexadecimal


def start_start():
    choice = input("So what you want to convert?\n"
                   "1) Binary\n"
                   "2) Decimal\n"
                   "3) Octal\n"
                   "4) Hexadecimal\n"
                   "I choose:")
    choice = int(choice)
    if choice == 1:
        change_to = input("To what?\n"
                          "1) Decimal\n"
                          "2) Octal\n"
                          "3) Hexadecimal\n"  
                          "I choose:")
        change_to = int(change_to)
        if change_to == 1:
            binary_to_decimal()
        elif change_to == 2:
            binary_to_octal()
        elif change_to == 3:
            binary_to_hexadecimal()

    if choice == 2:
        change_to = input("To what?\n"
                          "1) Binary\n" 
                          "2) Octal\n"
                          "3) Hexadecimal\n"
                          "I choose:")
        change_to = int(change_to)
        if change_to == 1:
            decimal_to_binary()
        elif change_to == 2:
            decimal_to_octal()
        elif change_to == 3:
            decimal_to_hexadecimal()

    if choice == 3:
        change_to = input("To what?\n"
                          "1) Binary\n"
                          "2) Decimal\n"
                          "3) Hexadecimal\n" 
                          "I choose:")
        change_to = int(change_to)
        if change_to == 1:
            octal_to_binary()
        elif change_to == 2:
            octal_to_decimal()
        elif change_to == 3:
            octal_to_hexadecimal()

    if choice == 4:
        change_to = input("To what?\n"
                          "1) Binary\n"  # !!!!
                          "2) Decimal\n"  
                          "3) Octal\n"  # -!!!!
                          "I choose:")
        change_to = int(change_to)
        if change_to == 1:
            hexadecimal_to_binary()
        elif change_to == 2:
            hexadecimal_to_decimal()
        elif change_to == 3:
            hexadecimal_to_octal()


# -------------------- Binary to everything ----------------------------
def binary_to_decimal():
    binary_number = list(input("Please input binary: "))  # 1010101010 => 10
    binary_number.reverse()
    new_list = []
    ans = 0

    for a, i in enumerate(binary_number):
        i = int(i)
        if i == 0:
            pass
        if i == 1:
            answer = i * 2 ** a
            new_list.append(answer)

    for i in new_list:
        ans = ans + i

    print(ans)


def binary_to_octal():
    binary_number = list(input("Please input binary: "))  # 1010101010 =>
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

    print(result)


def binary_to_hexadecimal():
    correct_binary = False
    ls1 = []
    ls2 = []
    ans1 = 0
    result = ""
    count1 = 0
    count2 = 0
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    binary_number = list(input("please input binary: "))

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

    print(result)

# -------------------- Decimal to everything ----------------------------
def decimal_to_binary():
    done_with_you = False
    ls1 = []
    result = ""


    dec_number = int(input("Please input your decimal number here: "))  # 348

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
    print(result)


def decimal_to_octal():
    done_with_you = False

    dec_number = int(input("Please enter decimal number: "))
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
    print(result)


def decimal_to_hexadecimal():
    done_with_you = False
    dec_number = int(input("Please enter decimal number: "))
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

    print(result)


# -------------------- Octal to everything ----------------------------
def octal_to_binary():
    oct_number = list(input("Please input the octal number here: "))  # 213
    ls1 = []
    ls2 = []
    ls3 = []
    num = 0
    result = ""
    count1 = 0
    count2 = 0
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

    print(oct_number)
    print(ls1)
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
    print(result)


def octal_to_hexadecimal():
    oct_number = list(input("Please input the octal number here: "))  # 213
    ls1 = []
    ls2 = []
    ls3 = []
    num = 0
    result = ""
    count1 = 0
    count2 = 0
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
        # print(i, count1, ls2)
        if count1 == 4:
            count1 = 0

            for a in ls2:
                num += a

            ls3.append(num)
            num = 0
            ls2.clear()

    print(ls3)
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

    print(result)


def octal_to_decimal():
    binary_number = list(input("Please input binary: "))  # 1657 => 943
    binary_number.reverse()
    new_list = []
    result = 0

    for a, i in enumerate(binary_number):
        i = int(i)
        answer = i * 8 ** a
        new_list.append(answer)

    for i in new_list:
        result = result + i

    print(result)

# -------------------- Hexadecimal to everything ----------------------------
def hexadecimal_to_binary():
    hexa_number = list(input("Input Hexadecimal number: "))

    ls1 = []
    ls2 = []
    ls3 = []
    num = 0
    result = ""
    count1 = 0
    count2 = 0
    correct_number = False
    int_ls = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    for i in hexa_number:
        if i not in int_ls:
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
    print(result)


def hexadecimal_to_decimal():
    hexa_number = list(input("Please input hexadecimal number: "))  # 1657 => 943
    hexa_number.reverse()
    new_list = []
    result = 0
    ls2 = []
    int_ls = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


    for i in hexa_number:
        if i not in int_ls:
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
    print(result)


def hexadecimal_to_octal():
    hexa_number = list(input("Input Hexadecimal number: "))

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

    # for f, g in enumerate(ls1):
    #     if g == 0:
    #         ls1.pop(f)
    #     elif g == 1:
    #         break
    #     break

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
    for i in final_ls:
        result += i
        result = result

    print(result)

start_start()
