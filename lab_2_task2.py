x = int(input("Введите 1 число: "))
y = int(input("Введите 2 число: "))

if y == 0:
    print("На ноль делить нельзя.")
else:
    if x % y == 0:
        print(f"{x} делится на {y} без остатка.")
    else:
        ostatok = x % y
        print(f"Остаток от деления {x} на {y} равен {ostatok}.")

    chislo = x // y
    print(f"Результат деления: {chislo}")