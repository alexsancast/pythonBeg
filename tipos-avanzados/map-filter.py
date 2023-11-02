usuarios = [[4, "Chanchito"], [3, "Felipe"], [5, "Alex"]]

# Map
# nombres = list(map(lambda usuario: usuario[0], usuarios))

# Filter
menosUsuarios = list(filter(lambda usuario: usuario[0] > 2, usuarios))
print(menosUsuarios)
