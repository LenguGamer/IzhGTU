import math
def expon(x):
    S, n, q = 1, 1, 1
    epsilon = 0.000001

    while abs(q) > epsilon:
        q = q*(x / n)
        S += q
        n += 1
    return round(S, 6)

def ln(z):
    x = 1 / z - 1
    S, n, q = x, 2, x

    epsilon = 0.00000000001
    while abs(q) > epsilon:
        q = q*(-1)*x*(n - 1)/n
        S += q
        n += 1
    return round((-1)*S, 6)

def sin(x):
    S, n, q = x, 1, x
    epsilon = 0.000001

    while abs(q) > epsilon:
        q = q*((-1)*x**2/((n + 1)*(n + 2)))
        S += q
        n += 2
    return round(S, 6)

def cos(x):
    S, n, q = 1, 0, 1
    epsilon = 0.000001

    while abs(q) > epsilon:
        q = q*((-1)*x**2/((n + 1)*(n + 2)))
        S += q
        n += 2
    return round(S, 6)
def main():
    n = 6
    x1 = 3.716+0.043*n
    x2 = 2.834 - 0.028*n
    x1 = 0.2
    print('            Мой код | Не мой код')
    print(f'     e^x1 {expon(x1)} | {round(math.exp(x1), 6)}')
    print(f'     e^x2 {expon(x2)} | {round(math.exp(x2), 6)}')
    print(f'ln(x1 + 1) {ln(x1 + 1)} | {round(math.log(x1 + 1), 6)}')
    print(f'ln(x2 + 1) {ln(x2 + 1)} | {round(math.log(x2 + 1), 6)}')
    print(f'  sin(x1) {sin(x1)} | {round(math.sin(x1), 6)}')
    print(f'   sin(x2) {sin(x2)} | {round(math.sin(x2), 6)}')
    print(f'  cos(x1) {cos(x1)} | {round(math.cos(x1), 6)}')
    print(f'  cos(x2) {cos(x2)} | {round(math.cos(x2), 6)}')



if __name__ == '__main__':
    main()