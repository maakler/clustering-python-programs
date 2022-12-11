p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]

def järjesta_punktid(järj):
    for i in range(1, len(järj)):
        key = järj[i]
        j = i-1
        while j >=0 and järj[i][1] < järj[j][1] :
            järj[j+1] = järj[j]
            j -= 1
        järj[j+1] = key
        
    return järj

print(järjesta_punktid(p))

#NB! ülesanne ei tulnud täiesti korrektselt välja