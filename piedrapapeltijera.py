import random

def jugadores():
    jugador=input('escoge (piedra-papel-tijera): ')
    return jugador.lower()   

def pc():
    lista=['piedra','papel','tijera']
    return random.choice(lista)

def main():
    jugador=jugadores()
    computadora=pc()
    print(f'{jugador= }')
    print(f'{computadora= }')
    if jugador == 'piedra' and computadora == 'tijera':
        print('jugador gana')    
    elif jugador == 'piedra' and computadora =='papel':
        print('computadora gana')
    elif jugador == 'piedra' and computadora =='piedra':
        print('empate')     
    elif jugador == 'papel' and computadora =='piedra':
        print('jugador gana')  
    elif jugador == 'papel' and computadora =='tijera':
        print('computadora gana')     
    elif jugador == 'papel' and computadora =='papel':
        print('empate') 
    elif jugador == 'tijera' and computadora =='papel':
        print('jugador gana')    
    elif jugador == 'tijera' and computadora =='piedra':
        print('computadora gana')   
    elif jugador == 'tijera' and computadora =='tijera':
        print('empate')            

if __name__ == '__main__':
    main() 