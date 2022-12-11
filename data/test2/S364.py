def järjesta_punktid(jar):
    for i in range(0, len(jar)-1):
        for j in range(i,len(jar)):
            if jar[j][1] < jar[i][1]:
                jar[j], jar[i] = jar[i], jar[j]
            elif jar[j][1] == jar[i][1]:
                if jar[j][0] < jar[i][0]:
                    jar[j], jar[i] == jar[i], jar[j]
            
        
p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]
järjesta_punktid(p)
print(p)