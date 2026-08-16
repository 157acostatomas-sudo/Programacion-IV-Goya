import json

# Creo una funcion para validar los datos del archivo. 
def validar_datos(archivo_salida):
        try:
            with open(archivo_salida, 'r') as archivo:
                datos = json.load(archivo)
                for producto in datos:
                    if not isinstance(producto['id'], int):
                        raise ValueError(f"El id del producto {producto['nombre']} no es un número entero.")
                    if not isinstance(producto['precio'], (int, float)):
                        raise ValueError(f"El precio del producto {producto['nombre']} no es un número.")
                    if not isinstance(producto['stock'], int):
                        raise ValueError(f"El stock del producto {producto['nombre']} no es un número entero.")
                print("Todos los datos son válidos.")
                return datos
        except (ValueError, TypeError) as e:
            print(f"Error en la validación: {e}")
            return None