def järjesta_punktid(l):
    for el in range(len(l)):  
        for i in range(len(l)-1):
            if l[i][1] > l[i+1][1]:
                l[i+1],l[i] = l[i],l[i+1]
            elif l[i][1] == l[i+1][1] and l[i][0] > l[i+1][0]:
                l[i+1],l[i] = l[i],l[i+1]

p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]
järjesta_punktid(p)
print(p)