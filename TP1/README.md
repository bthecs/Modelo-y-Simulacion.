
# Simulación de Población de Liebres y Zorros

Este es un programa que simula la población de liebres y zorros en un terreno, utilizando las ecuaciones de Lotka-Volterra.

### Requerimientos
- Python 3.x
- matplotlib
- plotly
- pandas
- prettytable

### Instrucciones de uso

Abre un terminal o consola de comandos en el directorio donde se encuentra el archivo.

Ejecuta el archivo con el siguiente comando:

```python
python depredador-presa.py
```


El programa solicitará ingresar una serie de valores para configurar la simulación:

- Capacidad máxima del terreno expresada con un numero entero, Ejemplo(1000,2000)
- Población inicial de liebres expresada con un numero entero, Ejemplo(1000,2000)
- Población inicial de zorros expresada con un numero entero, Ejemplo(1000,2000)
- Porcentaje de sobrevivencia de los zorros expresada con un numero flotante, Ejemplo(0.2,0.1)
- Porcentaje de crecimiento de las liebres expresada con un numero flotante, Ejemplo(0.08,0.05)
- Porcentaje de sobrevivencia de los zorros expresada con un numero flotante, Ejemplo(0.0004,0.000016)
- Porcentaje de pérdida de liebres expresada con un numero flotante, Ejemplo(0.0002,0.000001)
- Cantidad de semanas a simular expresadas en numero entero, Ejemplo(5000, 10000)

Después de ingresar los valores, el programa generará tres gráficos:

- Una tabla que muestra la población de liebres y zorros por semana
- Una gráfica de la población de liebres y zorros en función del tiempo
- Un diagrama de fase que muestra la población de zorros en función de la población de liebres.

# Imagenes de ejemplos
