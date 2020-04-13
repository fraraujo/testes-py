n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

if n1 > n2:
    print(n1, "é maior que", n2, ".")
elif n2 > n1:
    print(n2, "é maior que", n1, ".")
else:
    print("Os numeros são iguais.")