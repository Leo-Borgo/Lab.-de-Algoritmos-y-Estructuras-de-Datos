personas = ["Albert Einstein", "Lionel Messi", "Steve Jobs"]

for persona in personas:
    mensaje = f"Hola {persona}! Me gustaria invitarte a cenar a mi departamento, podemos charlar un rato"
    print(mensaje)

print("\nLionel Messi no podrá asistir a la cena.")
personas[1] = "Galileo Galilei"

print("\nEnviando una nueva serie de invitaciones:\n")
for persona in personas:
    mensaje = f"Hola {persona}! Me gustaria invitarte a cenar a mi despartamento, podemos charlar un rato"
    print(mensaje)
