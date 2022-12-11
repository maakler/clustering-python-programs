# Järjesta punktid
# Kasutan bubble sort meetodit 

p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]

def järjesta_punktid(p):
    while True:
        swap = False # tsükkel töötab kuni ühtegi vahetust enam ei toimu 
        for i in range(len(p)-1):
            if p[i][1] > p[i+1][1]: # kui y1 > y2, vahetus
                swap = True
                el1 = p[i]
                el2 = p[i+1]
                p[i+1] = el1
                p[i] = el2
            elif p[i][1] == p[i+1][1]: # kui y1 = y2, kontrollime x
                if p[i][0] > p[i+1][0]: # kui x1 > x2, vahetus
                    swap = True
                    el1 = p[i]
                    el2 = p[i+1]
                    p[i+1] = el1
                    p[i] = el2  
        if swap == False:
            break
 
järjesta_punktid(p) 
print(p)