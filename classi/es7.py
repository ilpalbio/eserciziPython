'''
esercizio 7 pagina 292

Elenca proprietà e metodi della classe Motociclo
'''
# classe motociclo
class Motociclo:
    def __init__(self, brand, cooling, displacement, power, speed): # costruttore
        self.brand = brand
        self.displacement = displacement
        self.power = power
        self.speed = speed
        self.cooling = cooling

    def assign_license_plate(self, license_plate): #metodo per assegnare la targa
        self.license_plate = license_plate

    def show_info(self): # metodo per scrivere tutte le informazioni del veicolo
        print('Targa: ', self.license_plate)
        print('Marca: ', self.brand.capitalize())
        print('Cilindrata: ', self.displacement,' cc')
        print('Potenza: ', self.power, ' kW')
        print('Velocità: ', self.speed, ' km/h')
        print('Sistema di raffreddamento: ', self.cooling.capitalize())

def main(): # funzione main
    # richiesta delle informazioni
    brand = input('Marca del motociclo: ')
    license_plate = input('Targa: ')
    displacement = int(input('Cilindrata (cc): '))
    power = int(input('Potenza (kW): '))
    speed = int(input('Velocità (km/h): '))
    cooling = input('Sistema di raffreddamento: ')

    motorcycle = Motociclo(brand, cooling, displacement, power, speed)

    # assegnazione della targa
    motorcycle.assign_license_plate(license_plate)

    # visualizzazione delle informazioni
    print()
    print('INFO')
    print('-' * 30)
    motorcycle.show_info()
    print('-' * 30)

main()