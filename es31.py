'''
esercizio 31 pagina 191

Un'azienda vende prodotti in tutta italia e la rete di vendita è suddivisa in 4 zone: Nord, Centro, Sud, Isole. Dopo aver acquisito
in un array il fatturato nelle 4 zone, calcola:
- il totale fatturato
- i valori in percentuale delle vendite nelle quattre zone rispetto al totale
'''
def chiedi_fatturato(l_zone, l_fatturato):
    for e in l_zone:
        fatturato = float(input('Fatturato ' + e + ' : '))
        l_fatturato.append(fatturato)

def calcola_percentuale(totale, fatturato):
    return totale / 100 * fatturato

def main():
    # liste
    l_fatturato = []
    l_zone = ['Nord', 'Centro', 'Sud', 'Isola']

    # richiesta del fatturato
    chiedi_fatturato(l_zone, l_fatturato)

    # calcolo somma fatturato
    tot_fatturato = sum(l_fatturato)
    print()
    print('Fatturato totale: ', tot_fatturato)
    print()
    # calcolo della percentuale
    for e in l_fatturato:
        perc_fatturato = calcola_percentuale(tot_fatturato, e)
        print('Fatturato ',l_zone.pop(0),' è ', perc_fatturato, ' %')
    
main()