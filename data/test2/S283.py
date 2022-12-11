def järjesta_punktid(p):
    for i in range(len(p)):
        miinimum = p[i][1]
        for j in range(i+1, len(p)):
            if p[j][1] < miinimum:
                miinimum = p[j][1]
        if p[i][1] != miinimum:
            p[i], p.index(miinimum) = p.index(miinimum), p[i]
    return p

p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]
print(järjesta_punktid(p))
            
            