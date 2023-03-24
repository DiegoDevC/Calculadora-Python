import math

# Formula esfera
def volume_esfera(raio):
    return 4/3 * math.pi * raio**3

# retangulo
def area_retangulo(base, altura):
    return base * altura

# hipotenusa
def hipotenusa(cateto1, cateto2):
    return math.sqrt(cateto1**2 + cateto2**2)

# regra de três simples
def regra_de_tres(valor1, valor2, valor3):
    return valor3 * valor2 / valor1


print("Bem-vindo(a) à calculadora")
print("Escolha a opção desejada:")
print("1 - Calcular o volume de uma esfera")
print("2 - Calcular a área de um retângulo")
print("3 - Calcular a hipotenusa de um triângulo retângulo")
print("4 - Calcular uma regra de três simples")
opcao = int(input("Digite a opção desejada: "))


if opcao == 1:
    raio = float(input("Digite o raio da esfera: "))
    resultado = volume_esfera(raio)
    print("O volume da esfera é:", resultado)
elif opcao == 2:
    base = float(input("Digite a base do retângulo: "))
    altura = float(input("Digite a altura do retângulo: "))
    resultado = area_retangulo(base, altura)
    print("A área do retângulo é:", resultado)
elif opcao == 3:
    cateto1 = float(input("Digite o primeiro cateto do triângulo: "))
    cateto2 = float(input("Digite o segundo cateto do triângulo: "))
    resultado = hipotenusa(cateto1, cateto2)
    print("A hipotenusa do triângulo é:", resultado)
elif opcao == 4:
    valor1 = float(input("Digite o primeiro valor da regra de três: "))
    valor2 = float(input("Digite o segundo valor da regra de três: "))
    valor3 = float(input("Digite o terceiro valor da regra de três: "))
    resultado = regra_de_tres(valor1, valor2, valor3)
    print("O valor da regra de três é:", resultado)
else:
    print("Opção inválida")
