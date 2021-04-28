'''
esercizio 25

I voti assegnati a 30 studenti di una classe in una prova di italiano sono memorizzati in un dizionario che ha per chiave la matricola,
mentre il valore associato al voto. Elenca i risulatati in ordine crescente di voto e successivamente visualizza quali voti diversi 
tra loro sono associati, riducendo a uno i voti uguali
'''
# funzione per la richiesta delle informazione e per la creazione di un dizionario ed una lista
def riempi_dizionario_e_lista(dizionario, lista):
    for i in range(30):
        matricola = input('Matricola studente: ')
        voto = float(input('Voto studente: '))

        # aggiunta di nuove chiavi e valori nel dizionario
        dizionario[matricola] = voto

        # aggiunta dei voti nella lista
        lista.append(voto)

# funzione per visualizzare i risulatati
def visualizza_risultati(lista_voti ,lista_voti_finale):
    # ordinazione dei voti in oridine crescente
    lista_voti.sort()

    # visulaizzazione dei voti con voti uguali
    print('-' * 10)
    for voti in lista_voti:
        print(voti)
    
    print('-' * 10)

    # eliminazione dei voti uguali
    elimina_voti_uguali(lista_voti, lista_voti_finale)

    print()
    # visualizzazione dei voti senza ripetizioni di voti
    print('Elenco voti senza ripetizioni')
    
    print('-' * 10)
    for voti in lista_voti_finale:
        print(voti)
    
    print('-' * 10)

# funzione per eliminare i voti uguali
def elimina_voti_uguali(lista_voti,lista_voti_finale):
    for voti in lista_voti:
        if voti not in lista_voti_finale:
            lista_voti_finale.append(voti)

# funzione principale
def main():
    dict_voti = dict()
    lista_voti = []
    lista_voti_finale = []

    # riempimento del dizionario e della lista
    riempi_dizionario_e_lista(dict_voti, lista_voti)

    # visualizzazione dei voti
    visualizza_risultati(lista_voti, lista_voti_finale)

main()



