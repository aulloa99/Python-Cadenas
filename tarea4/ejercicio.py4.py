# Solicitar el número de teléfono
numero_telefono = input("Por favor, introduce un número de teléfono en el formato +34-XXXXXXXXX-XX: ")

# Dividir el número en partes utilizando el guión como separador
partes = numero_telefono.split("-")

# Verificar si el número tiene el formato correcto
if len(partes) == 3 and partes[0] == "+34" and len(partes[1]) == 9 and len(partes[2]) == 2:
    numero_principal = partes[1]  # Extraer la parte central del número
    print("El número de teléfono principal es:", numero_principal)
else:
    print("El número de teléfono no tiene el formato correcto.")
