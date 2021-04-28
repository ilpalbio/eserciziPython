# es 31 pag 73
numeroDec = int(input('Numero decimale che si vuole convertire in binario: '))
listaCifre = []
numeroBin = 0
listaCifre.append(numeroDec % 2)
while numeroDec != 1:
    numeroDec //= 2
    listaCifre.append(numeroDec % 2)

listaCifre.reverse()

print('Il risultato della conversione del numero: ',end='')
for c in listaCifre:
    print(c,end='')






