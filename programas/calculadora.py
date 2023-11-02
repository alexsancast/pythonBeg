print("Bienvenidos a la calculadora \nPara salir escribe Salir \nLas Operaciones son suma, multi , div y resta")

resultado =""

while True :
    if not resultado:
        resultado = input("Ingrese el primer numero: ")
        if resultado.lower() == "salir":
            break 
        resultado = int(resultado)
    op = input("Ingresa operacion")
    if op.lower() == "salir":
        break
    n2 = input ("Ingresa el segundo numero:")
    if n2.lower() == "salir":
        break
    n2 = input(n2)

    if op.lower() == "suma":
        resultado += n2
    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "div":
        resultado /= n2    
    elif op.lower() == "multi":
        resultado *= n2
    else:
        print("Operacion incorreta")

print(f"El resultado es{resultado}")           




    
    
       