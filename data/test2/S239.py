def järjesta_punktid(l):
    for i in range(len(l)-1,0,-1):
        for j in range(i):
            if l[j][1]>l[j+1][1]:
                x=l[j]
                l[j]=l[j+1]
                l[j+1]=x
            elif l[j][1]==l[j+1][1]:
                if l[j][0]>l[j+1][0]:
                    x=l[j]
                    l[j]=l[j+1]
                    l[j+1]=x
                
    return l


p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]
print(järjesta_punktid(p))