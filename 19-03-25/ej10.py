personas = ["Albert Einstein", "Mahatma Gandhi", "Steve Jobs"]

for persona in personas:
    mensaje = f"Hola {persona}! Me gustaria invitarte a cenar a mi departamento, podemos charlar un rato"
    print(mensaje)

print("\nLionel Messi no podrá asistir a la cena.")

print("\nTengo una mesa mas grande, voy a invitar a mas personas.")

personas.insert(0, "Diego Maradona")

personas.insert(2, "Elon Musk")

personas.append("Leonardo da Vinci")

print("\nEnviando una nueva serie de invitaciones:\n")
for persona in personas:
    mensaje = f"Hola {persona}! Me gustaria invitarte a cenar a mi departamento, podemos charlar un rato"
    print(mensaje)
