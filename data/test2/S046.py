p= [(4,1), (4,3), (2,0), (6,1), (3,3), (5,2), (1,1)]
def järjesta_punktid(p):
    muutuja=0
    for i in range(len(p)-1):
        if p[i][1] > p[i+1][1]:
            p[i],p[i+1] = p[i+1],p[i]
            return järjesta_punktid(p)
            muutuja =1
        elif p[i][1] == p[i+1][1]:
            if p[i][0] > p[i+1][0]:
                p[i],p[i+1] = p[i+1],p[i]
                return järjesta_punktid(p)
                muutuja =1
    if muutuja == 0:
        return
    

