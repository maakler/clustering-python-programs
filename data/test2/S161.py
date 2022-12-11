p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]
def järjesta_punktid(p):
    for i in range(len(p)):
        for j in range(len(p)):
            if p[j][1]>p[i][1]:
                p[i],p[j]=p[j],p[i]
            elif p[j][1]==p[i][1]:
                if p[j][0]>p[i][0]:
                    p[i],p[j]=p[j],p[i]