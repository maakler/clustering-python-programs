def järjesta_punktid(p):
    for x in range(len(p)):
        for y in range(x,len(p)):
            if p[x][1]>p[y][1]:
                p[x],p[y] = p[y],p[x]
            elif p[x][1]==p[y][1]:
                if p[x][0]>p[y][0]:
                    p[x],p[y] = p[y],p[x]

p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]
järjesta_punktid(p)
print(p)