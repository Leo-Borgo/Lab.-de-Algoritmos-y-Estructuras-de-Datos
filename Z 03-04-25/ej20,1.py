import os, time, random
os.system("cls")

pedidos_sandwiches = ["de jamon y queso", "de pollo", "de vegetales asados", "de atun", "de huevo duro"]
sandwiches_terminados = []

for pedido in pedidos_sandwiches:
    print("Se está preparando el sandwich:", pedido)
    time.sleep(3)
    print("Sandwich", pedido, "terminado")
    time.sleep(1)
    os.system("cls")
for i in range(5):
    sandwich_actual = pedidos_sandwiches.pop()
    sandwiches_terminados.append(sandwich_actual)
os.system("cls")
print("Sandwiches preparados: ", sandwiches_terminados)
