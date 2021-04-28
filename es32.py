'''
es 32 pag 73
Implementa l'algoritmo per il calcolo della soluzione di un'equazione di primo  grado ax + b = 0. Il proceso risolutivo dipende
dai valori assunti dai coefficenti a e b secondo la tabella che segue.
'''
print('Equazione: ax + b = 0')
a = float(input('a: '))
b = float(input('b: '))
print('Equazione: ',a,'x',' + ',b,' = 0')
print()
if a == 0 and b == 0:
    print('Equazione indeterminata')
elif a == 0 and b != 0:
    print('Equazione impossibile')
elif a != 0 and b == 0:
    print("La soluzione dell'equazione è: x = 0")
else:
    print("La soluzione dell'equazione è: x = -b / a")
    print(-b / a)