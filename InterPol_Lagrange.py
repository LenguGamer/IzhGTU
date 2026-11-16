import matplotlib.pyplot as plt

def main():

    with open('plots.txt') as f:
        plots = f.readlines()
        plots = list(map(int, plots[0].split(' ')))

    x = plots[:len(plots) // 2:]
    y = plots[len(plots) // 2::]

    print(x)
    print(y)

    x_s = 0.0


    m_x = []
    m_y = []
    while x_s <= 7.0:
        L = 0
        for j in range(0, len(x)):
            S = 1
            S *= y[j]
            for i in range(0, len(x)):
                if i != j:
                    S *= (x_s - x[i]) / (x[j] - x[i])
            L += S
        m_x.append(x_s)
        m_y.append(L)
        x_s += 0.1

    print(m_x)
    print(m_y)
    plt.plot(m_x, m_y)
    plt.axis('equal')
    plt.show()

if __name__ == '__main__':
    main()
