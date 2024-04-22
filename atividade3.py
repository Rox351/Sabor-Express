soma_impares = 0

numeros = ['1','2','3','4','5','6','7','8','9','10']
nomes = ['Andre','Lucas','Bernado','Luiz']
ano = ['1998','2001','2002','2003']

# Utilizando loop for para percorrer todos os elementos da lista
for numero in numeros:
    print(numero)

for nome in nomes:
    print(nome)

for a in ano:
    print(a)


for numero in range(1, 11):
    if numero % 2 != 0:  # Verifica se o número é ímpar
        soma_impares += numero

print("A soma dos números ímpares de 1 a 10 é:", soma_impares)

for numero in range(10, 0, -1):
    print(numero)

numero = int(input("Digite um número para ver sua tabuada: "))

# Utilizar um loop for para imprimir a tabuada do número fornecido
print(f"Tabuada do {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
