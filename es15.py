'''
esercizio 15 

dato un elenco di nazioni contenuto in una lista e uno delle rispettive capitali in una seconda lista (nazione e relativa capitale
si trovano nella medesima posizione delle rispettive liste), visualizza la capitale di una nazione della quale viene fornito da 
tastiera il nome, segnalando con un messaggio di errore il caso in cui la nazione richiesta non sia compresa nell'elenco.
'''

def trova_capitale(l_nazioni, l_capitali):
    # richiesta nome nazione
    richiesta_nazione = input('Nazione della quale si vuole conoscere la capitale: ')

    # controllo se la nazione è nella lista
    if richiesta_nazione not in l_nazioni:
        print()
        print("Errore: la nazione non si trova nell'elenco")
    
    else:
        # trovare la capitale
        capitale = l_capitali[l_nazioni.index(richiesta_nazione)]

        return capitale

def main():
    nazioni = []
    capitali = []
    # richiessta delle nazioni e delle capitali
    while True:
        nazione = input('Nazione (* = fine): ')

        if nazione == '*':
            break

        else:
            capitale = input('Capitale: ')
            # aggiunta delle capitali e delle nazioni nelle liste
            nazioni.append(nazione)
            capitali.append(capitale)

    capitale_nazione = trova_capitale(nazioni,capitali)

    if capitale_nazione == None:
        pass
    else:
        print()
        print(capitale_nazione)

main()


    