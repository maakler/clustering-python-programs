def järjesta_punktid(järjend):
    for i in range(len(järjend)):
        for j in range(len(järjend)- i - 1):
            if järjend[j][1] > järjend[j + 1][1]:
                järjend[j], järjend[j + 1] = järjend[j + 1], järjend[j]
            else:
                if järjend[j][1] == järjend[j + 1][1]:
                    if järjend[j][0] > järjend[j + 1][0]:
                        järjend[j], järjend[j + 1] = järjend[j + 1], järjend[j]

jär = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]
print(järjesta_punktid(jär))