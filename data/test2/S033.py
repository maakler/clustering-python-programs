p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]

def järjesta_punktid(a):
    for i in range(len(a)):
        min = a[i]
        for j in range(i+1, len(a)):
            if a[j][1] < min[1] or (a[j][1] == min[1] and a[j][0] < min[0]):
                min = a[j]
        if a[i] != min:
            x = a.index(min)
            a[i], a[x] = a[x], a[i]

järjesta_punktid(p)
print(p)
    