test = 'aa'
match test:
    case 'a':
        print('aahh')
    case 'aa':
        print('aaahhhhhh')

fail = open(input("Sisesta failinimi: "), "r", encoding="utf-8")
plaan = []

for rida in fail:
    rida = rida.strip().split()
    plaan.append(rida)

fail.close()

halb = []
for aeg in range(len(plaan)):
    valja = plaan[aeg][0].split(":")
    valja = 100*int(valja[0])+int(valja[1])
    saabumine = plaan[aeg][1].split(":")
    saabumine = 100*int(saabumine[0])+int(saabumine[1])
    for aeg2 in range(len(plaan)):
        valja2 = plaan[aeg2][0].split(":")
        valja2 = 100*int(valja2[0])+int(valja2[1])
        saabumine2 = plaan[aeg2][1].split(":")
        saabumine2 = 100*int(saabumine2[0])+int(saabumine2[1])
        if valja < valja2 and saabumine > saabumine2 and int(plaan[aeg][2]) > int(plaan[aeg2][2]):
            halb.append(aeg)

for el in halb[::-1]:
    plaan.pop(el)

for sobib in plaan:
    print(sobib[0], sobib[1], sobib[2])