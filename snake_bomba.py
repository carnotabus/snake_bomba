import readchar
import os
import random
import time
#hacer niveles normales y dificiles
#primero el alto y luego el ancho x

y_es = 0
x_es = 1

ancho = 20
alto = 10
x = ancho
y = alto
posicion = [4,9]
y_pos = posicion[0]
x_pos = posicion[1]

#bombas
bomba1 = [random.randint(0,9),random.randint(0,19)]
bomba2 = [random.randint(0,9),random.randint(0,19)]
bomba3 = [random.randint(0,9),random.randint(0,19)]
bomba4 = [random.randint(0,9),random.randint(0,19)]
bomba5 = [random.randint(0,9),random.randint(0,19)]
bomba6 = [random.randint(0,9),random.randint(0,19)]

#premios
premio1 = [random.randint(0,9),random.randint(0,19)]
premio2 = [random.randint(0,9),random.randint(0,19)]
premio3 = [random.randint(0,9),random.randint(0,19)]
cantidad_premios = 0
premios_totales = 3

def menu():
#aca sugerir si instalaran figlet
    os.system("figlet bienvenido/a")
    print(" Este es mi juego!!!\n este juego consiste en un mapa ciego\n donde no veras si hay bombas o premios.")
    print(" Tu suerte te llevara a ganar o no!!!")
    print("\n [MENU]\n [1]Jugar\n [2]Registro de partidas\n [3]Como se juega")
    repp = int(input(" Respuesta: "))

    if repp == 1:
        print("") #aca nos invitarioa al menu a elgir la dificultad
    elif repp == 2:
        if  os.path.isfile(".partidas.txt") == False:
            print("\n -Usted no tiene partidas jugadas.")
            input("\n -Presione enter para volver al menu: ")
            os.system("python3 snake_bomba.py")
        else:
            os.system("clear")
            print(" ")
            os.system("cat .partidas.txt")
            input("\n -Presione enter para volver al menu: ")
            os.system("python3 snake_bomba.py")
    elif repp == 3:
        os.system("clear")
        print("\n Podras moverte en el mapa virtual con las teclas\n A(izquierda),S(abajo),D(derecha),W(arriba)\n La idea es conseguir los 3 premios sin morir!  ") #aca iria la explicacion del juego
        input("\n -Presione enter para volver al menu: ")
        os.system("python3 snake_bomba.py")

    else:
        print("\n Usted ha seleccionado una opcion que no existe")
        input("\n -Presione enter para volver al menu: ")
        os.system("python3 snake_bomba.py")

os.system("clear")
menu()

while True:
    os.system("clear")
    print(" +"+"-"*x+"+")
    for cory in range(y):
        print(" |", end="")
        for corx in range(x):
            if posicion[y_es] == cory and posicion[x_es] == corx:
                print("@",end="")
            else:
                print("*", end="")
        print("|")
    print(" +"+"-"*x+"+")
    print("")
    print(" Apreta q para salir")
    print(f" Has conseguido {cantidad_premios} premios!!!, te faltan {premios_totales} para ganar")
    
    direc = readchar.readchar()
    if direc == "w":
        posicion[0] -= 1
        y_pos + 1

    elif direc == "s":
        posicion[0] += 1
    elif direc == "a":
        posicion[1] -= 1
    elif direc == "d":
        posicion[1] += 1
    elif direc == "q":
        break

    
    if posicion[0] >= 10:
        posicion[0] = 0
    elif posicion[0] <= -1:
        posicion[0] = 9
    
    if posicion[1] >= 20:
        posicion[1] = 0
    elif posicion[1] <= -1:
        posicion[1] = 19
    else:
        print("", end="") 
#bombas _--------------------------------------------------------------------------   
    if posicion[y_es] == bomba1[0] and posicion[x_es] == bomba1[1]:
        os.system("clear")
        print("\n Has muerto por una explosion!!!")
        os.system("echo ' [partida jugada el dia' >> .partidas.txt")
        os.system("date >> .partidas.txt")
        os.system("echo ' Has perdido]\n' >> .partidas.txt")
        break
    elif posicion[y_es] == bomba2[0] and posicion[x_es] == bomba2[1]:
        os.system("clear")
        print("\n Has muerto por una explosion!!!")
        os.system("echo ' [partida jugada el dia' >> .partidas.txt")
        os.system("date >> .partidas.txt")
        os.system("echo ' Has perdido]\n' >> .partidas.txt")
        break
    elif posicion[y_es] == bomba3[0] and posicion[x_es] == bomba3[1]:
        os.system("clear")
        print("\n Has muerto por una explosion!!!")
        os.system("echo ' [partida jugada el dia' >>.partidas.txt")
        os.system("date >> .partidas.txt")
        os.system("echo ' Has perdido]\n' >> .partidas.txt")
        break
    elif posicion[y_es] == bomba4[0] and posicion[x_es] == bomba4[1]:
        os.system("clear")
        print("\n Has muerto por una explosion!!!")
        os.system("echo ' [partida jugada el dia' >> .partidas.txt")
        os.system("date >> .partidas.txt")
        os.system("echo ' Has perdido]\n' >> .partidas.txt")
        break
    elif posicion[y_es] == bomba5[0] and posicion[x_es] == bomba5[1]:
        os.system("clear")
        print("\n Has muerto por una explosion!!!")
        os.system("echo ' [partida jugada el dia' >> .partidas.txt")
        os.system("date >> .partidas.txt")
        os.system("echo ' Has perdido]\n' >> .partidas.txt")
        break
#premios -------------------------------------------------------------------
    if posicion[y_es] == premio1[0] and posicion[x_es] == premio1[1]:
        cantidad_premios +=1
        premios_totales -=1

    elif posicion[y_es] == premio2[0] and posicion[x_es] == premio2[1]:
        cantidad_premios +=1
        premios_totales -=1

    elif posicion[y_es] == premio3[0] and posicion[x_es] == premio3[1]:
        cantidad_premios +=1
        premios_totales -=1
    
    if cantidad_premios == 3:
        os.system("echo ' [partida jugada el dia' >> .partidas.txt")
        os.system("date >> .partidas.txt")
        os.system("echo ' Has ganado]\n' >> .partidas.txt")
        os.system("clear")
        print(f"\n Has conseguido {cantidad_premios} premios!!!")
        print(" Felicidades!!! has ganado!!!")
        break

repetir = input("\n Deseas jugar nuevamente? [s/n]\n Respuesta: ")

if repetir == "s":
    os.system("python3 snake_bomba.py")
elif repetir == "n":
    os.system("clear")
    os.system("figlet Gracias por jugar")

else:
    while repetir != "s" and repetir != "n":
        os.system("clear")
        print("\n Has introducido algo incorrecto")
        repetir = input(" Deseas jugar nuevamente? [s/n]\n Respuesta: ")
        if repetir == "s":
            os.system("python3 snake_bomba.py")
        elif repetir == "n":
            os.system("clear")
            os.system("figlet Gracias por jugar")
            break