'''
esercizio 14

Organizza in una struttura di dati i valori degli occupati negli ultimi 10 anni. Utilizza un dizionario, 
assegnando il ruolo di chiave all'anno. Inserisci i dati da tastiera e memorizzali nel contenitore. Calcola poi il valore medio 
dei dieci anni e visualizza il risultato.
'''
from statistics import mean as m

def richiedi_info(dizionario, lista):
    for i in range(10):
        anno = input('Anno (* = fine): ')

        if anno == '*':
            break

        else:
            occupati = int(input('Occupati: '))

            dizionario[anno] = occupati
            lista.append(occupati)

def calcola_media(lista):
    return m(lista)

def main():
    l_occupati = []
    d_anno = dict()

    richiedi_info(d_anno, l_occupati)

    media_occupati = calcola_media(l_occupati)

    print()
    print('La media degli occupati è: ', media_occupati)

main()
