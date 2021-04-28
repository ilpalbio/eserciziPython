'''
esercizio 21 

Data la classe Motociclo nel problema 7, deriva la classe Ciclomotore. Aggiungi le proprietà opportune
e modifica il metodo che consente di visualizzare i valori delle proprietà
'''
from Motociclo import *


class Ciclomotore(Motociclo):
    def __init__(self, brand, license_plate, displacement, power, speed):
        super().__init__(brand, license_plate, displacement, power, speed)


def main():
    # richiesta delle info
    brand = input('Marca: ')
    license_plate = input('Targa: ')
    while True:
        displacement = int(input('Cilidrata (cc): '))
        if displacement > 50:
            print('La cilindrata di un ciclomotore non deve essere maggiore di 50 cc')
            print()

        else:
            break

    while True:
        power = float(input('Potenza (CV): '))
        if power > 1.5:
            print('La potenza di un ciclomotore non deve essere maggiore di 1.5 CV')
            print()

        else:
            break

    while True:
        speed = int(input('Velocità (km/h): '))
        if speed > 40:
            print('La velocità di un ciclomotore non deve essere maggiore di 40 km/h')
            print()
        else:
            break

    motorcycle = Motociclo(brand, license_plate, displacement, power, speed)

    moped = Ciclomotore(brand, license_plate, displacement, power, speed)

    # visualizzazione delle nformazioni
    print()
    print('INFO')
    print('-' * 30)
    moped.show_info()
    print('-' * 30)


main()


