
def järjesta_punktid(järjend):
    for i in range(len(järjend)):
        for j in range(i+1, len(järjend)):
            if järjend[j][1] < järjend[i][1]:
                järjend[i], järjend[j] = järjend[j], järjend[i]
            elif järjend[j][1] == järjend[i][1]:                   
                if järjend[j][0] < järjend[i][0]:
                    järjend[i], järjend[j] = järjend[j], järjend[i]                  
    #return järjend