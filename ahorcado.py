def jugar():
    print ("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
    print ("Bienvenido al juego del ahorcado")
    print ("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
    
    palabra_secreta = "mandarina"
    
    ahorcado = False
    acerto = False
    
    while(not ahorcado and not acerto):
        entrada=input("ingrese una letra ...")
        indice = 0
        for letra in palabra_secreta:
            if(entrada==letra):
                print("se encontro la letra {} en la posicion {}".format(letra,indice))
                 
            indice = indice+1        
        print("Jugando...")
        
        
    print("Fin del juego")
    
if(__name__ == "__main__"):
    jugar()