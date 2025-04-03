import time, os, random
os.system("cls")

pedidos_sandwiches = ["de pastrón", "de pollo", "de pastrón", "de pastrón", "de huevo duro"]
pedidos_terminados = []

print("La sandwicheria se quedo sin de pastron!")

for "de pastron" in pedidos_sandwiches:
    pedidos_sandwiches.remove("de pastron")

for pedido in pedidos_sandwiches:
    print(pedido)
    pedidos_terminados.append(pedido)

print("\nPedidos terminados:")
print(pedidos_terminados)
