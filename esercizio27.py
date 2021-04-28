# es 27 pag 73
# richiesta del numero dei veicoli transitati
# giorni della settimana
listaGiorni = [' Lunedì',' Martedì',' Mercoledì',' Giovedì',' Venerdì',' Sabato',' Domenica']
listaVeicoli = []
numeroGiorno = 0
nVeicoli = int(input('Numero di veicoli transitati'+ listaGiorni[numeroGiorno] + ' :'))
numeroGiorno += 1
listaVeicoli.append(nVeicoli)
while True:
    nVeicoli = int(input('Numero di veicoli transitati'+ listaGiorni[numeroGiorno] + ' :'))
    # controllo giorni della settimana
    if numeroGiorno != 6:
        numeroGiorno += 1
    else:
        numeroGiorno = 0
    # controllo numero di veicoli
    if nVeicoli != 0:
        listaVeicoli.append(nVeicoli)
    else:
        break

# numero veicoli transitati
sommaVeicoli = sum(listaVeicoli)
# visualizzazione veicoli
print()
print('Il numero di veicoli transitati sono: ',sommaVeicoli)


