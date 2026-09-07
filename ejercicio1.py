def calcular_pago(horas, tarifa):
	pago = horas * tarifa
	print("Pago dentro de la función: C$", pago)
	return pago


pago = calcular_pago(40, 120)
print("Pago fuera de la función: C$", pago)