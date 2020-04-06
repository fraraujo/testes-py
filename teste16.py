#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
#Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
#Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

m2 = float(input("Digite quantos m² tem a área a ser pintada "))
tinta = m2 / 3
ltinta = 18 
ptinta = 80
qtinta = tinta / ltinta
vtinta = qtinta * ptinta

print("Você deverá comprar ", qtinta, "latas de tinta no valor de", vtinta)