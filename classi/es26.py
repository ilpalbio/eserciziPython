'''
esercizio 26 pagina 293

Deriva dalla classe Quadrato del Problema 8 una nuova classe Rettangolo aggiungendo un secondo lato per l'altezzae riscrivendo
i metodi per il calcolo del perimetro dell'area
'''
from Quadrato import *


class Rettangolo(Quadrato):
    def __init__(self, side, hight):
        super().__init__(side)
        self.base = side
        self.hight = hight

    def calculate_perimeter(self):
        return self.base * 2 + self.hight * 2

    def calculate_area(self):
        return self.base * self.hight
