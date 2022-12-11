def järjesta_punktid(p):
    n = len(p)
    for i in range(n):
        for j in range(0, n-i-1):
            if p[j][1] > p[j+1][1]:
                p[j], p[j+1] = p[j+1], p[j]

    for i in range(n):
        for j in range(0, n-i-1):
            if p[j][1] == p[j+1][1]:
                if p[j][0] > p[j+1][0]:
                    p[j], p[j+1] = p[j+1], p[j]
