def järjesta_punktid(järjend):
    for i in range(len(järjend)):
        vähim_väärtus_index = i
        for j in range(i + 1, len(järjend)):
            if järjend[j] < järjend[vähim_väärtus_index]:
                vähim_väärtus_index = j
        järjend[i], järjend[vähim_väärtus_index] = järjend[vähim_väärtus_index], järjend[i]
        

p =[(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]
järjesta_punktid(p)
print(p)