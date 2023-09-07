# Solicitar el precio del producto en euros con dos decimales
precio_str = input("Por favor, introduce el precio del producto en euros (con dos decimales): ")

# Convertir el precio a un número decimal
precio = float(precio_str)

# Calcular la parte de euros y céntimos
euros = int(precio)
centimos = int((precio - euros) * 100)

# Imprimir el número de euros y céntimos
print("Número de euros:", euros)
print("Número de céntimos:", centimos)
