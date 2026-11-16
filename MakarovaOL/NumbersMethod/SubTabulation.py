def k_difference(m):
    final_diff = [m]
    for k in range(1, len(m)):
        m_r = []
        for i in range(0, len(final_diff[k - 1]) - 1):
            m_r.append(final_diff[k - 1][i + 1] - final_diff[k - 1][i])
        final_diff.append(m_r)
    return final_diff

def first_polynom_Neuton(x, y, x_t, h, n):
    y_diff = k_difference(y)
    S = y[0]
    q = (x_t - x[0]) / h + 1
    s = 1
    for i in range(1, n + 1):
        s = s*(q - i) / i
        S += s * y_diff[i][0]

    s_next = s * (q - n - 1) / (n + 1)
    err = abs(s_next * y_diff[n + 1][0])

    return S, err

def second_polynom_Neuton(x, y, x_t, h, n):
    y_diff = k_difference(y)
    S = y[-1]
    q = (x_t - x[-1]) / h - 1
    s = 1
    for i in range(1, n + 1):
        s = s*(q + i) / i
        S += s * y_diff[i][-1]

    s_next = s * (q + n + 1) / (n + 1)
    err = abs(s_next * y_diff[n + 1][-1])

    return S, err

def main():
    x = [1.10, 1.15, 1.20, 1.25, 1.30, 1.35, 1.40, 1.45, 1.50, 1.55, 1.60]
    y = [0.89121, 0.91276, 0.93204, 0.94898, 0.96356, 0.97572, 0.98545, 0.99271, 0.99749, 0.99973, 0.99957]

    h = 0.05
    H = 0.02
    n = 3

    for k in range(11):
        x_t = round(1.10 + k* H, 2)

        kray = int(round((x_t - x[0]) / h, 5))

        x_p = x[kray:kray + n + 2]
        y_p = y[kray:kray + n + 2]

        val, err = first_polynom_Neuton(x_p, y_p, x_t, h, n)
        print(x_t, val, err)

if __name__ == '__main__':
    main()