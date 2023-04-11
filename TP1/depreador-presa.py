import matplotlib.pyplot as plt
import plotly.graph_objs as go


# Función de simulación
def simulacion(cap_terreno, liebres, zorros, porc_sobrev, porc_crec, porc_zorros_sobreviven, porc_perdida_liebres):
    cap_actual = cap_terreno - liebres
    tasa_liebres = (1/cap_terreno) * cap_actual * porc_crec * liebres
    caza = zorros * liebres
    liebres_nuevas = tasa_liebres - porc_perdida_liebres * caza
    zorros_nuevos = porc_zorros_sobreviven * caza - porc_sobrev * zorros
    return liebres_nuevas, zorros_nuevos

def menu():
    # Inicialización de variables
    cap_terreno = int(input("Ingrese una capacidad maxima para el terreno: "))  # Capacidad máxima del terreno
    liebres = int(input("Ingrese la cantidad de liebres en el terreno: "))   # Población inicial de liebres
    zorros = int(input("Ingrese la cantidad de zorros en el terreno: "))     # Población inicial de zorros
    porc_sobrevivencia = float(input("Ingrese el porcentaje de sobrevivencia de los zorros: ")) # Porcentaje de sobrevivencia de los zorros
    porc_crecimiento = float(input("Ingrese el porcentaje de crecimiento de las liebres: ")) # Porcentaje de crecimiento de las liebres
    porc_zorros = float(input("Ingrese el porcentaje de sobrevivencia de los zorros: ")) # Porcentaje de sobrevivencia de los zorros
    porc_perdida_liebres = float(input("Ingrese el porcentaje de perdida de liebres: ")) # Porcentaje de perdida de liebres
    # Bucle de simulación
    # cantidad de semanas
    semanas = int(input("Ingrese la cantidad de semanas a simular: "))
    dt = 0.1 # Incremento de tiempo (en semanas)
    lista_zorros = [zorros]
    lista_liebres = [liebres]
    semanas_total = []
    for i in range(semanas):
        liebres_nuevas, zorros_nuevos = simulacion(cap_terreno, liebres, zorros, porc_sobrevivencia, porc_crecimiento, porc_zorros, porc_perdida_liebres)
        liebres += dt * liebres_nuevas
        zorros += dt * zorros_nuevos
        liebres = max(min(liebres, cap_terreno), 1)
        zorros = max(min(zorros, cap_terreno), 1)
        lista_zorros.append(int(zorros))
        lista_liebres.append(int(liebres))
        semanas_total.append(i)

    return lista_zorros, lista_liebres, semanas_total

def graficos(lista_zorros, lista_liebres, semanas_total):


    # Graficar los resultados
    tabla = go.Table(
        header=dict(values=['Semanas','Zorros', 'Liebres']),
        cells=dict(values=[semanas_total, lista_zorros, lista_liebres])
    )
    # Configurar diseño de tabla
    layout = go.Layout(
        title='Población de Liebres y Zorros por Semana',
        width=720,
        height=720
    )
    # Crear gráfico de tabla y mostrarlo
    fig = go.Figure(data=[tabla], layout=layout)
    fig.show()
    # Graficar
    plt.plot(lista_zorros, label="Zorros")
    plt.plot(lista_liebres, label="Liebres")
    plt.xlabel("Semanas")
    plt.ylabel("Población")
    plt.title("Población de liebres y zorros")
    plt.legend()
    plt.show()

    # Diagrama de fase
    plt.plot(lista_liebres, lista_zorros)
    plt.xlabel("Población de liebres")
    plt.ylabel("Población de zorros")
    plt.title("Diagrama de fase")
    plt.show()
    

if __name__ == '__main__':
    lista_zorros, lista_liebres, semanas_total = menu()
    graficos(lista_zorros, lista_liebres, semanas_total)
    