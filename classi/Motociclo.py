# classe motociclo
class Motociclo:
    def __init__(self, brand, license_plate, displacement, power, speed): # costruttore
        self.brand = brand
        self.license_plate = license_plate
        self.displacement = displacement
        self.power = power
        self.speed = speed

    def show_info(self):
        print('Marca: ', self.brand.capitalize())
        print('Targa: ', self.license_plate)
        print('Cilindrata: ', self.displacement, 'cc')
        print('Potenza: ', self.power, 'CV')
        print('Velocità: ', self.speed, 'km/h')


