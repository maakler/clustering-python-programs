
def järjesta_punktid(p):
    while True:
        hm=0
        for a in range(len(p)-1):
            if p[a][1]>p[a+1][1]:
                p[a],p[a+1]=p[a+1],p[a]
                hm=1
            if p[a][1]==p[a+1][1]:
                if p[a][0]>p[a+1][0]:
                    p[a],p[a+1]=p[a+1],p[a]
                    hm=1
        if hm==0:
            break
        

