
def järjesta_punktid(p):
    for i in range(0, len(p)-1):
        s = i
        tühi = []
        
        for j in range(i, len(p)):
            if p[j] < p[s]:
                s = j
                p[i], p[s] = p[s], p[i]
        for el in range(i, len(p)):
            if p[el][1] < p[j][1]:
                j = el
                p[s], p[i] = p[i], p[j]
            
        
                        
            
                    
        
    return p
print(järjesta_punktid([(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]))