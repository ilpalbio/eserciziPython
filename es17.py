'''
esercizio 17

costruisci un dizionario ottenuto da quello dell'esercizio precedente invertendo il ruolo di chiave e valore. usa il nuovo
dizionario per trovare il nome della nazione, noto il nome dela capitale.
'''
def main():
    dict_capitali = dict()

    # richiessta delle nazioni e delle capitali
    while True:
        nazione = input('Nazione (* = fine): ')

        if nazione == '*':
            break

        else:
            capitale = input('Capitale: ')
            # aggiunta delle capitali e delle nazioni nelle liste
            dict_capitali[capitale] = nazione

    # richiesta della capitale
    trova_nazione = input('Capitale della nazione che si vuole trovare: ')

    nome_nazione = dict_capitali[trova_nazione]

    print(nome_nazione)

main()