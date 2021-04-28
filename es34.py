'''
esercizio 34

Le prenotazioni per la partecipazione a un convegno sono memorizzate secondo l'ordine di arrivo (suggermento: utilizza una struttura
di coda per memorizzare i dati dei partecipanti). Scrivi un programma che comprenda due funzionalità:

- l'operazione per registrare i dati dei partecipanti;
- l'operatore per visualizzare i nomi dei partecipanti a cui si deve inviare una lettera di conferma: si tratta dei nomi dell'elenco,
eliminando quelli ai quali la lettera è già stata inviata e che sono registrati in un apposito elenco. La funzione che produce 
l'elenco deve anche aggiornare l'elenco dei partecipanti ai quali è già stata inviata la lettera
'''
def verifica_partecipanti(nome, invito, partecipanti_con, partecipanti_senza):
    if invito == 'si':
        partecipanti_con.append(nome)

    elif invito == 'no':
        partecipanti_senza.append(nome)

    else:
        print('Risposta non accettata')

def main():
    partecipanti_con = []
    partecipanti_senza = []

    # richiesta dei nomi dei partecipanti
    while True:
        nome = input('Nome partecipante (* = fine): ')

        if nome != '*':
            invito = input('Ha ricevuto la lettera? ').lower()
            verifica_partecipanti(nome, invito, partecipanti_con, partecipanti_senza)
            print()

        else:
            break

    print()
    # visualizzazione delle liste
    print('Persone che hanno ricevuto la lettera')
    for persone in partecipanti_con:
        print(persone.capitalize(), end = ' ')

    print()
    print()
    
    print('Persone che non hanno ricevuto la lettera')
    for persone in partecipanti_senza:
        print(persone.capitalize(), end = ' ')
main()
 