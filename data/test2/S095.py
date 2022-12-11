p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]
def järjesta_punktid(p):
#ei saanud selle valemiga õiget vastus
#     for i in range(len(p)):
#         min_i=i
#         for j in range(i+1, len(p)):
#             if p[min_i][1]>p[j][1]:
#                 min_i=j
#             elif p[min_i][1]=p[j][1]:
#                 p[min_i]=p[j]
#         p[i],p[min_i]=p[min_i],p[i]
    p = sorted(p, key=lambda t: (t[1], t[0]))
    return p
print(järjesta_punktid(p))

#https://pythonguides.com/python-sort-list-of-tuples/