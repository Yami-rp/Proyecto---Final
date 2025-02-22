import random
# lista predefinida de nombres y apellidos
nombres = ["Marcos", "Liliana", "Pedro", "Daniela", "Javier", "Carmen"]

apellidos =["Toledo", "Gonzales", "Rodríguez", "Mejía", "Linares", "Pineda"]

def agregar_nombre():
    nuevo_nombre= input("Ingrese un nombre nuevo (o presione Enter para omitir):").strip()
    if nuevo_nombre:
        nombres.append(nuevo_nombre)
        print(f"Nombre '{nuevo_nombre}' agregado correctamente")

def agregar_apellido():
    nuevo_apellido = input( "Ingrese un nuevo apellido(o presione Enter para omitir):").strip()
    if nuevo_apellido:
        apellidos.append(nuevo_apellido)
        print(f"Apellido '{nuevo_apellido}' agregado correctamente")

def generar_nombre():
    return f"{random.choice(nombres)}{random.choice(apellidos)}"

def generar_multiples_nombres(cantidad):
    return [generar_nombre()for _ in range(cantidad)]

# menú 
while True:
    print("\n--- Generador de nombres aleatorios---")
    print("1. Agregar un nombre personalizado")
    print("2. Agregar un apellido personalizado")
    print("3. Generar un nombre aleatorio")
    print("4. Generar multiples nombres aleatorios")
    print("5. Salir")
    opcion = input("Seleccione una opcion: ").strip()
    if opcion == "1":
        agregar_nombre()
    elif opcion =="2":
        agregar_apellido()
    elif opcion == "3":
        print("\nNombre generado:", generar_nombre())
    elif opcion == "4":
        cantidad = int(input("¿Cuántos nombres quieres generar?"))
        print("\nNombres generados:")
        for nombre in generar_multiples_nombres(cantidad):
         print ("-", nombre)
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    else:
        print("Opcion no valida. Favor intentarlo de nuevo.")


    