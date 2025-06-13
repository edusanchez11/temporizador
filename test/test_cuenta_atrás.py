from temporizador.cuenta_atras import cuenta_atras

def test_cuenta_atras_simple(monkeypatch):
    # Evita la espera real
    monkeypatch.setattr("time.sleep", lambda x: None)
    # Ejecuta la función con 2 segundos
    resultado = cuenta_atras(2)
    assert resultado is True
