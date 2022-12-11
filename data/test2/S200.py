def järjesta_punktid(järjend):
    väärtus = False
    for i in range(1,len(järjend),1):
        if järjend[i-1][1] > järjend[i][1]:
                järjend[i-1],järjend[i] = järjend[i],järjend[i-1]
                väärtus = True
        elif järjend[i-1][1] == järjend[i][1]:
                if järjend[i-1][0] > järjend[i][0]:
                    järjend[i-1],järjend[i] = järjend[i],järjend[i-1]
                    väärtus = True
                    
    if väärtus == True:
        return järjesta_punktid(järjend)