# es 30 pag 73
numeroBin = input('Numero binario da convertire in decimale: ')
lunghezzaBin = int(input('Numero cifre del numero binario: '))
contatore = 0
risultato = 0
for c in range(0,lunghezzaBin):
    print(numeroBin)
    cifra = int(input('Cifra del numero binario a partire da destra: '))
    calcolo = cifra * (2**contatore)
    contatore += 1
    risultato += calcolo

print('Il risultato della conversione del numero: ',risultato)
print()
print('Risultato conversione con la funzione: ',int(numeroBin,2))




