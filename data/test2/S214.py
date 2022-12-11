#bubble sort
def järjesta_punktid(järjend):
    for i in range(len(järjend)):
        for j in range(len(järjend)-1):
            if järjend[j][1] > järjend[j+1][1]:
                järjend[j], järjend[j+1] = järjend[j+1], järjend[j]
            elif järjend[j][1] == järjend[j+1][1]:
                if järjend[j][0] > järjend[j+1][0]:
                    järjend[j], järjend[j+1] = järjend[j+1],järjend[j]