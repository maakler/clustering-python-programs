def järjesta_punktid(jär):
    n = len(jär)
    for i in range(n):
        for j in range(n-i-1):
            if (jär[j][1] > jär[j+1][1]):
                suurem = jär[j]
                jär[j] = jär[j+1]
                jär[j+1] = suurem
    for x in range(n):
        for y in range(n-x-1):
            if jär[y][1]==jär[y+1][1]:
                if jär[y][0]>jär[y+1][0]:
                    suurem=jär[y]
                    jär[y]=jär[y+1]
                    jär[y+1]=suurem
                
järjend=[(4,1),(3,3),(2,0),(6,1),(3,2),(5,2),(1,1)]
järjesta_punktid(järjend)
print(järjend)