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