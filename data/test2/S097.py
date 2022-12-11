def järjesta_punktid(järjend):
    for i in range(len(järjend)):
        for j in range(i+1, len(järjend)):
            if järjend[j][1] < järjend[i][1]:
                järjend[j], järjend[i] = järjend[i], järjend[j]
            elif järjend[j][1] == järjend[i][1]:
                if järjend[j][0] < järjend[i][0]:
                    järjend[j], järjend[i] = järjend[i], järjend[j]
            else:
                continue

p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]
järjesta_punktid(p)
print(p)
                