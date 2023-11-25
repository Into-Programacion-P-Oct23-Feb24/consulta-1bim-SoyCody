suma_notas = 0
notas = []
contador = True
num_notas = 0
while contador == True:
    nota = float(input(f"Ingrese la nota: "))
    notas.append(nota)
    suma_notas += nota
    contador += 1
    num_notas += 1
    print("Desea continuar? Presione x para mostrar el promedio")
    bandera = str(input())
    if bandera == "x":
        contador = False
    else:
        contador = True
promedio = suma_notas / num_notas
print(f"\nPromedio final: {promedio}")