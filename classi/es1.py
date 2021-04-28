''' 
esercizio 1 pagina 292

Crea una classe Atleta per rappresentare le informazioni su un giocatore. La classe deve contenere un attributo booleano chamato 
visitaMedica
'''
class Atleta:

    # costruttore
    def __init__(self, name, surname, age , height, weight, sport):
        self.name = name
        self.surname = surname
        self.age = age
        self.height = height
        self.weight = weight
        self.sport = sport
        self.team = ''
        self.visitaMedica = False

    '''
    esercizio 2 pagina 292

    Aggiungi alla classe Atleta un metodo per assegnare all'atleta il nome della squadra dove gioca
    '''
    def assign_team(self, team):
        self.team = team

    '''
    esercizio 3 pagina 292

    Aggiungi alla classe Atleta unmetodo chiamato 'effettua_visita' che ponga l'attributo viitaMedica uguale a True
    '''

    def effettua_visita(self):
        self.visitaMedica = True

    '''
    esercizio 4 pagina 292

    Aggiungi alla classe Atleta un metodo per visualizzare i dati del giocatore
    '''

    def show_info(self):
        # visualizzazione delle informazioni
        print('Nome: ', self.name.capitalize())
        print('Cognome: ', self.surname.capitalize())
        print('Età: ', self.age, ' anni')
        print('Altezza: ', self.height, ' cm')
        print('Peso: ', self.weight, ' kg')
        print('Sport: ', self.sport.capitalize())
        print('Squadra: ', self.team.capitalize())


def main():

    # richiesta delle informazioni
    name = input('Nome giocatore: ')
    surname = input('Cognome giocatore: ')
    age = int(input('Età giocatore: '))
    height = float(input('Altezza giocatore (cm): '))
    weight = float(input('Peso giocatore (kg): '))
    sport = input('Sport praticato: ')


    # istanza 
    atleta = Atleta(name, surname, age, height, weight, sport)

    # richiesta della squadra
    team = input('Squadra in cui gioca: ')
    atleta.assign_team(team)

    # cambio del valore booleano di visitaMedica
    atleta.effettua_visita()

    # visuallizazione delle informzioni del giocatore
    print()
    print('INFO')
    print('-' * 30)

    atleta.show_info()

    print('-' * 30)



main()