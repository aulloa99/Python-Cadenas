# Solicitar una frase al usuario
frase = input("Por favor, introduce una frase: ")

# Solicitar una vocal al usuario
vocal = input("Por favor, introduce una vocal: ")

# Verificar si la entrada es una sola vocal en minúscula
if len(vocal) == 1 and vocal.isalpha() and vocal.lower() in 'aeiou':
    # Convertir la vocal a mayúscula
    vocal_mayuscula = vocal.upper()

    # Reemplazar la vocal en minúscula por la vocal en mayúscula en la frase
    frase_con_vocal_mayuscula = frase.replace(vocal.lower(), vocal_mayuscula)

    # Mostrar la frase con la vocal en mayúscula
    print("Frase con la vocal en mayúscula:", frase_con_vocal_mayuscula)
else:
    print("La entrada de la vocal no es válida. Debe ser una sola vocal en minúscula (a, e, i, o, u).")
