p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]
def järjesta_punktid(l):
    for j in range(len(l)):
        for i in range(len(l)-1,-1,-1):
            if i == 0:
                pass
            else:
                if l[i][1]>l[i-1][1]:
                    pass
                elif l[i][1]<l[i-1][1]:
                    a = l[i]
                    b = l[i-1]
                    l[i-1]=a
                    l[i]=b
                else:
                    if l[i][0]<l[i-1][0]:
                        a = l[i]
                        b = l[i-1]
                        l[i-1]=a
                        l[i]=b

järjesta_punktid(p)
print(p)