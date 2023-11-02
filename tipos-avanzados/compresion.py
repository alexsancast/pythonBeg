usuarios = [[4, "Chanchito"], [3, "Felipe"], [5, "Alex"]]

# nombres = []

# for usuario in usuarios:
#     nombres.append(usuario[1])
# print(nombres)

# Transformar listas
# nombres = [usuario[1] for usuario in usuarios]
# Buscar listas
nombres = [usuario for usuario in usuarios if usuario[0] > 2]

print(nombres)
