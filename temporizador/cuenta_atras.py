import time

def cuenta_atras(segundos):
    while segundos:
        print(f"\rTiempo restante: {segundos} segundos", end="", flush=True)
        time.sleep(1)
        segundos -= 1
    print("tiempo finalizado")