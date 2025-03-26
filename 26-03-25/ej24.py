import os, time, random

usuarios_actuales = ["Messi", "Newton", "Einstein", "Leo", "Ronaldo"]
usuarios_nuevos = ["Alvarez", "Leo", "MacAllister", "Dibu", "Enzo Fernandez"]

for usuarioA in usuarios_actuales:
    for usuarioB in usuarios_nuevos:
        if usuarioA == usuarioB:
            print("Ese nombre esta en uso, debe de elegir otro.")
        else:
            print("Ese nombre esta disponible.")