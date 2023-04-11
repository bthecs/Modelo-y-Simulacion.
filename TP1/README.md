
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

- Capacidad máxima del terreno
- Población inicial de liebres
- Población inicial de zorros
- Porcentaje de sobrevivencia de los zorros
- Porcentaje de crecimiento de las liebres
- Porcentaje de sobrevivencia de los zorros
- Porcentaje de pérdida de liebres
- Cantidad de semanas a simular

Después de ingresar los valores, el programa generará tres gráficos:

- Una tabla que muestra la población de liebres y zorros por semana
- Una gráfica de la población de liebres y zorros en función del tiempo
- Un diagrama de fase que muestra la población de zorros en función de la población de liebres.