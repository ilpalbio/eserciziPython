'''
esercizio 27 pagina 190

Organizza con un dizionario la rubrica con i nomi delle persone e i rispettivi numeri telefonici. Fornito poi il nome della persona,
il programma visualizza il suo numero di telefono oppure un messaggio nel caso la persona non sia presente nella rubrica
'''

# definizione della funzione per l'aggiunta di elementi al dizionario vuoto
def crea_dizionario(dizionario):
    while True:
        # richiesta ome della persona
        nome = input('Nome persona (* = fine richiesta): ')

        if nome == '*':
            break

        else:
            # richiesta del numero di telefono
            n_telefono = input('Numero di telefono: ')
            # creazione del dizionario 
            dizionario[nome] = n_telefono

# definizione per trovare il numero di telefono
def trova_numero(dizionario, chiave):
    return dizionario[chiave]

def main():
    dict_numeri = dict()

    # aggiunta/ aggiunzione di elementi al dizionario
    crea_dizionario(dict_numeri)

    print()
    # richiesta del nome della persona
    nome = input('Nome della persona di cui si vuole conoscere il numero di telefono: ')

    if nome in dict_numeri:
        # reperimento del numero di telefono
        n_telefono = trova_numero(dict_numeri, nome)

        # visualizzazione del numero
        print('Il numero di telefono di ', nome.capitalize(),' è ', n_telefono)
    
    else:
        print('Questo nome non si trova nella rubrica')

main()


