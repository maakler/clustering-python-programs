def järjesta_punktid(jär):
    for i in range(len(jär)):
        for j in range(len(jär)):
            if jär[i][1] < jär[j][1]:
                jär[i], jär[j] = jär[j], jär[i]
                
            elif jär[i][1] == jär[j][1]:
                if jär[i][0] < jär[j][0]:
                    jär[i], jär[j] = jär[j], jär[i]
