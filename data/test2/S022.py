p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]

def järjesta_punktid(a):
    for i in range(len(a)):
        min = i
        for j in range(i+1, len(a)):
            if a[j][1] < a[min][1]:
                min = j
        if i != min:
            a[i],a[min] = a[min],a[i]
    
    for i in range(len(a)):
        min = i
        for j in range(i+1, len(a)):
            if a[j] < a[min] and a[j][1] == a[min][1]:
                min = j
        if i != min:
            a[i],a[min] = a[min],a[i]
    
    print(a)

järjesta_punktid(p)