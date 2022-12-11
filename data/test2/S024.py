def järjesta_punktid(p):
    for i in range(len(p)):
        miinimum = i
        for j in range(i+1, len(p)):
            if p[j][1] < p[i][1]:
                miinimum = j  
        if i != miinimum:
            p[i], p[miinimum] = p[miinimum], p[i]

            

#järjesta_punktid([(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)])
    