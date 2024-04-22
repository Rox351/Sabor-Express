print('Digite um numero:')
numero_digitado = int(input())  # Converta a entrada para inteiro

if numero_digitado % 2 == 0:
  print('Seu numero é Par')
else:
  print('Seu numero é Impar')

print('Digite sua idade:')
idade = int(input()) #Digite sua idade

if idade <= 12:
    print('Criança')
elif idade <= 18:
    print('Adolescente')    
else:
    print('Adulto')

usuario = 'Pedro'
senha = 'p'

print('Digite seu usuario:')
input()
print('Digite sua senha:')
input()

if usuario == 'Pedro' and senha == 'p':
    print(usuario + senha )
    
    print('Usuario e senha correto!')
else :
    print('Usuário ou senha incorreto')