import random

def generar_nombre(Nombres =None,  apellidos =None ):
    nombresPredeterminados = ["Sofia", "Flor", "Rebeca", "Dinora", "Diana", "Natalia", "Marisol"] 
    apellidosPredeterminados = ["Martinez", "Miranda", "Moran", "Hernandez", "Gonzales", "Santos","Mejia"]

    if nombres is None:
        nombres = nombresPredeterminados
    if apellidos is None:
        apellidos = apellidosPredeterminados
    nombre = random.choice(Nombres)
    apellido = random.choice(apellidos)
    return f"{nombre} {apellido}"
 
def agregar_nombres_personalizados():
    nombres_personalizados= input("Ingresa nombres personalizados  separandolos por una coma").split(",")
    apellidos_personalizados= input(" Ingresa apellidos personalizados separandolos por una coma").split(",")
    return[nombre.strip() for nombre in nombres_personalizados], [apellidos.strip() for apellidos in apellidos_personalizados]
if __name__ == "__main__":
    option = input("¿Quisieras usar nombres personalizados? (s/n): ").strip().lower()
    if option == "s":
       nombres, apellidos = agregar_nombres_personalizados() 
    else:
        nombres, apellidos = None, None

        print("Nonmbre creado:", generar_nombre(nombres, apellidos))