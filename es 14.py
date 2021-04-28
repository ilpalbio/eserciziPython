'''
es 14 pag 72
crea un programma ch scriva la differenza di due numeri a e b se il loro prodotto è maggiore di 10,
oppure la loro somma se il prodotto è minore o uguale a 10
'''

a = float(input('Numero a: '))
b = float(input('Numero b: '))

if a * b > 10:
    print('La differenza di ',a,' e ',b,' è ', a - b )
else:
    print('La somma di ',a,' e ',b,' è ', a + b )
