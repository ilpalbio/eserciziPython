# es 25 pag 73
# richiesta dei nomi e dei punteggi
nome1 = input('Nome primo cadìndidato: ').lower()
voti1 = int(input('Numero voti: '))
nome2 = input('Nome secondo candidato: ').lower()
voti2 = int(input('Numero voti: '))
# visualizzare i candidati in ordine alfabetico
print()
print('Ordine alfabetico dei candidati')
if nome1 < nome2:
    print(nome1)
    print(nome2)
else:
    print(nome2)
    print(nome1)

print()
# ordine decrescente di punteggio
print('Ordine decrescente di punteggio dei candidati')
if voti1 > voti2:
    print(nome2)
    print(nome1)
elif voti1 < voti2:
    print(nome1)
    print(nome2)
else:
    print('I voti sono pari')