'''
esercizio 5 pagina 292

Elenca proprietà e metodi della classe Prodotto
'''
# calsee prodotto
class Prodotto:
    __purchase = False
    def __init__(self, name, brand, calories): # costruttore
        self.name = name
        self.brand = brand
        self.calories = calories

    # funzione per comprare il prodotto
    def buy_prodoct(self):
        self.__purchase = True

    '''
    esercizio 6 pagina 22

    Definisci il metodo 'assegna_prezzo' della classe Prodotto
    '''

    # funzione per assegnare 
    def assegna_prezzo(self, price):
        self.price = price


def main():
    # richiesta informazioni
    name = input('Nome prodotto: ')
    brand = input('Marca prodotto: ')
    calories = float(input('Calorie prodotto: '))
    price = float(input('Prezzo prodotto: '))

    prodoct = Prodotto(name, brand, calories)

    # acquisto del prodotto
    prodoct.buy_prodoct()

    # assgnazione del prezzo
    prodoct.assegna_prezzo(price)

main()

