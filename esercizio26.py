# es 26 pag 73
# richiestadegli stipendi
stipendio = float(input('Stipendio del dipendente: '))
listaStipendi = []
# aggiunta degli stipendi ad una lista
listaStipendi.append(stipendio)
while True:
    stipendio = float(input('Stipendio del dipendente: '))
    if stipendio != -1:
        listaStipendi.append(stipendio)
    else:
        break

sommaLista = sum(listaStipendi)
media = sommaLista / len(listaStipendi)
# visualizzazione della media degli stipedi
print()
print('Media stipendio dei dipendenti: ',media,' €')