import time, os

os.system("cls")

pizzas = ["Muzzarella", "Napolitana", "Con champiñones", "Margarita"]

pizzas_amigo = pizzas[:]
pizzas_amigo.append("De huevo")

for pizza in pizzas:
    print("Mis pizzas favoritas son: ", pizza), time.sleep(1)
    
print("\n")
print("----------------------------------------------------------------------")
print("\n")

for pizza_amigo in pizzas_amigo:
    print("Las pizzas favoritas de mi amigo son: ", pizza_amigo), time.sleep(1)
