'''
esercizio 28 pagina 190

I nomi delle città e i corrispondenti Codici di Avviamento Postale (CAP) vengono inseriti da tastiera e memorizzati in un
dizionario, dove il CAP è la chiave. Fornito poi da tastiera il nome di una città, costruisci un programma che visualizzi il suo CAP
oppure un messaggio nel caso la città non sia compresa nell'elenco. Analogamente, fornendo il CAP restituisce il nome della città 
oppure un messaggio di errore.
'''
# definizione della funzione pr creare un dizionario
def crea_dizionario(dict_cap, dict_citta):
    while True:
        citta = input('Nome della città (* = fine richiesta): ')

        if citta == '*':
            break

        else:
            cap = input('CAP città: ')
            dict_cap[cap] = citta
            dict_citta[citta] = cap



def trova_valore(dizionario, chiave):
    return dizionario[chiave]

def main():
    # dizionario con chiave il CAP
    dict_cap = dict()
    dict_citta = dict()

    # aggiunta di elementi al dizionario vuoto
    crea_dizionario(dict_cap, dict_citta)

    print()
    # richiesta della città
    citta = input('Città di cui si vuole conoscere il CAP: ')

    if citta in dict_citta:
        # visualizzazione del CAP
        cap = trova_valore(dict_citta, citta)
        print('Il CAP della città ',citta.capitalize(),' è ',cap)

    else:
        print('Questa città non è presente')

    print()
    # richiesta del cap
    cap = input('CAP della città che si vuole conoscere: ')

    if cap in dict_cap:
        # visualizzazione città
        citta = trova_valore(dict_cap, cap)
        print('La città con CAP ',cap.capitalize(), ' è ', citta)

    else:
        print('Questo CAP non è presente')

main()


