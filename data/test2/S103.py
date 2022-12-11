def järjesta_punktid(p):
    for i in range(len(p)-1):
        miinimum = i
        for j in range(i+1,len(p)):
            if p[j][1] < p[miinimum][1]:
                miinimum = j
            elif p[j][1] == p[miinimum][1]:
                if p[j][0] < p[miinimum][0]:
                    miinimum = j
        if i != miinimum:
            p[i] , p[miinimum] = p[miinimum], p[i] 
