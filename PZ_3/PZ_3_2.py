N = int(input("Введите число от 1 до 4 (1 = сложение, 2 = вычитание, 3 = умножение, 4 = деление): "))
if N < 1:
    print("Число должно быть от 1 до 4.")
    exit()
elif N > 4:
    print("Число должно быть от 1 до 4.")
    exit()

A = float(input("Введите первое вещественное число A: "))
B = float(input("Введите второе вещественное число B: "))
if B == 0:
    print("Число B не должно быть равным нулю.")
    exit()

if N == 1:
    result = A+B
    print("Результат сложения: ", result)
elif N == 2:
    result = A-B
    print("Результат вычитания: ", result)
elif N == 3:
    result = A*B
    print("Результат умножения: ", result)
elif N == 4:
    result = A/B
    print("Результат деления: ", result)



