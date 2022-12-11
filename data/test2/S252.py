def järjesta_punktid(järjend):
    n = len(järjend)
    for i in range(n-1):
        kontroll = 0
        for j in range(n-1):
            if järjend[j] > järjend [j + 1]:
                tmp = järjend[j]
                järjend[j] = järjend[j+1]
                järjend[j+1] = tmp
                kontroll = 1
                
            
        if kontroll == 0:
            break
    return järjend



p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]

result = järjesta_punktid(p)
print(result)
