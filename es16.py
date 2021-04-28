'''
esercizio 16

risolvi il problema precedente partendo da due liste che generano un dizionario con la nazione come chiave e la capitale come valore.
Successivamente interroga il dizionario per visulaizzare la capitale di una nazione.
'''
def crea_dizionario(l_nazioni,l_capitali,dict_nazioni):
    for chiavi in l_nazioni:
        for valori in l_capitali:
            dict_nazioni[chiavi] = valori
            l_capitali.remove(valori)
            break

def main():
    nazioni = []
    capitali = []
    dict_nazioni = dict()
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

    # creare il dizionario
    crea_dizionario(nazioni,capitali,dict_nazioni)

    print(dict_nazioni)

    print()
    # richiesta della nazione per la capitale
    trova_capitale = input('Nazione di cui si vuole conoscere la papitale: ')

    # trovare la capitale
    capitale_nazione = dict_nazioni[trova_capitale]

    print(capitale_nazione)

main()