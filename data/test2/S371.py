def järjesta_punktid(punktid):
    for i in range(len(punktid)):
        miinimum = i
        for j in range(i + 1, len(punktid)):
            if punktid[j][1] < punktid[miinimum][1]:
                miinimum = j
            if punktid[j][1] == punktid[miinimum][1]:
                if punktid[j][0] < punktid[miinimum][0]:
                    miinimum = j
        if i != miinimum:
            punktid[i], punktid[miinimum] = punktid[miinimum], punktid[i]
            
p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]
järjesta_punktid(p)
print(p)