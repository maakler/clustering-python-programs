def järjesta_punktid(p):
    for j in range(len(p)-1):
        for i in range(0, len(p)-1-j):
            if p[i][1] > p[i+1][1]:
                p[i], p[i+1] = p[i+1], p[i]
            elif p[i][1] == p[i+1][1] and p[i][0] > p[i+1][0]:
                    p[i], p[i+1] = p[i+1], p[i]