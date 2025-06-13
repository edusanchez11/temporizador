# Temporizador que cuenta atrás desde un número de segundos dado.

import time

'''
Cuenta atrás interactiva que muestra el tiempo restante en formato MM:SS
y finaliza al llegar a 0.
cancelada con Ctrl+C.
'''

def cuenta_atras(segundos):
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