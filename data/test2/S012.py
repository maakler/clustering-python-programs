#kodu 2 - järjesta punktid
def järjesta_punktid(p):
    for i in range(len(p)):
        min_y = p[i]
        min_x = p[i]
        for j in range(i+1, len(p)):
            if min_y[1] > p[j][1]:
                min_y = p[j]
            elif min_y[1] == p[j][1]:
                if min_x[0] > p[j][0]:
                    min_y = p[j]
        indeks = p.index(min_y)           
        p[i], p[indeks] = p[indeks], p[i]
p = [(1, 4), (6, 4), (4, 4), (3, 4)]
järjesta_punktid(p)
print(p)