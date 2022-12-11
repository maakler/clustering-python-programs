def järjesta_punktid(a):
    for i in range(len(a) - 1):
        for j in range(i, len(a)):
            if a[i][1] > a[j][1]:
                a[i], a[j] = a[j], a[i]
            elif a[i][1] == a[j][1]:
                if a[i][0] > a[j][0]:
                    a[i], a[j] = a[j], a[i]   
