matrix = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]
figs = ["X", "O"]


def print_matrix():
    global matrix

    for i in range(3):
        for j in range(3):
            print(matrix[i][j], end=" ")
        print()


def input_figs(fig):
    global matrix

    while True:
        field = list(map(int, input(f"Введите ячейку для {fig} в формате (строка(1-3) столбец(1-3)):").split()))
        if min(field) >= 1 and max(field) <= 3 and matrix[field[0]-1][field[1]-1] == "-":
            break
        elif min(field) >= 1 and max(field) <= 3 and matrix[field[0]-1][field[1]-1] != "-":
            print(f"Ошибка ввода. Ячейка уже занята {matrix[field[0]-1][field[1]-1]}. Введите координаты заново!")
            print_matrix()
        else:
            print("Ошибка ввода. Координаты вышли за пределы поля. Введите координаты заново!")
            print_matrix()
    return field


def victory():
    global matrix
    result = False
    for i in range(3):
        chet_x, chet_o = 0, 0
        for j in range(3):
            if matrix[i][j] == "X":
                chet_x += 1
            elif matrix[i][j] == "O":
                chet_o += 1
        if chet_x == 3:
            print("Выиграли X-ки!")
            result = True
        elif chet_o == 3:
            print("Выиграли O-ки!")
            result = True

    for j in range(3):
        chet_x, chet_o = 0, 0
        for i in range(3):
            if matrix[i][j] == "X":
                chet_x += 1
            elif matrix[i][j] == "O":
                chet_o += 1

        if chet_x == 3:
            print("Выиграли X-ки!")
            result = True
        elif chet_o == 3:
            print("Выиграли O-ки!")
            result = True

    chet_nul = 0
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == "-":
                chet_nul += 1

    if matrix[0][0] == matrix[1][1] == matrix[2][2] != "-" or matrix[0][2] == matrix[1][1] == matrix[2][0] != "-":
        print(f"Выиграли {matrix[1][1]}-ки!")
        result = True

    if chet_nul == 0 and not result:
        print("Ничья!!")
        result = True

    return result


print_matrix()
print("Давайте сыграем в крестики-нолики")
vic = victory()
while not vic:
    for f in figs:
        coord = input_figs(f)
        matrix[coord[0] - 1][coord[1] - 1] = f
        print_matrix()
        vic = victory()
        if vic:
            break

print("Автор: Вячеслав Попов (johnnydepp@bk.ru). Группа: PDEV-16 (SkillFactory)")
