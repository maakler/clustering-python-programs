
def järjesta_punktid(jrj):
    
    
    for i in range(len(jrj)-1):
        for j in range(len(jrj)-i-1):
            
            if jrj[j][1]>jrj[j+1][1]:
                jrj[j], jrj[j+1] = jrj[j+1], jrj[j]
                
            elif jrj[j][1]==jrj[j+1][1]:
                
                if jrj[j][0]>jrj[j+1][0]:
                    jrj[j], jrj[j+1] = jrj[j+1], jrj[j]
            


p=[(2,3),(3,3),(2,0),(6,1),(3,2),(5,2),(1,1)]

järjesta_punktid(p)

print(p)