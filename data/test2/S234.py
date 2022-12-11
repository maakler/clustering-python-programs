def järjesta_punktid(p):
    for f in range(len(p)):
        for a in range(len(p)-1):
            if p[a][1]>p[a+1][1]:
                p[a],p[a+1]=p[a+1],p[a]
            elif p[a][1]==p[a+1][1]:
                if p[a][0]>p[a+1][0]:
                    p[a],p[a+1]=p[a+1],p[a]
    return p