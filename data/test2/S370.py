def järjesta_punktid(a):
    for i in range(len(a)-1):
        for j in range (i+1, len(a)):
            if a[i][1]>a[j][1] or a[i][1]==a[j][1] and a[i][0]>a[j][0]:
                a[i],a[j]=a[j],a[i]
                    
