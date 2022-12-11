# 2. Järjesta punktid

def järjesta_punktid(järjend):
    for i in range(len(järjend) - 1):
        for j in range(i + 1, len(järjend)):
            if järjend[i][1] > järjend[j][1]:
                järjend[i], järjend[j] = järjend[j], järjend[i]
            elif järjend[i][1] == järjend[j][1]:
                if järjend[i][0] > järjend[j][0]:
                    järjend[i], järjend[j] = järjend[j], järjend[i]

    


järjend = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]
järjesta_punktid(järjend)
print(järjend)