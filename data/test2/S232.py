def järjesta_punktid(järjend): #mullimeetod ehk bubble sort
    pikkus = len(järjend)
    for i in range(pikkus - 1):
        for j in range(0, pikkus-i-1):
            if järjend[j][1] > järjend[j+1][1]:
                järjend[j], järjend[j+1] = järjend[j+1], järjend[j]
    for i in range(pikkus - 1):
        for j in range(0, pikkus-i-1):
            if järjend[j][0] > järjend[j+1][0] and järjend[j+1][1] == järjend[j][1]:
                järjend[j], järjend[j+1] = järjend[j+1], järjend[j]
p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]
järjesta_punktid(p)
print(p)