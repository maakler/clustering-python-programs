def järjesta_punktid(p):
    for punkt1 in range(len(p)):
        for punkt2 in range(punkt1,len(p)):
            if p[punkt1][1] > p[punkt2][1]:
                p[punkt1], p[punkt2] = p[punkt2], p[punkt1]
            elif p[punkt1][1] == p[punkt2][1] and p[punkt1][0] > p[punkt2][0]:
                p[punkt1], p[punkt2] = p[punkt2], p[punkt1]
