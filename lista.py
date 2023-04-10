'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''

lista = []
maior = 0
menor = 0
for c in range (0, 5):
    lista.append(int(input(f'Digite uma valor {c}:  ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista [c]
        if lista[c] < menor:
            menor = lista[c]
print('=-'*30)
print(f'Você digitou os valores {lista}')

print(f'O maior valor foi {maior}')
print(f'o Menor valro foi {menor}')