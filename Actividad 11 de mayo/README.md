# Actividad 11 de Mayo - Suma con Transformación

Este script de Python procesa los primeros 10 números naturales y realiza una suma basada en una condición específica.

## ¿Qué hace el código?
El programa recorre los números del 1 al 10 y aplica las siguientes reglas:
1. **Números Pares:** Se suman tal cual están (2, 4, 6, 8, 10).
2. **Números Impares:** Se aplica la fórmula `(n * 2) - 1` antes de sumarlos.

## Explicación del resultado
Si te salía **55** antes, era porque en tu código anterior estabas sumando los números originales sin llamar correctamente a la función. 

Con este código nuevo:
* El `1` se queda como `1` (porque `1*2 - 1 = 1`).
* El `3` se vuelve `5` (porque `3*2 - 1 = 5`).
* Así sucesivamente, lo que dará un resultado **mayor a 55**.

## Requisitos
* Python 3.x
