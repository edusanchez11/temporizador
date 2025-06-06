import time

def cronometro(func):
    # Guardar el tiempo de inicio
    inicio = time.time()
    input("Presiona ENTER para detener el cronómetro")
    # Calcular el tiempo transcurrido
    fin = time.time()
    transcurrido = fin - inicio
    # Mostrar el tiempo transcurrido
    print(f"Duración del cronómetro: {transcurrido:.2f} segundos")