import builtins
from temporizador.cronometro import cronometro

'''
Pruebas para la función cronometro del módulo temporizador.
Realiza un cronómetro que mide el tiempo transcurrido entre dos pulsaciones de ENTER.
El monkeypatch se usa para simular las pulsaciones de ENTER y evitar esperas reales.
'''

def test_cronometro(monkeypatch):
    # Simula dos pulsaciones de ENTER
    inputs = iter(['', ''])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))
    # Simula el tiempo para que siempre devuelva 2 segundos
    monkeypatch.setattr("time.time", lambda: test_cronometro.times.pop(0))
    test_cronometro.times = [100.0, 102.0]
    # Captura los prints
    outputs = []
    monkeypatch.setattr(builtins, "print", outputs.append)
    duracion = cronometro()
    assert abs(duracion - 2.0) < 0.01
    assert any("Duración" in str(o) for o in outputs)