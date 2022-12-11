def järjesta_punktid(a):
    for i in range(len(a)):
        min=i
        for j in range(i+1, len(a)):
            if a[j][1]<a[min][1]:
                min=j
            elif a[j][1]==a[min][1]:
                if a[j][0]<a[min][0]:
                    min=j                    
        if i!=min:
            a[i], a[min] = a[min], a[i]
p=[(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]
järjesta_punktid(p)
print(p)