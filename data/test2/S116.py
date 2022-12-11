p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]

def järjesta_punktid(p):
    for i in range(len(p)):
        for j in range(i+1,len(p)):
            if p[i][1] > p[j][1]:
                p[i], p[j] = p[j], p[i]
                
    for k in range(len(p)):
        for l in range(k+1, len(p)):
            if p[k][0] > p[l][0] and p[k][1] == p[l][1]:
                p[k], p[l] = p[l], p[k]
                
    return

print(järjesta_punktid(p))