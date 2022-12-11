def järjesta_punktid(punktid):
    muutused = 1
    while muutused != 0:
        muutused = 0
        for indeks in range(len(punktid)-1):
            if punktid[indeks][1] > punktid[indeks+1][1] or punktid[indeks][0] > punktid[indeks+1][0] and punktid[indeks][1] == punktid[indeks+1][1]:
                punkt1 = punktid[indeks]
                punkt2 = punktid[indeks+1]
                punktid[indeks] = punkt2
                punktid[indeks+1] = punkt1
                muutused = 1
                print(punkt1, punkt2)

"""
p = [(1, 4), (6, 4), (4, 4), (3, 4)]

järjesta_punktid(p)

print(p)"""