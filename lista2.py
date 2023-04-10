'''Crie um programa que vai ler vários números e colocar em uma lista.                 
 Depois disso, mostre:        A) Quantos números foram digitados.             B) A lista de valores, ordenada de forma decrescente.       C) Se o valor 5 foi digitado e está ou não na lista.'''

num = list()

while True:
    n = int(input('Digite um numero: '))
    num.append(n)
    print('Valor adicionado')
    r = str(input('Deseja continuar [S/N]: '))
    if r in 'Nn':
        break
    
print(' Obrigada!  ' )
print('= = '*30)
num.sort(reverse=True)
print(f'Foram Digitados {len(num)}')
print(f'Segue a lista ordenada de forma decrescente {num}')
print(f' O numero cinco foi digitado {num.count(5)} x ')

if 5 in num:
    print('O valor cinco esta na lista')
else:
    print(' o Valor cinco não esta na lista ')