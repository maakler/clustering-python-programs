# 2. Järjesta punktid / RP

p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1), (10,1), (1,10),(2,1),(3,1),(7,1),(4,1),(5,1)]

def järjesta_punktid(järjend):
    
    for indeks in range(len(järjend)): # Järjesta y-kordinaadid
        miinimum = indeks
        for uus in range(indeks+1, len(järjend)):
            if järjend[miinimum][1] > järjend[uus][1]:
                miinimum = uus        
        järjend[indeks], järjend[miinimum] = järjend[miinimum], järjend[indeks]
        
    for indeks in range(len(järjend)): # Järjesta x-kordinaadid
        miinimum = indeks
        for uus in range(indeks+1, len(järjend)):
            if järjend[miinimum][0] > järjend[uus][0] and järjend[miinimum][1] == järjend[uus][1]:
                miinimum = uus        
        järjend[indeks], järjend[miinimum] = järjend[miinimum], järjend[indeks]
        
        
järjesta_punktid(p)
print(p)