# es 3 scheda
while True:
    frase = input('Inserire la frase/parola che si vuole tradurre in italiano: ')
    fraseSenzaSpazi = frase.strip()
    listaParole = fraseSenzaSpazi.split(' ')
    tuplaVocali = ('a','e','i','o','u')
    listaLettere = []
    listaParoleFinali = []
    listaFraseFinale = []
    cParole = 0

    for parole in listaParole:
        lettere = list(parole)
        listaLettere.append(lettere)
        cParole += 1

    for elementi in range(cParole):
        for stringhe in listaLettere[0]:
            if stringhe in tuplaVocali:
                listaParoleFinali.append(stringhe)
            else:
                listaParoleFinali.append(stringhe)
                for c in range(0,2):
                    listaLettere[0].remove(stringhe)
                    
        sommaListaLettere = ''.join(map(str, listaParoleFinali))
        listaFraseFinale.append(sommaListaLettere)
        listaLettere.remove(listaLettere[0])
        listaParoleFinali.clear()

    sommaListaParole = ' '.join(map(str, listaFraseFinale))

    print('La traduzione di questa frase è:')
    print(sommaListaParole)

    print()
    risposta = input("Vuoi tradurre un'altra frase/parola: ").lower()
    if risposta == 'si':
        pass
    else:
        print('Ok arrivederci')
        break

