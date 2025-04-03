import os, time, random
os.system("cls")

lenguajes_favoritos = {"Juan": "python", "Sara": "c", "Eduardo": "rust", "Agustina": "c#"}
personas_nuevas = {"Juan", "Marta", "Eduardo", "Lucia", "Agustina", "Carlos"}

for persona in personas_nuevas:
    if persona in lenguajes_favoritos:
        print("Gracias por responder la encuesta: ", persona)
    else:
        print(persona, "te invitamos a que respondas nuestro cuestionario!")
