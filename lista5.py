'''Faça um programa que leia nome e peso de várias pessoas,guardando tudo em uma lista. No final mostre:   A) Quantas pessoas foram cadastradas.  B) Uma listagem com as pessoas mais pesadas.  C) Uma listagem com as pessoas mais leves.'''

temp = list()
dados = []
maior = menor = 0
while True:
    temp.append(str(input('nome: ')))
    temp.append(float(input('Seu peso: ')))
    dados.append(temp[:])
    temp.clear()
    
    
    r = str(input(('Deseja cadastrar mais um? ')))
    if r in 'Nn':
        break

print(f'{len(dados)}')