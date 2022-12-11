def järjesta_punktid(järjend):
    for võrreldav1 in range(len(järjend)):
        mini = võrreldav1
        
        for võrreldav2 in range(võrreldav1 + 1,len(järjend)):
            if järjend[võrreldav1][1] >= järjend[võrreldav2][1]:
                
                if järjend[võrreldav1][0] > järjend[võrreldav2][0]:
                    
                    if järjend[võrreldav2][1] <= järjend[mini][1]:
                        if järjend[võrreldav2][0] < järjend[mini][0]:
                            mini = võrreldav2
                
        if võrreldav1 != mini:
                järjend[võrreldav1], järjend[mini] = järjend[mini], järjend[võrreldav1]
                
    
    return järjend
                
    
print(järjesta_punktid([(4,1),(3,3),(2,0),(6,1),(3,2),(5,2),(1,1)]))