class Quadrato:
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self): # metodo per calcolare il perimetro
        return self.side * 4

    def calculate_area(self): # metodo per il calcolo dell'area

        return self.side ** 2
