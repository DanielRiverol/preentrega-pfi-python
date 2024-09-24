import pytest
import app  # Asegúrate de que el archivo app.py esté en el mismo directorio o en un directorio dentro de sys.path

def test_agregar_producto():
    """Verifica que se pueda agregar un producto correctamente."""
    app.productos = []
    app.agregar_producto("Manzana", 10)
    assert app.productos == [["Manzana", 10]]

def test_mostrar_productos_sin_productos():
    """Verifica que se muestre el mensaje correcto cuando no hay productos."""
    app.productos = []
    # Aquí simulamos la impresión y verificamos el resultado
    with pytest.raises(SystemExit) as pytest_exit:
        with pytest.capsys() as capsys:
            app.mostrar_productos()
    captured = capsys.readouterr()
    assert captured.out == "No hay productos registrados.\n"
    assert pytest_exit.type == SystemExit

def test_mostrar_productos_con_productos():
    """Verifica que se muestre la lista de productos correctamente."""
    app.productos = [["Manzana", 10], ["Banana", 5]]
    # Aquí simulamos la impresión y verificamos el resultado
    with pytest.raises(SystemExit) as pytest_exit:
        with pytest.capsys() as capsys:
            app.mostrar_productos()
    captured = capsys.readouterr()
    assert "Manzana" in captured.out
    assert "Banana" in captured.out
    assert pytest_exit.type == SystemExit