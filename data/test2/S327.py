def järjesta_punktid(koordinaadid):
    n = len(koordinaadid)
    
    for i in range(n-1):
        for j in range(0, n-i-1):
            if koordinaadid[j][1] > koordinaadid[j+1][1]:
                koordinaadid[j], koordinaadid[j + 1] = koordinaadid[j + 1], koordinaadid[j]
    
    for i in range(n-1):
        for j in range(0, n-i-1):
            if koordinaadid[j][0] > koordinaadid[j+1][0] and koordinaadid[j][1] == koordinaadid[j+1][1]:
                koordinaadid[j], koordinaadid[j + 1] = koordinaadid[j + 1], koordinaadid[j]
