p = [(1, 4), (6, 4), (4, 4), (3, 4)]
def järjesta_punktid(p):
    for i in range(len(p)):
        for j in range(i+1, len(p)):
            if p[i][1] > p[j][1]:
                p[i], p[j] = p[j], p[i]
            elif p[i][1] == p[j][1] and p[i][0] > p[j][0]:
                p[i], p[j] = p[j], p[i]
