def järjesta_punktid(jrj):
    for i in range(0, len(jrj)-1):
        s = i
        for j in range(i, len(jrj)):
            if jrj[j][1] < jrj[s][1]:
                s = j
        jrj[i], jrj[s] = jrj[s], jrj[i]
        
    for a in range(0, len(jrj)-1):
        x = a
        for b in range(a, len(jrj)):
            if jrj[b][1] == jrj[x][1]:
                if jrj[b][0] < jrj[x][0]:
                    x = b
        jrj[a], jrj[x] = jrj[x], jrj[a]
        

    return jrj
            
p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]
print(järjesta_punktid(p))