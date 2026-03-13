# Calculadora de média simples

numeros = []
quantidade = int(input("Quantos números você deseja inserir? "))

for i in range(quantidade):
    valor = float(input(f"Digite o {i+1}º número: "))
    numeros.append(valor)

media = sum(numeros) / len(numeros)

print(f"A média dos números é: {media:.2f}")
