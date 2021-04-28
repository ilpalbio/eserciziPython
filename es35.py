'''
Esercizio 35

Organizza con un dizionario i dati sui conti correnti bancari con numero del conto e saldo. Fornito poi il numero di conto, 
il programma visualizza il saldo oppure un messaggio nel caso in cui il conto non sia presente nella mappa.
'''
def trova_saldo(dict,chiave):
    return dict[chiave] 
def main():
    # crezione di un dizionario vuoto
    conto_corrente = dict()

    # richiesta numero conto e saldo
    while True:
        numero_conto = input('Numero del conto corrente (* = fine): ')

        if numero_conto != '*':
            saldo = float(input('Saldo: '))

            # crezione
            conto_corrente[numero_conto] = saldo

        else:
            break

    print()
    # richiesta numero del conto
    richiesta_conto = input('Nome del conto corrente: ')

    if richiesta_conto in conto_corrente:
       saldo_conto = trova_saldo(conto_corrente,richiesta_conto)

       print('Soldi nel conto corrente: ',saldo_conto,' €')

    else:
        print()
        print('Conto corrente non trovato')
    
main()
        



            

