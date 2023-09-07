productos = input("Por favor, introduce los productos de la cesta de la compra separados por comas: ")

lista_productos = productos.split(',')

print("Productos en la cesta de la compra:")
for producto in lista_productos:
    print(producto.strip())  
