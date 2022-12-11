
def järjesta_punktid(p):
    # sorteeri kaks korda, sest igal elemendil on 2 punkti
    for k in range(2):
        # kasutan muudetud mullimeetodit sorteerimiseks
        sorteeritud = False
        while not sorteeritud:
            for i in range(len(p)-1):
                # jäta element meelde, vastasel korral
                # muudaksime kõik järjendi elemendid
                # ühesuguseks
                backup = p[i+1]
                if p[i][k] > p[i+1][k]:
                    p[i+1] = p[i]
                    p[i] = backup
            # kontrolli, kas järjend on sorteeritud
            sorteeritud = True
            for i in range(len(p)-1):
                if p[i][k] > p[i+1][k]:
                    sorteeritud = False
                    break
        
