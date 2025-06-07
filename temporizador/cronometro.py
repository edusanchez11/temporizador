import time

# cronometro interactivo que mide el tiempo transcurrido entre dos pulsaciones de ENTER

def cronometro():
    input("Presiona ENTER para iniciar el cronómetro...")
    inicio = time.time()
    input("Presiona ENTER para detener el cronómetro.")
    fin = time.time()
    duracion = fin - inicio
    print(f"Duración: {duracion:.2f} segundos")