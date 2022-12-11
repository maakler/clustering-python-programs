def järjesta_punktid(p):
    for i in range(len(p)):
        min = i
        for j in range(i+1, len(p)):
            if p[j][1] < p[min][1]:
                min = j
            elif p[j][1] == p[min][1] and p[j][0] < p[min][0]:
                min = j
            elif p[j][1] < p[min][1] and p[j][0] == p[min][0]:
                min = j
        if i != min:
            p[i], p[min] = p[min], p[i]
            
p =  [(2, 3), (2, 5), (2, 2), (2, 4)]
järjesta_punktid(p)
print(p)
