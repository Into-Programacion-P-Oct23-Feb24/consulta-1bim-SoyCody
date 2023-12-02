suma_notas = 0
notas = []
c = True
num_notas = 0
while c == True:
    nota = float(input(f"Ingrese la nota: "))
    notas.append(nota)
    suma_notas += nota
    c += 1
    num_notas += 1
    print("Desea continuar? Presione x para mostrar el promedio")
    bandera = str(input())
    if bandera == "x":
        c = False
    else:
        c = True
promedio = suma_notas / num_notas
print(f"\nPromedio final: {promedio}")