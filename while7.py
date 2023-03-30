'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''
from random import choice
cont = 0
while True: 
    
    n = choice([1, 5])
    print('VAMOS JOGAR PAR OU IRMPA?? ')
    print('=*' * 30)
    jogador = str(input('você é par ou impar? ')).upper()
    if jogador == 'PAR':
        computador = 'IMPAR'
    else:
        computador = 'PAR'
    print('=*' * 30)
    print(f' Você escolheu {jogador}, então eu sou {computador}') 
    print('=*' * 30)

    njogador = int(input('Escolha seu numero: '))
    print(f'Eu escolho {n}')
    x = njogador + n
    if x % 2 == 0:
        valor = 'PAR'
    else: 
        valor = 'IMAPR'
    print(f'Deu... {valor}')
    if jogador == valor:
        print('PARABÉNS VOCÊ GANHOU!')
        cont += 1
    else:
        print('Poxa, não foi desta vez!')
        break

print('=*' * 30)

print(f'GAME OVER, VOCÊ GANHOU {cont} VEZES')