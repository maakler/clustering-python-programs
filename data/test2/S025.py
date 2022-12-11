def järjesta_punktid(a):
    for i in range(len(a)):
        m = i
        for j in range(i+1, len(a)):
            if a[j][1] < a[m][1]:
                m = j
            elif a[j][0] < a[m][0] and a[j][1] == a[m][1]:
                m = j
        if i != m:
            a[i], a[m] = a[m], a[i]