def järjesta_punktid(p):
    for i in range(len(p)):
        for j in range(len(p)-1):
            if p[j][1] > p[j+1][1]:
                p[j], p[j+1] = p[j+1], p[j]
            if p[j][1] == p[j+1][1]:
                if p[j][0] > p[j+1][0]:
                    p[j], p[j+1] = p[j+1], p[j]
    
p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]

järjesta_punktid(p)
print(p)

#mullsortimine
#https://stackabuse.com/bubble-sort-in-python/