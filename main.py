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
            pass

    if choice == 2:
        change_to = input("To what?\n"
                          "1) Binary\n"
                          "2) Octal\n"
                          "3) Hexadecimal"
                          "I choose:")
        change_to = int(change_to)
        if change_to == 1:
            pass
        elif change_to == 2:
            pass
        elif change_to == 3:
            pass

    if choice == 3:
        change_to = input("To what?\n"
                          "1) Binary\n"
                          "2) Decimal\n"
                          "3) Hexadecimal"
                          "I choose:")
        change_to = int(change_to)
        if change_to == 1:
            pass
        elif change_to == 2:
            pass
        elif change_to == 3:
            pass

    if choice == 4:
        change_to = input("To what?\n"
                          "1) Binary\n"
                          "2) Decimal\n"
                          "3) Octal"
                          "I choose:")
        change_to = int(change_to)
        if change_to == 1:
            pass
        elif change_to == 2:
            pass
        elif change_to == 3:
            pass



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

    print(new_ls)

    for i in new_ls:
        answer = answer + i

        count2 += 1
        if count2 == 3:
            answer = str(answer)
            final_ls.append(answer)
            count2 = 0
            answer = 0
    print(final_ls)
    for i in final_ls:
        result += i
        result = result

    print(result)



start_start()
