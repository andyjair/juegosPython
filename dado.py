import random
    
def jugador1():
    jugador1 = input('jugador 1 tira el dado (y/n): ')
    if jugador1 == 'y':
            dados = random.sample(range(1,7),2)
            suma= sum(dados)
            print(f'Los dados son: {dados}')
            print(f'La suma es:{suma}')      
            return suma
    else:
        jugador1 = input('perdiste!! ') 

def jugador2():
    jugador2 = input('jugador 2 tira el dado (y/n): ')
    if jugador2 == 'y':
            dados = random.sample(range(1,7),2)
            suma= sum(dados)
            print(f'Los dados son: {dados}')
            print(f'La suma es: {suma}')
            return suma   
    else:
        jugador2 = print('Perdiste!! ')           

def inicio():
    inicio = input('comenzar juego (y/n): ')
    if inicio == 'y':
        meta = random.sample(range(1,7),2)
        meta=sum(meta)
        print(meta)
        return meta
    else:
        print('Juego finalizado')

def main():
    meta = inicio()
    jugador1sum = []
    jugador2sum = []
    while meta != jugador1sum and meta != jugador2sum:
        jugador1sum =jugador1()
        jugador2sum = jugador2()
    if jugador1 == meta:
        print("jugador 1 gano")
    else: 
        print("jugador 2 gano")
    if input('quieres jugar otra vez[s/n]')== "s":
        main()
if __name__ == '__main__':
    main()