import random
import re

# Lista de palabras para elegir al azar
palabras = ["lunes", "perro", "manta", "carta", "raton", "rueda", "orden", "yanyo"]

# Seleccionar una palabra al azar
palabra_secreta = random.choice(palabras)

intentos_restantes = 5

print("Bienvenido a Wordle!")

while intentos_restantes > 0:
    intento = input("Ingresa tu intento de 5 letras: ").lower()
    
    # Validar la longitud de la entrada del jugador
    if len(intento) != 5:
        print("Por favor ingresa una palabra de 5 letras.")
        continue
    
    feedback = ""
    
    # Comparar cada letra del intento con la palabra secreta
    for i in range(5):
        if intento[i] == palabra_secreta[i]:
            feedback += "[" + intento[i] + "]"
        elif intento[i] in palabra_secreta:
            feedback += "(" + intento[i] + ")"
        else:
            feedback += intento[i]
    
    print("Intento:", feedback)
    
    # Actualizar el contador de intentos restantes
    intentos_restantes -= 1
    print("Intentos restantes:", intentos_restantes)
    
    # Verificar si el jugador ha adivinado la palabra
    resultado_final = re.sub("[\[\]]", "", feedback) # quitarle los corchetes a feedback para poder comparar los caracteres ingresados con mejor precision
    print(resultado_final)
    if resultado_final == palabra_secreta:
        print("¡Felicidades! ¡Has adivinado la palabra secreta!")
        break

if intentos_restantes == 0:
    print("¡Lo siento! Has agotado tus intentos. La palabra secreta era:", palabra_secreta)
