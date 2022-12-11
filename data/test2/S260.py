def järjesta_punktid(p):
    n = len(p)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if p[j][1] > p[j+1][1]:
                p[j], p[j+1] = p[j+1],p[j]
            if p[j][1] == p[j+1][1]:
                if p[j] > p[j+1]:
                    p[j], p[j+1] = p[j+1],p[j]

p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]          
järjesta_punktid(p)