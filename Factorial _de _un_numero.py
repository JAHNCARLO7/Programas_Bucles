
num = int(input("Número para factorial: "))
factorial = 1

if num < 0:
    print("Factorial no definido para negativos")
else:
    for i in range(1, num + 1):
        factorial *= i
    print("El factorial de", num, "es:", factorial)

inicio = int(input("Primer número: "))
diferencia = int(input("Diferencia: "))
limite = int(input("Límite máximo: "))

num = inicio
while True:
    print(num, end=" ")
    num += diferencia
    if num > limite:
        break

print("\nSecuencia aritmética desde", inicio, "hasta", limite)