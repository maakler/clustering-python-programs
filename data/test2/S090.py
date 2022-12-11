def järjesta_punktid(x):
    for i in range(len(x)):
        min = i
        for j in range(i+1, len(x)):
            if x[j][1] < x[min][1]:
                min = j
            elif x[j][1] == x[min][1]:
                if x[j][0] < x[min][0]:
                    min = j
        if i != min:
            x[i], x[min] = x[min], x[i]
            