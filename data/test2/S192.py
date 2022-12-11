p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]
def järjesta_punktid(järjend): # Mullsortimine
    n = len(järjend)
    for i in range(n):
        for j in range(0, n-i-1):
            if järjend[j][1] > järjend[j + 1][1]: # Kui teine element on erinevad
                järjend[j], järjend[j + 1] = järjend[j + 1], järjend[j]
            elif järjend[j][1] == järjend[j + 1][1]: # Kui teine element on võrdsed
                if järjend[j] > järjend[j + 1]: # Siis võrdle esimese elemendi järgi
                    järjend[j], järjend[j + 1] = järjend[j + 1], järjend[j]