# es 29 pag 73
listaCitta = []
contatore = 0
valorePrefissato = float(input("Valore prefissato per l'escursione termica: "))
while True:
    citta = input('Nome della città: ')
    if citta != '*':
        listaCitta.append(citta)
        tempMax = float(input('Temperatura massima: '))
        tempMin = float(input('Temperatura minima: '))
        escursione = tempMax - tempMin
        if escursione > valorePrefissato:
            contatore += 1
        else:
            contatore += 0
    else:
        break

print("Le città che hanno l'escursione termica maggiore di", valorePrefissato,' sono: {:7d}'.format(contatore))
