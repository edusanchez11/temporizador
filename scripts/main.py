from temporizador.cronometro import cronometro
from temporizador.cuenta_atras import cuenta_atras
import time

# función principal

def main():
    """
    Muestra un menú para elegir entre cuenta atrás y cronómetro.
    """
    print("Prueba de funciones de temporizador")
    print("1. Cuenta atrás")
    print("2. Cronometro")
    opcion = input("Selecciona una opción (1 o 2): ")

    # Ejecutar la función según la opción seleccionada
    
    if opcion == "1":
        segundos = int(input("Introduce el número de segundos para la cuenta atrás: "))
        cuenta_atras(segundos)
    elif opcion == "2":
        cronometro()
    else:
        print("Opción no válida")


if __name__ == "__main__":
    # Ejecutar la función principal
    main()