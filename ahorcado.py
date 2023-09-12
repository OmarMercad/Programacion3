def jugar():
    print ("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
    print ("Bienvenido al juego del ahorcado")
    print ("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
    
    palabra_secreta = "mandarina"
    letras_acertadas=["-","_","_","_","_","_","_","_","_"]
    ahorcado = False
    acerto = False
    errores = 0
    print(letras_acertadas)
    while(not ahorcado and not acerto):
        entrada = input("ingrese una letra ...")
        entrada = entrada.strip()
        entrada = entrada.lower()
        
        if entrada in palabra_secreta:
            indice = 0
            for letra in palabra_secreta:
                if(entrada==letra):
                    letras_acertadas[indice] = letra

                indice = indice+1  
        else: 
            errores += 1 
            
        ahorcado = errores == 9 
        acerto = "-" not in letras_acertadas
        print(letras_acertadas)
    if(acerto):
        print ("felicidades, ganaste")
    else:
        print("lo siento, perdiste")
        
        
        
        
    print("Fin del juego")
    
if(__name__ == "__main__"):
    jugar()