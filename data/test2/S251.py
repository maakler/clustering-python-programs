#teen selection sort eeskujul
def järjesta_punktid(p):
    for i in range(len(p)):
        esimene = int( str(p[i][1]) + str(p[i][0]))
        väikseim = esimene
        asukoht = i
        
        for j in range(i+1,len(p)):
            teine = int( str(p[j][1]) + str(p[j][0]))
            
            if teine < väikseim:
                asukoht = j
                väikseim = teine
        
        p[i], p[asukoht] = p[asukoht], p[i]
        

p = [(1,2), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]

järjesta_punktid(p)