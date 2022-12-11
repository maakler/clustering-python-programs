def järjesta_punktid(jär):
    for i in range(len(jär)):
        for j in range(i+1, len(jär)):
            if jär[j][1] <= jär[i][1]:
                jär[i], jär[j] = jär[j], jär[i]
                if jär[j][0] <= jär[i][0] and jär[j][1] <= jär[i][1]:
                    jär[i], jär[j] = jär[j], jär[i]