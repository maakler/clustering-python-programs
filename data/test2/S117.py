#alustasin 08.12.2021 (17:03)
def järjesta_punktid(jarjend):
    for i in range(len(jarjend)):
        mini = i
        for j in range(i + 1, len(jarjend)):
            if jarjend[j][1] < jarjend[mini][1]:
                mini = j
            if jarjend[j][1] == jarjend[mini][1]:
                if jarjend[j][0] < jarjend[mini][0]:
                    mini = j
        jarjend[i], jarjend[mini] = jarjend[mini], jarjend[i]