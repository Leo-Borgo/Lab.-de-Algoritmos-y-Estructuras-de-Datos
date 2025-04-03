import os
import time

os.system("cls")

ingredientes = []

print("Prepararemos una pizza.\n"
      "Constantemente le pediré ingredientes.\n"
      "Si quiere ver los ingredientes actuales escriba 'receta'.\n"
      "Si quiere salir del programa escriba 'salir'.")

time.sleep(1)

while True:
    ingrediente = input("\nIngrese un ingrediente para su pizza: ").strip().lower()

    if ingrediente == "salir":
        print("Gracias por usar el programa. ¡Disfruta tu pizza!")
        break
    elif ingrediente == "receta":
        print(f"Los ingredientes actuales son: {', '.join(ingredientes) if ingredientes else 'ninguno'}.")
    else:
        ingredientes.append(ingrediente)
        print(f"{ingrediente.capitalize()} agregado a la receta.")

    time.sleep(0.75)
    os.system("cls")
