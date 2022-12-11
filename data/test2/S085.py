def järjesta_punktid(n):
    for i in range(len(n)):
        for j in range(0,len(n)-i-1):
            if (n[j][1] > n[j+1][1]):
                a = n[j]
                n[j]=n[j+1]
                n[j+1]=a
            elif n[j][1]==n[j+1][1]: 
                if(n[j][0] > n[j+1][0]):
                    a = n[j]
                    n[j]=n[j+1]
                    n[j+1]=a
                    