import builtins
from temporizador.cronometro import cronometro

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