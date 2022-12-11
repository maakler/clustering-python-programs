def järjesta_punktid(järjend):
    for i in range(len(järjend)):
        for j in range(i+1, len(järjend)):
            if järjend[i] > järjend[j]: 
                järjend[i], järjend[j] = järjend[j], järjend[i]
            if järjend[i][1] > järjend[j][1]:
                järjend[i], järjend[j] = järjend[j], järjend[i]