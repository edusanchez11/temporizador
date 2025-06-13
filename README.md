# temporizador

Pequeña librería Python que permite ejecutar:
- Un **cronómetro** con inicio y parada manual
- Una **cuenta atrás** en segundos

# Clonar Repositorio

git clone https://github.com/edusanchez11/temporizador.git

cd temporizador

## 📦 Instalación

Desde el directorio raíz del proyecto:

```bash
pip install -e .
```

## 🚀 Uso
Ejecutar el script funcional

```bash
python scripts/main.py
```
Verás el menú:
1. Cuenta atrás
2. Cronómetro

## 🔧 Estructura del proyecto
```bash
temporizador/
├── scripts/               # Script funcional
│   └── main.py
├── temporizador/          # Código fuente de la librería
│   ├── cuenta_atras.py
│   ├── cronometro.py
│   └── __init__.py
├── test/                  # Pruebas automáticas
│   └── test_temporizador.py
├── README.md
├── setup.py               # Instalador
```
## 📋 Autor

Eduardo Sánchez

Máster en Data Science & IA

GitHub: @edusanchez11
