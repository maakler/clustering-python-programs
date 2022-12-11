def järjesta_punktid(a):
    for i in range(len(a)):
        min_index = i
        for j in range(i+1, len(a)):
            if a[min_index][1] > a[j][1]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]