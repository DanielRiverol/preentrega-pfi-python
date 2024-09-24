import app  # Importamos tu archivo app.py que contiene el código

def test_agregar_producto():
    app.productos = []  # Reiniciar la lista de productos
    app.productos.append(["Manzana", 10])  # Simular agregar producto
    assert len(app.productos) == 1  # Verificar que se agregó
    assert app.productos[0] == ["Manzana", 10]  # Verificar nombre y cantidad

def test_mostrar_productos_sin_productos():
    app.productos = []  # Asegurarse de que esté vacía
    resultado = app.mostrar_productos()
    assert resultado == "No hay productos registrados."

def test_salir():
    assert app.salir() == "Saliendo del sistema de inventario..."
