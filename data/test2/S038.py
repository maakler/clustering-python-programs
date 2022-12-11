
def  järjesta_punktid(a):
    ind = 1
    jnd = 0
    for i in range(0, len(a)):
        for j in range(0, len(a)-1):
            if a[j][ind] > a[j+1][ind] :
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
    for i in range(0, len(a)):
        for j in range(0, len(a)-1):
            if a[j][ind] == a[j+1][ind]:
                if a[j][jnd] > a[j+1][jnd] :
                    tempo = a[j]
                    a[j] = a[j+1]
                    a[j+1] = tempo

