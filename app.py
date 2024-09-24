# Lista para almacenar los productos
productos = []


# Función principal para el sistema de inventario
def main():
    # Variable de control para el bucle del menú
    opcion = 0

    # Bucle para mostrar el menú hasta que el usuario elija salir
    while opcion != 3:
        print("\n--- Menú de Inventario ---")
        print("1. Agregar producto")
        print("2. Mostrar productos")
        print("3. Salir")

        # Solicitar la opción al usuario
        opcion = int(input("Seleccioná una opción: "))

        if opcion == 1:
            # Agregar un nuevo producto
            nombre = input("Ingresá el nombre del producto: ")
            cantidad = int(input("Ingresá la cantidad del producto: "))

            # Agregar el producto a la lista como una tupla (nombre, cantidad)
            productos.append([nombre, cantidad])
            print("Producto agregado con éxito.")

        elif opcion == 2:
            # Mostrar los productos
            if len(productos) == 0:
                print("No hay productos registrados.")
            else:
                print("\n--- Lista de Productos ---")
                for i, producto in enumerate(productos):
                    print("Producto", i + 1, ": Nombre:", producto[0], ", Cantidad:", producto[1])

        elif opcion == 3:
            # Salir del programa
            print("Saliendo del sistema de inventario...")

        else:
            print("Opción inválida, por favor intentá de nuevo.")

    # Mensaje final
    print("Programa finalizado.")


if __name__ == "__main__":
    main()
