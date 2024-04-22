# Lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a']

# Inicializando a soma
soma = 0

# Utilizando um loop for para calcular a soma dos números na lista
for numero in numeros:
    if isinstance(numero, int) or isinstance(numero, float):
        # Se o elemento for numérico, adicioná-lo à soma
        soma += numero
    else:
        # Se o elemento não for numérico, imprimir uma mensagem de erro
        print(f"Erro: Elemento '{numero}' não é numérico e será ignorado.")

# Imprimir a soma
print("A soma dos números é:", soma)


# Função para calcular a média dos valores em uma lista
def calcular_media(valores):
    try:
        # Tentativa de calcular a média
        media = sum(valores) / len(valores)
        return media
    except ZeroDivisionError:
        # Lidar com a divisão por zero caso a lista esteja vazia
        print("Erro: A lista está vazia, não é possível calcular a média.")
        return None

# Exemplo de lista de valores
lista_valores = [10, 20, 30, 40, 50]

# Calcular a média dos valores na lista
media = calcular_media(lista_valores)

# Imprimir a média
if media is not None:
    print("A média dos valores é:", media)
