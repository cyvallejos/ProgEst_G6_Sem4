#El siguiente ejercicio pide leer n cantidad de notas, decir si es aprendizaje incial, fundamental, satisfactorio, avanzado y muestra todas las notas.
def clasificar_nota(note):
    if 1 <= note <= 59:
        return "Aprendizaje inicial"
    elif note <= 69:
        return "Aprendizaje fundamental"
    elif note <= 89:
        return "Aprendizaje satisfactorio"
    elif note <= 100:
        return "Aprendizaje avanzado"
    else:
        return "Nota inválida"


def programa():
    notas = []
    cantidad = int(input("¿Cuántas notas desea ingresar? "))

    for i in range(cantidad):
        note = float(input(f"Ingrese la nota {i + 1} (1-100): "))
        notas.append(note)

    print("\nTodas las notas:")
    for note in notas:
        print(f"{note} - {clasificar_nota(note)}")


programa()