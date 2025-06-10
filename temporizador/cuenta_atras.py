# Temporizador que cuenta atrás desde un número de segundos dado.

import time

def cuenta_atras(segundos):
    while segundos:
        print(f"Tiempo restante: {segundos} segundos")
        time.sleep(1)
        segundos -= 1
    print("Tiempo finalizado")
