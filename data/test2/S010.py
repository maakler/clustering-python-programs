p = [(1, 4), (6, 4), (4, 4), (3, 4)]

def järjesta_punktid(p): # Kasutasin selection sort meetodit ehk valikumeetodit
    for indeks in range(0, len(p)-1):
        #rida=p[indeks][1]
        #veerg=p[indeks][0]
        vähim=indeks
        for j in range(indeks, len(p)):
            if p[j][1]<p[vähim][1]:
                vähim=j
            elif p[j][1]==p[vähim][1] and p[j][0]<p[vähim][0]:
                vähim=j            
        p[indeks], p[vähim]=p[vähim], p[indeks]

järjesta_punktid(p)
print(p)