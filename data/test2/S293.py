x = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (5,1), (1,1)]
#https://et.wikipedia.org/wiki/Valiksortimine
def järjesta_punktid(x):
    for i in range(0, len(x)-1):
        s = i
        for j in range(i, len(x)):
            if x[j][1] < x[s][1]:
                s = j
        x[i], x[s] = x[s], x[i]
        
    for i in range(0, len(x)-1):
        s=i
        for j in range(i, len(x)):
            if x[i][1]==x[j][1]:
                if x[i][0]>x[j][0]:
                    s=j
                    x[i] , x[j]=x[j], x[i] 
            else:
                continue
    
        

    
    