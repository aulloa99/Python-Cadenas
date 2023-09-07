# Solicitar el nombre completo del usuario
nombre_completo = input("Por favor, introduce tu nombre completo: ")

# Formatear el nombre completo en minúsculas
nombre_min = nombre_completo.lower()

# Formatear el nombre completo en mayúsculas
nombre_may = nombre_completo.upper()

# Formatear el nombre con la primera letra de cada palabra en mayúscula
nombre_cap = nombre_completo.title()

# Imprimir las tres versiones del nombre
print("Nombre en minúsculas:", nombre_min)
print("Nombre en mayúsculas:", nombre_may)
print("Nombre con iniciales en mayúsculas:", nombre_cap)
