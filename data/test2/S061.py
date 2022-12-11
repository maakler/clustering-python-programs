def järjesta_punktid(jarjend):
    for i in range(0, len(jarjend) - 1):
        for j in range(i, len(jarjend)):
            if jarjend[j][1] < jarjend[i][1]:
                jarjend[j], jarjend[i] = jarjend[i], jarjend[j]
            if jarjend[j][1] == jarjend[i][1]:
                if jarjend[j][0] < jarjend[i][0]:
                    jarjend[j], jarjend[i] = jarjend[i], jarjend[j]
p = [(1, 4), (6, 4), (4, 4), (3, 4)]
järjesta_punktid(p)
print(p)