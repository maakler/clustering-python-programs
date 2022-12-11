def järjesta_punktid(jada):
    for i in range(0, len(jada)-1):
        s = i
        for j in range(i, len(jada)):
            if jada[j][1] < jada[s][1]:
                s = j
        jada[i], jada[s] = jada[s], jada[i]
    for i in range(0, len(jada)-1):
        s = i
        for j in range(i, len(jada)):
            if jada[j][0] < jada[s][0] and jada[j][1] == jada[s][1]:
                s = j
        jada[i], jada[s] = jada[s], jada[i]