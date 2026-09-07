#Calcular_iva está fuera de procesar_venta para poder reutilizarse.
def calcular_iva(subtotal):
	return subtotal * 0.15


def procesar_venta(subtotal):
	iva = calcular_iva(subtotal)
	return subtotal + iva


total = procesar_venta(2000)
print("Total: C$", total)