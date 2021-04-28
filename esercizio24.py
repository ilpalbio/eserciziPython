# es 24 pag 73
# richiesta dei nomi e dei voti ottenuti
nome1 = input('Nome primo candidato: ')
punteggio1 = int(input('Numero voti: '))
nome2 = input('Nome secondo candidato: ')
punteggio2 = int(input('Numero voti: '))
# calcolo della percentuale
sommaVoti = punteggio1 + punteggio2
percentuale1 = punteggio1 / sommaVoti * 100
percentuale2 = punteggio2 / sommaVoti * 100
# comunicazione vincitore e percentuali
if punteggio1 > punteggio2:
    print('Il vincitore è: ',nome1)
elif punteggio2 > punteggio1:
    print('Il vincitore è: ',nome2)
else:
    print('Pareggio dei voti')
# percentuali dei voti con 0 cifre decimali
print('Percentuale voti primo candidato:','{:.0f}'.format(percentuale1),'%')
print('Percentuale voti secondo candidato: ','{:.0f}'.format(percentuale2),'%')



