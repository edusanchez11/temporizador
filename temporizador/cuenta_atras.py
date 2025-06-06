import time

def cuenta_atras(segundos):
    while segundos:
        print(f"Tiempo restante: {segundos} segundos", end="")
        time.sleep(1)
        segundos -= 1
    print("tiempo finalizado")