from openpyxl import Workbook, load_workbook

wb = load_workbook('docs/mission.xlsx')
ws = wb.active

print(ws)  # prints what worksheet you are on

# ws['C2'].value = 'Dylan'  # changes the value in that cell

# ws.title = 'Data'  # changes the title

# print(ws['C2'].value)  # prints everything in the cell

working_down = True

num = '2'

# print(ws[current_cell].value)


def cell_move():
    global num
    take_out = ls[0]
    ls.remove(take_out)
    num = int(num)
    num += 1
    num = str(num)
    current_cell = 'C' + num
    ls.append(current_cell)
    print(ls)

def amount_equal(num):
    num_ls = ['N', 'M', 'O', 'P', 'Q']
    count = 2

    def checking_amount(count):
        numb = str(int(num) + 1)
        looking_at = 'C' + numb
        if ws[[ls[1]]] == ws[looking_at]:
            print(f"before append=== {ls}")
            ls.append(looking_at)
            print(f"after append == {ls}")
            count += 1
            return count
        elif ws[[ls[1]]] != ws[looking_at]:
            how_many = False
            return count



    if count == 2:
        place = 'N' + num
        place2 = 'M' + num

        val = ls[0]
        val = val[1:]
        val = "B" + val

        mal = ls[1]
        mal = mal[1:]
        mal = "B" + mal

        ws[place] = ws[val].value
        ws[place2] = ws[mal].value
    elif count > 2:
        how_many = True
        while how_many:
            count = checking_amount(count)

        print(ls)
        num = int(num)
        for i in range(0, count):
            a = i + num
            a = str(a)

            val = ls[i]
            val = val[1:]
            val = "B" + val
            print(val)
            for x in num_ls:
                specific_cell = x + a
                ws[specific_cell] = val

# NPQORST
# ls = (C300, C301, C302, C303)  ->
# ls = (C132, C133, C134)
# ls = (C232, C233)
ls = ['c1', 'c2']

while working_down:

    if ws[ls[0]].value == ws[ls[1]].value:
        print("equal!   --------------------")
        amount_equal(num)
        cell_move()
    else:

        print("not equal")
        cell_move()
    if ws[ls[1]].value is None:
        print("done!!!!!")
        working_down = False





wb.save('docs/mission.xlsx')

