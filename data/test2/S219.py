# def selection_sort(A):
#     for i in range(0, len(A)-1):
#         s = i
#         for j in range(i, len(A)):
#             if A[j] < A[s]:
#                 s = j
#         A[i], A[s] = A[s], A[i]

p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]

def järjesta_punktid(järjend):
    for i in range(0, len(järjend)-1):
        s = i
        for j in range(i, len(järjend)):
            if järjend[j] < järjend[s]:
                s = j
        for j in range(i, len(järjend)):
            if järjend[j][1] < järjend[s][1]:
                s = j
        järjend[i], järjend[s] = järjend[s], järjend[i]
        
järjesta_punktid(p)
print(p)