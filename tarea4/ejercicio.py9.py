fecha_nacimiento = input("Por favor, introduce tu fecha de nacimiento (dd/mm/aaaa): ")

dia, mes, anio = fecha_nacimiento.split('/')

if len(dia) == 1:
    dia = '0' + dia
if len(mes) == 1:
    mes = '0' + mes
print("Día:", dia)
print("Mes:", mes)
print("Año:", anio)
