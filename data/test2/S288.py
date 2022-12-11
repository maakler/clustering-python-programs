def järjesta_punktid(p):
    for i in range(1, len(p)):
        võti = p[i][1]
        asendus = p[i]
        j = i - 1
        while j >= 0 and võti < p[j][1]:
            p[j + 1] = p[j]
            j -= 1
        p[j + 1] = asendus
    for i in range(1, len(p)):
        võti = p[i][1]
        asendus = p[i]
        j = i - 1
        x = 0
        while j >= 0 and võti == p[j][1]:
            if p[i - x][0] > p[j][0]:
                pass
            else:
                p[j + 1] = p[j]
                p[j] = asendus
            j -= 1
            x += 1