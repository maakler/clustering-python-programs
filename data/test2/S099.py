def järjesta_punktid(p):
#     for i in range(len(a)):
#         min = i
#         for j in range(i+1, len(a)):
#             if a[j] < a[min]:
#                 min = j
#             if i != min:
#                 a[i], a[min] = a[min], a[i]
    for i in range(len(p)-1):
        for j in range(i+1, len(p)):
            if p[j][1] < p[i][1]:
                p[i], p[j] = p[j], p[i]
            elif p[j][1] == p[i][1] and p[j][0] < p[i][0]:
                p[i], p[j] = p[j], p[i]
                
                
p = [(4,1),(3,3),(2,0),(6,1),(3,2),(5,2),(1,1)]
järjesta_punktid(p)     
print(p)


