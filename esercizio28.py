# es  28 pag 73
listaLanci = []
while True:
    studente = input('Nome studente: ')
    if studente != '*':
        lancio = float(input('Distanza del lancio: '))
        listaLanci.append(lancio)
    else:
        break

print('Il lancio più lungo è statto di: {:.1f} '.format(max(listaLanci)),' m')

