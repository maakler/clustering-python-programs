def järjesta_punktid(jär):
    n = len(jär)
    for i in range(n-1):
        for j in range(n-i-1):
            if jär[j][1] > jär[j+1][1]:
                jär[j], jär[j+1] = jär[j+1], jär[j]
            elif jär[j][1] == jär[j+1][1]:
                if jär[j][0] > jär[j+1][0]:
                    jär[j], jär[j+1] = jär[j+1], jär[j]

p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]
järjesta_punktid(p)