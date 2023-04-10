'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.'''
lista = list()
listapar = []
listainpar = []

while True:
    n = (int(input('Digite um numero: ')))
    lista.append(n)
    if n % 2 == 0:
        listapar.append(n)
    else:
        listainpar.append(n)
    r = str(input('Deseja continuar [S/N]: '))
    if r in 'Nn':
        break

print(f'{lista}')
print(f'{listapar}')
print(f'{listainpar}')