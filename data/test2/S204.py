def järjesta_punktid(a):
    järgmine=1
    eelmine=0
    b=len(a)
    for i in range(0, b):
        for j in range(0,b-1):
            if a[j][järgmine] > a[j+1][järgmine]:
                k = a[j]
                a[j]= a[j+1]
                a[j+1]= k
        for i in range(0, b):
            for j in range(0, b-1):
                if a[j][järgmine] == a[j+1][järgmine] and  a[j][eelmine] > a[j+1][eelmine]:
                    ka = a[j]
                    a[j] = a[j+1]
                    a[j+1] = ka