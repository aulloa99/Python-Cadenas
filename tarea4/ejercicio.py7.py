# Solicitar la dirección de correo electrónico del usuario
correo_usuario = input("Por favor, introduce tu dirección de correo electrónico: ")

# Dividir el correo electrónico en nombre de usuario y dominio
nombre_usuario, dominio = correo_usuario.split("@")

# Crear un nuevo correo electrónico con el mismo nombre de usuario y el dominio "ceu.es"
nuevo_correo = nombre_usuario + "@ceu.es"

# Imprimir el nuevo correo electrónico
print("Nuevo correo electrónico:", nuevo_correo)
