# es 2 scheda
listaParole = []
listaNumeroLettere = []
while True:
    parola = input('Parola che vuole inserire nella lista: ')
    if parola != '*':
        listaParole.append(parola)
    else:
        break

for parola in listaParole:
        numeroLettere = len(parola)
        listaNumeroLettere.append(numeroLettere)

print('Il numero di lettere contenenti nelle parole date sono: ',end='')
for elementi in listaNumeroLettere:
    print(elementi, end=', ')