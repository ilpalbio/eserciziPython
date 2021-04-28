'''
esercizio 25 pagina 293

Crea la classe 'Triangolo', la classederivata 'Triangoloisoscele' e, da quest'ultima, la classe derivata 'TriangoloEquilatero'
'''
# classe Triangolo
class Triangolo:
    def __init__(self, hight, base, side_1, side_2):

        self.hight = hight
        self.base = base
        self.side_1 = side_1
        self.side_2 = side_2

    def show_info(self):
        print('Altezza: ', self.hight)
        print('Base: ', self.base)
        print('Lato 1: ', self.side_1)
        print('Lato 2: ', self.side_2)

# classe Triangolo isoscele
class Triangoloisoscele(Triangolo):
    def __init__(self, hight, base, side_oblique):
        super().__init__(hight, base)

        self.side_oblique = side_oblique

    def show_info(self):
        print('Altezza: ', self.hight)
        print('Base: ', self.base)
        print('Lato obliquo: ', self.side_oblique)

# classe Triangolo equilatero
class Triangoloequilatero(Triangoloisoscele):
    def __init__(self, hight, base, side):
        super().__init__(hight, base)

        self.side = side

    def show_info(self):
        print('Altezza: ', self.hight)
        print('Base: ', self.base)
        print('Lato: ', self.side)

