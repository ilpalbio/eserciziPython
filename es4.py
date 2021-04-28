# es 4 scheda
pGreco = 3.14159265358
print('Che area vuoi calcolare')
print('1. Quadrato')
print('2. Rettangolo')
print('3. Trianglo')
print('4. Cerchio')
scelta = input('Risposta: ').lower()
# calcolo area quadrato
if scelta == '1' or scelta == 'quadrato':
    lato = float(input('Lato del quadrato: '))
    area = lato * lato
    print("L'area del quadrato è ", area)
# calcolo area rettangolo
elif scelta == '2' or scelta == 'rettangolo':
    lato = float(input('Lato del rettangolo: '))
    h = float(input('Altezza del rettangolo: '))
    area = lato * h
    print("L'area del rettangolo è", area)
# calcolo area triangolo
elif scelta == '3' or scelta == 'triangolo':
    cateto = float(input('Cateto: '))
    h = float(input('Altezza relativa al cateto: '))
    area = (cateto * h) / 2
    print("L'area del triangolo è ",area)
# calcolo area cerchio
else:
    raggio = float(input('Raggio della circonferenza: '))
    area = pGreco * raggio ** 2
    print("L'area del cerchio è {:.2f}".format(area))