def järjesta_punktid(jär):
    
    for i in range(len(jär)-1):
        for j in range(i+1,len(jär)):
            if jär[i][1]>jär[j][1]:
                jär[i],jär[j]=jär[j],jär[i]
    
    for i in range(len(jär)-1):
        for j in range(i+1,len(jär)):
            if jär[i][0]>jär[j][0] and jär[i][1]==jär[j][1]:
                jär[i],jär[j]=jär[j],jär[i]
    
    