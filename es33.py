# es 33
def estrai_pazienti(lista):
    return lista.pop(0)

def main():
    lista_pazienti = []
    while True:
        nome = input('Nome paziente (* = fine): ')

        if nome == '*':
            break

        else:
            lista_pazienti.append(nome)

    print('Pazienti')
    print('-'*20)

    for n in range(len(lista_pazienti)):
        paziente = estrai_pazienti(lista_pazienti)

        print()
        print(paziente)

main()
        
    

