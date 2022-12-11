def järjesta_punktid(järjend):
    for i in range(len(järjend)):
        for j in range(i + 1, len(järjend)):
            k = 1
            if järjend[i][k] > järjend[j][k]:
                järjend[i], järjend[j] = järjend[j], järjend[i]
            
    for i in range(len(järjend)):
        for j in range(i + 1, len(järjend)):
            if järjend[i][1] == järjend[j][1]:    
                k = 0
                if järjend[i][k] > järjend[j][k]:
                    järjend[i], järjend[j] = järjend[j], järjend[i]
            else:
                break