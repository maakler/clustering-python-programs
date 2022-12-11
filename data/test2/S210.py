def järjesta_punktid(p):
    p = sorted(p, key=lambda t: (t[1], t[0]))
    print(p)
p = [(1,2),(2,1)]
järjesta_punktid(p)