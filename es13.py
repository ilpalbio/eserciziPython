'''
esercizio 13

Acquisisci da tastiera un elenco di parole , memorizzandole in una lista, finchè l'utente segnala la fine dell'inserimento con un
asterisco *. Viusalizza alla fine il numero delle parole memorizzate. Ordina alfabeticamente la lista delle parole e visualizzala ,
odinata in modo crescente e decrescente.
'''
def richiedi_parole(lista):
    while True:
        parola = input('Parola (* = fine): ').lower()

        if parola == '*':
            break

        else:
            lista.append(parola)

def visualizza_lista(lista):
    lista.sort()

    print()
    print('Lista crescente')
    # lista crescente
    for e in lista:
        print(e.capitalize())

    lista.reverse()

    print()
    print('Lista decrescente')
    for e in lista:
        print(e.capitalize())


def main():
    l_parole = []

    # richiesta delle parole
    richiedi_parole(l_parole)

    # visualizzazione della lista
    visualizza_lista(l_parole)

main()