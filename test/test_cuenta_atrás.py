from temporizador.cuenta_atras import cuenta_atras

'''
Pruebas para la función cuenta_atras del módulo temporizador.
Realiza una cuenta atrás desde un número de segundos dado.
El monkeypatch se usa para simular la entrada del usuario y evitar esperas reales.
'''
def test_cuenta_atras_simple(monkeypatch):
    # Evita la espera real
    monkeypatch.setattr("time.sleep", lambda x: None)
    # Ejecuta la función con 2 segundos
    resultado = cuenta_atras(2)
    assert resultado is True
