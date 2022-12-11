def järjesta_punktid(järjend):
    miinimum =200
    for i in range(0, len(järjend)):
        for j in range(0, len(järjend)-1):
            if järjend[j][1] > järjend[j+1][1]:
                muutuja = järjend[j]
                järjend[j] = järjend[j+1]
                järjend[j+1] = muutuja
                    
    for i in range(0, len(järjend)):
        for j in range(0, len(järjend)-1):
            if järjend[j][1] == järjend[j+1][1]:
                    if järjend[j][0] > järjend[j+1][0]:
                        muutuja = järjend[j]
                        järjend[j] = järjend[j+1]
                        järjend[j+1] = muutuja
                    

          
print(järjesta_punktid([(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]))
