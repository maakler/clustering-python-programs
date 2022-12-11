def järjesta_punktid(järjend):
    for i in range(len(järjend)):
        #veerg = järjend[i][0]
        #rida = järjend[i][1]
        for j in range(i+1,len(järjend)):
            if järjend[i][1] > järjend[j][1]:
                järjend[i],järjend[j] = järjend[j],järjend[i]
            if järjend[i][1] == järjend[j][1] and järjend[i][0] > järjend[j][0]:
                järjend[i],järjend[j] = järjend[j],järjend[i]
   # return järjend
                
    
    
#järjend = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]

#print(järjesta_punktid(järjend))