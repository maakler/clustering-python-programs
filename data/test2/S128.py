def järjesta_punktid(järjend):
    for i in range(len(järjend)-1):
        for j in range(len(järjend)-i-1):
            if järjend[j][1] > järjend[j+1][1]:
                järjend[j], järjend[j+1] = järjend[j+1], järjend[j]
            elif järjend[j][0] > järjend[j+1][0] and järjend[j][1] == järjend[j+1][1]:
                järjend[j], järjend[j+1] = järjend[j+1], järjend[j]
