# es 1 scheda
parola = input('Parola da verificare: ')
listaparola = list(parola)
listaInvertita = []

for lettere in listaparola:
    listaInvertita.append(lettere)

listaInvertita.reverse()
if listaparola == listaInvertita:
    print('La parola', parola,'è palindroma')
else:
    print('La parola', parola, 'NON è palindroma')