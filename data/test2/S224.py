def järjesta_punktid(järjend):
    for i in range(len(järjend)-1):
        for j in range(i+1, len(järjend)):
            if järjend[i][0] > järjend[j][0]:
                järjend[i], järjend[j] = järjend[j], järjend[i]
            if järjend[i][0] == järjend[j][0]:
                if järjend[i][1] > järjend[j][1]:
                    järjend[i], järjend[j] = järjend[j], järjend[i]
            
            
    print(järjend)
    
