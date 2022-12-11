def järjesta_punktid(n):
    for i in range(len(n)-1):
        min_ = 1
        for j in range(i+1, len(n)):
            if n[j][i] < n[min_]:
                min_=j
            elif n[j][1] == n[min_][1]:
                if n[j][0] < n[min_][0]:
                    min_=j
        if i != min_:
            n[i], n[min_] = n[min_], n[i]
    