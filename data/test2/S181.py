def järjesta_punktid(a):
    pikkus = len(a)
    for i in range(pikkus):
        for j in range(pikkus-1):
            if a[j][1] > a[i][1]:
                a[j],a[i] = a[i],a[j]
            elif a[j][1] == a[i][1]:
                if a[j][0] > a[i][0]:
                    a[j],a[i] = a[i],a[j]