import time

# cronometro interactivo que mide el tiempo transcurrido entre dos pulsaciones de ENTER

def cronometro(): 
    """
    Inicia un cronómetro que mide el tiempo entre dos pulsaciones de ENTER.

    Returns:
        float or None: Duración en segundos, o None si se cancela.
    """
    try:
        input("Presiona ENTER para iniciar el cronómetro...")
        inicio = time.time()
        input("Presiona ENTER para detener el cronómetro.")
        fin = time.time()
        duracion = fin - inicio
        print(f"Duración: {duracion:.2f} segundos")
        return duracion
    except KeyboardInterrupt:
        print("\nCronómetro cancelado.")
        return None