'''
esercizio 29 pagina 190

Scrivi un programma che legga un reddito da tastiera e calcoli l'importo dell'imposta sul reddito e la tassazione media.
'''
# funzione per calcolare importo dell'imposta
def calcolo_imposta(d_tassazione, reddito):
    for e in d_tassazione:
        if reddito > e[0] and reddito <= e[1]:
            # calcolo dell'importo dell'imposta
            imposta = d_tassazione[e][1] + (reddito - d_tassazione[e][0]) / 100 * d_tassazione[e][2]

    return imposta

# funzione per calcolare la tassazione media
def calcolo_tassazione(imposta, reddito):
    return imposta / reddito * 100

# funzione main()
def main():
    d_tassazione = {
        (0, 15000) : (0 ,0 , 23),
        (15000, 28000) : (15000, 3450, 28),
        (28000, 55000) : (28000, 6960, 38),
        (55000, 75000) : (55000, 27860, 41),
        (75000, 10**12) : (75000, 58610, 43)
    }

    reddito = float(input('Reddito: '))

    imposta = calcolo_imposta(d_tassazione, reddito)

    # calcolo tassazione media
    tassazione_media = calcolo_tassazione(imposta, reddito)

    print()
    # visualizzazione dei risultati
    print("IMPORTO DELL'IMPOSTA:  {:.2f}".format(imposta), '€')
    print("TASSAZIONE MEDIA: {:.2f} ".format(tassazione_media), '%')
main()