def järjesta_punktid(p):
    for i in range(0, len(p)-1):
        s = i
        for j in range(i, len(p)):
            if p[j][1] < p[s][1]:
                s = j
            if p[j][1] == p[s][1] and p[j][0] < p[s][0]:
                s = j
        p[i], p[s] = p[s], p[i]