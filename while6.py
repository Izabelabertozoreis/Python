

while True:
    n = int(input('escolha um numero para a tabuada: '))
    if n < 0:
        print('O numero escolhido é negativo!  ENCERRANDO O PROGRAMA')
        break   
    print('-' * 30)
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-' * 30)
    