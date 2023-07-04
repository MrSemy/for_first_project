import random


def greet():
    print("-------------------")
    print("  Приветсвуем вас  ")
    print("      в игре       ")
    print("  крестики-нолики  ")
    print("-------------------")
    print(" формат ввода: x y ")
    print(" x - номер строки  ")
    print(" y - номер столбца ")


def need_robot():
    print("вы будете играть один?")
    print("1 - да")
    print("0 - нет")
    while True:
        try:
            answer = int(input())
        except ValueError:
            print(" Введите число!!")
            continue

        if answer not in range(0, 2):
            print(" Введите число 0 или 1! ")
            continue
        return answer


def get_robot_turn():
    while True:
        robot_x, robot_y = random.randint(0, 2), random.randint(0, 2)
        if field[robot_x][robot_y] != " ":
            print(" Клетка занята! ")
            continue
        return robot_x, robot_y


def show():
    print()
    print("    | 0 | 1 | 2 | ")
    print("  --------------- ")
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print("  --------------- ")
    print()


def ask():
    while True:
        cords = input("         Ваш ход: ").split()

        if len(cords) != 2:
            print(" Введите 2 координаты! ")
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print(" Введите числа! ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Координаты вне диапазона! ")
            continue

        if field[x][y] != " ":
            print(" Клетка занята! ")
            continue

        return x, y


def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            show()
            print("Выиграл X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            show()
            print("Выиграл 0!!!")
            return True
    return False


greet()
robot = need_robot()
field = [[" "] * 3 for i in range(3)]
count = 0
while True:
    show()
    count += 1
    if count % 2 == 1:
        print(" Ходит крестик!")
        x, y = ask()
    else:
        print(" Ходит нолик!")
        if robot == 1:
            x, y = get_robot_turn()
        else:
            x, y = ask()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if check_win():
        break

    if count == 9:
        show()
        print(" Ничья!")
        break
