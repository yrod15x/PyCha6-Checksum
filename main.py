from CheckSum import Checksum

print("""*** Programa que muestra el restante de sumar los digitos de un numero 
entero que a su vez son multiplicados por una sucesion de 1 hasta la cantidad
de estos digitos *** """)
print()

suma = Checksum()
suma.entrada_dato()

print(f"El resultado del CHECKSUM es {suma.mostrar_checksum()}")
print()