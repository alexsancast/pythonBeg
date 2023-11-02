punto = {"x": 25, "y": 50}
print(punto["y"])
# asignar llave
# punto["z"] = 45

if "lala" in punto:
    print("Se encuentra")

usuarios = [
    {"id", 1, "nombre", "Alexander", "edad", 29},
    {"id", 2, "nombre", "Pedro", "edad", 30}

]

for valor in punto:
    print(valor, punto[valor])


for valor in punto.items():
    print(valor)


for llave, valor in punto.items():
    print(llave, valor)


# print(punto.get("ala", 97))
