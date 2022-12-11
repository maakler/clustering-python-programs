a = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]
for i in range(len(a)):
    min = i
    for j in range(1+i, len(a)):
        if a[j][1] < a[min][1]:
            min = j
        if a[j][1] == a[min][1]:
            ####srav 2 el i togda v]ravnivaju

    a[i], a[min] = a[min], a[i]
print(a)