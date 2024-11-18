
# Sopa de Letras Solver

Este proyecto implementa un programa en Python que resuelve sopas de letras, permitiendo buscar palabras en todas las direcciones posibles y generando un reporte en formato JSON.

## Tabla de Contenidos
1. [Descripción](#descripción)
2. [Instalación](#instalación)
3. [Uso](#uso)
4. [Estructura del Archivo de Entrada](#estructura-del-archivo-de-entrada)
5. [Contribuciones](#contribuciones)
6. [Licencia](#licencia)

## Descripción
El programa realiza las siguientes funciones:
1. Lee una sopa de letras y una lista de palabras desde un archivo `.txt`.
2. Busca las palabras en la sopa de letras considerando todas las direcciones (horizontal, vertical y diagonal).
3. Genera un archivo `reporte.json` que indica qué palabras fueron encontradas y cuáles no.

## Instalación
1. Clona este repositorio en tu máquina local:
   ```bash
   git clone https://github.com/1809m4n3l/Sopa_de_LETRAS.git
   ```
2. Navega a la carpeta del proyecto:
   ```bash
   cd Sopa_de_LETRAS
   ```
3. Instala las dependencias necesarias (si aplica):
   ```bash
   pip install -r requirements.txt
   ```

## Uso
1. Asegúrate de tener un archivo de entrada en formato `.txt` que contenga la sopa de letras y las palabras a buscar (ver estructura en la sección siguiente).
2. Ejecuta el programa desde la terminal:
   ```bash
   python solver.py archivo_entrada.txt
   ```
3. El resultado se guardará en un archivo `reporte.json` en la misma carpeta del proyecto.

## Estructura del Archivo de Entrada
El archivo de entrada debe tener la siguiente estructura:

```
SOPA_DE_LETRAS
A M A R S
S T E R I
O M A Z C
A L C R H
P O L O S

PALABRAS_A_BUSCAR
AMAR
OSA
ATAR
SOLO
POLOS
MEZCLAR
PALO
```

1. **SOPA_DE_LETRAS**: Define la cuadrícula de la sopa de letras, con letras separadas por espacios.
2. **PALABRAS_A_BUSCAR**: Lista de palabras a encontrar, una por línea.

## Contribuciones
¡Contribuciones son bienvenidas! Si tienes ideas para mejorar este proyecto, abre un *issue* o envía un *pull request*.

## Licencia
Este proyecto está bajo la Licencia MIT. Para más detalles, consulta el archivo `LICENSE`.
