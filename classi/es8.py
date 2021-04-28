'''
esercizio 8 pagina 292

Crea una classe 'Quadrato' con l'attributo 'lato' e i metodi per il calcolo del perimetro e dell'area
'''
# classe quadrato
class Quadrato:
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self): # metodo per calcolare il perimetro
        self.perimeter = self.side * 4

        return self.perimeter

    def calculate_area(self): # metodo per il calcolo dell'area
        self.area = self.side ** 2

        return self.area

def main(): # funzione main
    side = float(input('Lunghezza lato del quadrato: '))

    square = Quadrato(side)

    # calcolo del perimetro e dell'area
    perimeter = square.calculate_perimeter()

    area = square.calculate_area()

    print()
    print('PERIMETRO QUADRATO: {:.1f}'.format(perimeter))
    print('AREA QUADRATO: {:.1f}'.format(area))

main()