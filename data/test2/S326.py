def järjesta_punktid(p):
    for i in range(len(p)-1):
        min_ = i
        for j in range(i, len(p)):
            if p[j][1] < p[min_][1]:
                min_ = j
            elif p[j][1] == p[min_][1]:
                if p[j][0] < p[min_][0]:
                    min_ = j
        if i != min_:
            p[i], p[min_] = p[min_], p[i]
    #return p

