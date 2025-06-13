# Temporizador que cuenta atrás desde un número de segundos dado.

import time

def cuenta_atras(segundos):

    """
    Realiza una cuenta atrás desde el número de segundos indicado.

    Args:
        segundos (int): Número de segundos para la cuenta atrás.

    Returns:
        bool: True si finaliza correctamente, False si se cancela.
    """
    try:
        while segundos:
            mins, secs = divmod(segundos, 60)
            tiempo = f"{mins:02d}:{secs:02d}"
            print(f"Tiempo restante: {tiempo}")
            time.sleep(1)
            segundos -= 1
        print("Tiempo finalizado")
        return True
    except KeyboardInterrupt:
        print("\nCuenta atrás cancelada.")
        return False