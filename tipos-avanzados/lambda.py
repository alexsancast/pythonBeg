numeros = [3, 345, 5554, 654, 654]
# numeros.sort()  # ordenar listas
numeros.sort(reverse=True)  # Ordernar al reves

# devuelve una nueva lista con los elementos ordenados
numeros2 = sorted(numeros)


usuarios = [[4, "Chanchito"], [3, "Felipe"], [5, "Alex"]]
usuarios.sort(key=lambda el: el[0])

print(usuarios)
