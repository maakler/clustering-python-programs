
def järjesta_punktid(järjend):
    for i in range(len(järjend)):
        min = i
        for j in range(i+1,len(järjend)):
            if järjend[j] < järjend[min]:
                min = j
        if i != min:
            järjend[i],järjend[min] = järjend[min],järjend[i]
    for i in range(0,len(järjend)):
        for j in range(0,len(järjend)-i-1):
            if järjend[j][-1] > järjend[j+1][-1]:
                t = järjend[j]
                järjend[j] = järjend[j+1]
                järjend[j+1] = t
                
                


p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]
järjesta_punktid(p)
print(p)
