def järjesta_punktid(p):
    for i in range(len(p)):
        for j in range(len(p)-1):
            if p[j][1] > p[j + 1][1]:
                temp = p[j]
                p[j] = p[j+1]
                p[j+1] = temp
            if p[j][1] == p[j+1][1]:
                if p[j][0] > p[j+1][0]:
                    temp = p[j]
                    p[j] = p[j+1]
                    p[j+1] = temp
    return p
p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]
print(järjesta_punktid(p))
