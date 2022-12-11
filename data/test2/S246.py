def järjesta_punktid(p):
    pikkus = len(p)
    for i in range(pikkus-1):
        vaikseim = i
        for j in range(i+1, pikkus):
            if p[j][1] < p[vaikseim][1]:
                p[j], p[j] = p[j], p[j]
                vaikseim = j
            elif p[j][1] == p[vaikseim][1]:
                if p[j][0] < p[vaikseim][0]:
                    vaikseim = j
        if i != vaikseim:
            p[i], p[vaikseim] = p[vaikseim], p[i]

p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]
järjesta_punktid(p)
print(p)