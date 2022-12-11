#Järjestab koordinaatpunktid

p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]


def järjesta_punktid(järjend):
    for n in range(len(järjend)):
        for i in range(len(järjend)-1):
            if järjend[i][1] > järjend[i+1][1]:
                järjend[i], järjend[i+1] = järjend[i+1], järjend[i]
            if järjend[i][1] == järjend[i+1][1] and järjend[i][0] > järjend[i+1][0]:
                järjend[i], järjend[i+1] = järjend[i+1], järjend[i]


#print(p)
#järjesta_punktid(p)
#print(p)