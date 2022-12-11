
def järjesta_punktid(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j][1] > arr[j + 1][1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j][1] == arr[j + 1][1] :
                if arr[j][0] > arr[j + 1][0] :
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
 
arr = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]

järjesta_punktid(arr)
print(arr)
