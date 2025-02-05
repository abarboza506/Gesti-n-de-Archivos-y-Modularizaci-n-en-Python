# Proyecto: [Nombre del Proyecto]
<<<<<<< Updated upstream
# Estudiante: Prof. Andrés
# Fecha de Inicio: 2025/02/24
=======
# Estudiante: Adrian Barboza Chavarría
# Fecha de Inicio: 04/02/2025
>>>>>>> Stashed changes
# Fecha de Entrega: [dd/mm/aaaa]
# Descripción: Este archivo contiene el punto de entrada principal del proyecto.
# Recuerda incluir tu nombre completo, la fecha en la que iniciaste el proyecto y la fecha estimada de entrega.
# Esto ayuda a mantener un registro claro del trabajo realizado.

<<<<<<< Updated upstream
# from analisis_datos.estadisticas import media,calcular_mediana #Importar modulos

from analisis_datos import *

lista_compras = generar_lista_de_compras()
print(lista_compras)
precios = [precio for _, precio in lista_compras]
print('Media: ', media(precios))
print('Mediana: ', calcular_mediana(precios)) 
=======
import random

def generar_lista_de_compras():
    productos = {
        'manzanas': 1000,
        'bananos': 150,
        'cerezas':2000,
        'naranjas':900,
        'pan':2275,
        'leche':900,
        'huevos':3400,
        'queso':4500,
        'sandia': 1200
    }
    seleccion = random.sample(list(productos.items()),k=5) # Selecciona 5 prodcuntos de la lista de compras
    return seleccion
>>>>>>> Stashed changes
