def järjesta_punktid(jär):
    for i in range(len(jär)):
        min=i
        for j in range(i+1,len(jär)):
            if jär[j][1]<jär[min][1]:
                min=j
        if i != min:
            jär[i],jär[min]=jär[min],jär[i]
    for i in range(len(jär)):
        for j in range(len(jär)):
            if jär[j][1]==jär[i][1]:
                if jär[j][0]>jär[i][0]:
                    jär[i],jär[j]=jär[j],jär[i]
    #return jär
p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]
print(järjesta_punktid(p))            