def järjesta_punktid(p):
    for i in range(len(p)):
        for j in range(len(p)):
            if p[i][1]<p[j][1]:
                p[i],p[j]=p[j],p[i]
                
    for i in range(len(p)):
        for j in range(len(p)):
            if p[i][1]==p[j][1] and p[i][0]<p[j][0]:
                p[i],p[j]=p[j],p[i]
