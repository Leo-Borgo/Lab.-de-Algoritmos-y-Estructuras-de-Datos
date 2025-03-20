import time

lugares = ["Dubai", "Brasil", "Grecia", "Noruega", "Australia"]

print("Lista original: ", lugares, "\n")
time.sleep(1)
print("Lista ordenada: ", sorted(lugares), "\n")
time.sleep(1)
print("Lista original: ", lugares, "\n")
time.sleep(1)
lugares.reverse()
print("Lista invertida: ", lugares, "\n")
time.sleep(1)
print("Lista actual: ", lugares, "\n")
time.sleep(1)
lugares.reverse() 
print("Lista original (restaurada): ", lugares, "\n")
time.sleep(1)
lugares.sort()
print("Lista ordenada: ", lugares, "\n")
time.sleep(1)
lugares.sort(reverse=True)
print("Lista inversa: ", lugares, "\n")