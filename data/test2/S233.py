def järjesta_punktid(p):
    for i in range(0, len(p)-1):
        s = i
        for j in range(i, len(p)):
            if p[j][1] < p[s][1]:
                s = j
            elif p[j][1] == p[s][1]:
                if p[j][0] < p[s][0]:
                    s = j
        p[i], p[s] = p[s], p[i]
p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]
print(järjesta_punktid(p))