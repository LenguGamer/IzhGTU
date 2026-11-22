import math
def Lagrange(x, y, x_s):
    L = 0
    for j in range(0, len(x)):
        S = 1
        S *= y[j]
        for i in range(0, len(x)):
            if i != j:
                S *= (x_s - x[i]) / (x[j] - x[i])
        L += S

    f = math.log(2.3*x_s) - 0.8 / x_s

    err_absolute = abs(f - L)
    err_teor = abs((2 / x[0]**3 + 4.8 / x[0]**4) * (x_s - x[0])*(x_s - x[1])*(x_s - x[2]) / 6)
    return L, f, err_absolute, err_teor

def main():
    x = [1.2, 1.9, 3.3, 4.7, 5.4, 6.8, 7.5]
    y = [0.3486, 1.0537, 1.7844, 2.2103, 2.3712, 2.6322, 2.7411]
    x_s = float(input('Введите значение из промежутка крайних значений входных данных:'))

    i = 1
    while i < len(x) and x_s > x[i]:
        i += 1

    if i == 1:
        x_srez = x[0:3]
        y_srez = y[0:3]
    elif i == len(x) - 1:
        x_srez = x[-3:len(x)]
        y_srez = y[-3:len(x)]
    else:
        l_r = abs(x[i - 1] - x_s) + abs(x[i] - x_s) + abs(x[i + 1] - x_s)
        l_l = abs(x[i - 1] - x_s) + abs(x[i] - x_s) + abs(x[i - 2] - x_s)
        if l_l <= l_r:
            x_srez = x[i - 2:i+1]
            y_srez = y[i - 2:i+1]
        else:
            x_srez = x[i - 1:i+2]
            y_srez = y[i - 1:i+2]

    answer = Lagrange(x_srez, y_srez, x_s)

    print(f'Выбранный отрезок для точки {x_s}: {x_srez}')
    print(f'Значение функции f в точке {x_s}: {answer[1]}')
    print(f'Значение полинома Лагранжа в точке {x_s}: {answer[0]}')
    print(f'Значение Абсолютной погрешности в точке {x_s}: {answer[2]}')
    print(f'Значение Теоретической погрешности в точке {x_s}: {answer[3]}')


if __name__ == '__main__':
    main()
