def järjesta_punktid(järjend):
    n = len(järjend)
    for i in range (n-1):
        for j in range(0,n-i-1):
            if järjend[j] < järjend[j+1]:
                järjend[j+1], järjend[j] = järjend[j], järjend[j+1]