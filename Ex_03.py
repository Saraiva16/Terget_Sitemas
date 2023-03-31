
#3)
print("Vamos calcular os valores")

c_dias = 0
resp = "S"
while resp in "Ss":
    dia = float(input("Digite o faturamento do dia: R$"))
    resp = str(input('Quer continuar ? [S/N] '))
    c_dias += 1
    maior = dia
    menor = dia
    if maior == 0:
        maior = 0
    else:
        if maior > 0:
            maior

print(f'Dos {c_dias} dias registrados...')
print(f'O maior faturamento foi de R${maior}.')
print(f'E o menor faturamento foi de R${menor}')
