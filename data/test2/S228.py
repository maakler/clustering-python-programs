#alguses vaatan y järgi, siis x
def järjesta_punktid(p):
    for ennik in range(len(p)): #vaatan läbi järjendis olevad ennikud
        miinimum = p[ennik][1]
        for j in range(ennik+1, len(p)):
            if p[j][1] < p[ennik][1]: 
                miinimum = j
                p[ennik], p[miinimum] = p[miinimum], p[ennik]
            if p[j][1] == p[ennik][1]: #kui y on võrdsed
                miinimum = p[ennik][0]
                if p[j][0] < p[ennik][0]:
                    miinimum = j
                    p[ennik], p[miinimum] = p[miinimum], p[ennik]

p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]

järjesta_punktid(p)
print(p)