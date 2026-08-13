#productos = [
#    {"nombre": "Laptop", "precio": 1200, "stock": 15},
#    {"nombre": "Mouse", "precio": 25, "stock": 5},
#    {"nombre": "Teclado", "precio": 75, "stock": 25},
#    {"nombre": "Monitor", "precio": 300, "stock": 8},
#]


# print(productos[1]["nombre"])  # Salida: Mouse
# print(productos[2]["precio"])  # Salida: 75

# productos_bajo_stock = []
# for producto in productos:
#    print(f"producto: {producto['nombre']}, Precio: ${producto['precio']}")
#    if producto['stock'] < 10:
#        productos_bajo_stock.append(producto)

# print("\n Productos con bajo stock:")
# print(productos_bajo_stock)  # Salida: [{'nombre': 'Mouse', 'precio': 25, 'stock': 5}, {'nombre': 'Monitor', 'precio': 300, 'stock': 8}]


#def calcular_promedio_precio(lista):
#    if not lista:
#        return 0
#    total_precio = sum(p['precio'] for p in lista)
#    return total_precio / len(lista)
#
#precio_promedio = calcular_promedio_precio(productos)
#print(f"\n El precio promedio de los productos es: ${precio_promedio:.2f}")  # Salida: El precio promedio de los productos es: $400.00

import csv

productos_desde_csv = []

with open('datos.csv', mode='r', encoding = 'utf-8') as archivo_csv:
    lector_diccionario = csv.DictReader(archivo_csv)
    for fila in lector_diccionario:
        fila['id'] = int(fila['id'])
        fila['precio'] = float(fila['precio'])
        fila['stock'] = int(fila['stock'])

        productos_desde_csv.append(fila)

print("\n Productos desde el archivo CSV:")
print(productos_desde_csv)  # Salida: [{'id': 1, 'nombre': 'Laptop', 'precio': 1200.0, 'stock': 15}, {'id': 2, 'nombre': 'Mouse', 'precio': 25.0, 'stock': 5}, {'id': 3, 'nombre': 'Teclado', 'precio': 75.0, 'stock': 25}, {'id': 4, 'nombre': 'Monitor', 'precio': 300.0, 'stock': 8}]



