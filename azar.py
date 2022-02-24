import random

def inicio():
    inicio = input('Comenzar el juego s/n: ')
    turnos = 5
    if inicio == "s":
        azar = random.randrange(0,11)
        return azar, turnos 
    else:
        print('termino el juego')      
    
def adivina():
    jugador=int(input("adivina el numero: "))
    return jugador    

def main():
    azar, numero_turno = inicio()
    while numero_turno != 0:
        print(f"te quedan {numero_turno} turnos")
        jugador = adivina()
        numero_turno -= 1
        if jugador == azar:
            print("ganaste")
            break
    if numero_turno == 0 and jugador != azar:
        print("perdiste pe gil")
    if input('quieres jugar otra vez s/n:') == "s":
        main()
    else:
        print("termino el juego")       

if __name__ == "__main__":
    main()