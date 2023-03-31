#Código feito em Python
#5)
new_string = ""
frase = str(input('Digite uma frase: '))
print(f'Você digitou: {frase}')
for palavra in frase.split(" "):
    new_string += palavra[::-1]+" "
print(f'A frase que você digitou invertida fica: {new_string}')
