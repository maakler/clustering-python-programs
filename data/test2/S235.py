def järjesta_punktid(järjend):
    for i in range(len(järjend)):
        for j in range(i+1, len(järjend)):
            if järjend[i][1] > järjend[j][1]:
                järjend[i], järjend[j] = järjend[j], järjend[i]
            elif  järjend[i][1] == järjend[j][1]:
                if järjend[i][0] > järjend[j][0]:
                    järjend[i], järjend[j] = järjend[j], järjend[i]
            else:
                continue
            

p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]
print(järjesta_punktid(p))