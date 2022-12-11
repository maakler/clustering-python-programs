p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]


def järjesta_punktid(p):
    for x in range(len(p)):
        for i in range(1,len(p)):
            if p[i-1][1] > p[i][1]:
                p[i-1],p[i] = p[i],p[i-1]
            elif p[i-1][1] == p[i][1]:
                if p[i-1][0] > p[i][0]:
                    p[i-1],p[i] = p[i],p[i-1]
    
    return p

print(järjesta_punktid(p))
            
        