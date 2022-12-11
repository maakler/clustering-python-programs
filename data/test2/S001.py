def järjesta_punktid(p):
    for a in range(len(p)-1):
        for b in range(a+1,len(p)):
            if p[b][1] < p[a][1] or p[b][1] == p[a][1] and p[b][0] < p[a][0]:
                p[a], p[b] = p[b], p[a]