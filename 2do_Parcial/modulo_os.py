import os 
def mostrar_menu():
    print("\n====HERRAMINETA DE MODULO OS ====")
    print("1. Mostrar directorio actual")
    print("2. Listar archivos y carpetas")
    print("3. Crear una carpeta")
    print("4. Eliminar una carpeta")
    print("5. cambiar de directorio")
    print("x. Salir")

while True:
    mostrar_menu()
    opcion=input("Selecciona una opción: ")

    if opcion=="1":
        print("Directorio actual:", os.getcwd())

    elif opcion=="2":
        archivos=os.listdir()
        print("Contenido del directorio: ")
        for archivo in archivos:
            print("-", archivo)

    elif opcion=="3":
        nombre=input("¿Que nombre llevara la nueva carpeta?:")
        os.mkdir(nombre)
        try:
            print("Carpeta creada correctamnete!")
        except:
            print("La carpeta no se pudo crear.")

    elif opcion=="4":
        nombre=input("nombre de la carpetra que se quiere borrar: ")
        os.rmdir(nombre)
        try: ##rl comando try sirve para ejecutar un bloque de codigo que podria falllar, este lo ejevutara sin detener el resto.
            print("la carpeta se elimino correctamente!!")
        except:
            print("la carpeta no se pudo borrar.")     

    elif opcion=="5":
        ruta=input("Ingresa la ruta del nuevo directorio: ")
        try: 
            os.chdir(ruta)
            print("Directorio cambiado correctamente!")
        except:
            print("No se pudon cambiar de directorio.")

    elif opcion=="x":
        print("Saliendo del programa.")
        break

    else:
        print("Opocion no valida")   