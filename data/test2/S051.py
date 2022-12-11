# Valisin pistemeetodi.
def järjesta_punktid(koordinaadid):
    for i in range(1, len(koordinaadid)):
        võti = koordinaadid[i]
        j = i-1
        while j >= 0 and võti[1] <= koordinaadid[j][1]:
            if võti[1] == koordinaadid[j][1] and koordinaadid[j][0] < võti[0]:
                break
            else:
                koordinaadid[j+1] = koordinaadid[j]
                j -= 1
        koordinaadid[j+1] = võti

p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]
järjesta_punktid(p)
print(p)