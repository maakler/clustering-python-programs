#Mullimeetod
def järjesta_punktid(p):
    n = len(p)
     
    for i in range(n):
        for j in range(0+i, n):
            if p[i][1] > p[j][1]:
                p[i], p[j] = p[j], p[i]
            
    for i in range(n):
        for j in range(0+i, n):
            if p[i][1] == p[j][1]:
                if p[i][0] > p[j][0]:
                    p[i], p[j] = p[j], p[i]
    
