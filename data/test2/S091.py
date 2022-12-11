def järjesta_punktid(jarjend):
    for i in range(len(jarjend)):
        for j in range(len(jarjend)-i-1):
            if jarjend[j][1] > jarjend[j+1][1]: 
                jarjend[j], jarjend[j+1] = jarjend[j+1], jarjend[j]
            else:
                if jarjend[j][1]==jarjend[j+1][1]:
                    if jarjend[j][0] > jarjend[j+1][0]:
                        jarjend[j], jarjend[j+1] = jarjend[j+1], jarjend[j]

            
p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]
print(järjesta_punktid(p))