
p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]
def järjesta_punktid():
    global p
    return sorted(p, key=lambda k: [k[1], k[0]])


print(järjesta_punktid())

