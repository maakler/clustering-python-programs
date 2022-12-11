p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]
def järjesta_punktid(järjend):
    tühi = []
    pikkus = len(järjend)-1
    i = 0
    for j in range(pikkus):
        for i in range(pikkus):
            if järjend[i][1] > järjend[i+1][1]:
                järjend[i], järjend[i+1] = järjend[i+1], järjend[i]
                if i == 5:
                    tühi.append(järjend)
            elif järjend[i][1] == järjend[i+1][1]:
                järjend[i], järjend[i+1] = järjend[i], järjend[i+1]
                if i == 5:
                    tühi.append(str(järjend))
    print(tühi)
järjesta_punktid(p)