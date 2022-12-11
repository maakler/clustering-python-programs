def järjesta_punktid(jär):
    for i in range(len(jär)):
        min = i
        for j in range(i+1, len(jär)):
            if jär[j][1] < jär[min][1]:
                min = j
            elif jär[j][1] == jär[min][1] and jär[j][0] < jär[min][0]:
                min = j
        if i != min:
            jär[i], jär[min] = jär[min], jär[i]