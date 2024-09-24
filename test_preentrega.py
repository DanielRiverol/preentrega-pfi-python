import app  # Importamos el archivo que contiene el código

def setup_function():
    # Inicializar la lista de productos antes de cada test
    app.productos = []

def test_agregar_producto():
    resultado = app.agregar_producto("Manzana", 10)
    assert resultado == "Producto agregado con éxito."
    assert len(app.productos) == 1
    assert app.productos[0] == ["Manzana", 10]

def test_mostrar_productos_vacio():
    resultado = app.mostrar_productos()
    assert resultado == "No hay productos registrados."

def test_mostrar_productos_con_productos():
    app.agregar_producto("Manzana", 10)
    app.agregar_producto("Banana", 5)
    resultado = app.mostrar_productos()
    assert "Producto 1 : Nombre: Manzana, Cantidad: 10" in resultado
    assert "Producto 2 : Nombre: Banana, Cantidad: 5" in resultado

def test_opcion_invalida():
    resultado = app.ejecutar_opcion(99)
    assert resultado == "Opción inválida, por favor intentá de nuevo."

def test_salir_del_menu():
    resultado = app.ejecutar_opcion(3)
    assert resultado == "Saliendo del sistema de inventario..."
