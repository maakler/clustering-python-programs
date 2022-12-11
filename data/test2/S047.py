def järjesta_punktid(järjend):
    n = len(järjend)
    
    for i in range(n-1):
        for j in range(0, n-i-1):
            if järjend[j][1] > järjend[j + 1][1]:
                järjend[j], järjend[j + 1] = järjend[j + 1], järjend[j]
            
            elif järjend[j][1] == järjend[j + 1][1] and järjend[j][0] > järjend[j + 1][0]:
                    järjend[j], järjend[j + 1] = järjend[j + 1], järjend[j]
    return järjend

p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]
print(järjesta_punktid(p))
 