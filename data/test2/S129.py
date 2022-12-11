# järjesta punktid

def järjesta_punktid(arr):
    pikkus = len(arr)
    for i in range(pikkus):
        for j in range(0, pikkus-i-1):
            if arr[j][0] > arr[j+1][0]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            if arr[j][1] > arr[j+1][1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

p = [(4,1),
     (3,3),
     (2,0),
     (6,1),
     (3,2),
     (5,2),
     (1,1)]

järjesta_punktid(p)
print(p)
