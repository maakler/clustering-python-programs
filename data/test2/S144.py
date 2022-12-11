def järjesta_punktid(p):
    length = len(p)
    for i in range(length):
        for j in range(length-1):
            if p[j][1] > p[i][1]:
                p[j], p[i] = p[i], p[j]
            elif p[j][1] == p[i][1]:
                if p[j][0] > p[i][0]:
                    p[j], p[i] = p[i], p[j]