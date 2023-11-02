"""Metodo Upper  transformar letra a mayus"""
animal = "  chanChito feliz"
print(animal.upper())
print(animal.lower())
print(animal.capitalize()) #Primera letra en mayuscula
print(animal.strip().capitalize())
print(animal.title()) #Primera letra de cada palabra en mayus
print(animal.strip()) #Elmina espacios de izquierda a derecha
print(animal.lstrip()) #Elimina los espacio de la izquierda
print(animal.rstrip()) #Elimina los espacio de la derecha
print(animal.find("Ch")) #Busca el indice de la cadena
print(animal.replace("Ch" , "j")) #Remplazar cadenas de caracteres
print("Ch" in animal) #Devuelve un boolean si se encuentra o no 
print("Ch" not in animal) # Negacion