
galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [F/M] ')).upper()[0]
        if pessoa['sexo'] in 'MF' :
            break
        print('ERRO, POR FAVOR DIGITE F OU M.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar a cadastrar? [S/N]: ')).upper()[0]
        if resp in 'SN ':
            break
        print('ERRO, POR FAVOR DIGITE s OU n.')
    if resp == 'N':
        break
print()
print('-=' * 30)
print()
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
print()
media = soma / len(galera)
print(f'A media de idade é {media:5.2f} Anos.')
print()
print("mulheres cadastradas foram ", end='')
for p in galera:
    if p['sexo'] in 'F' :
        print(f' {p["nome"]} ', end='' )
print()
print(' Lista de pessoas que estão acima da media: ', end=' ')
for p in galera:
    if p['idade'] >= media:
        print('    ')
        for k, v in p.items():
            print(f' {k} = {v}; ', end='')
        print()
print('<< encerrado >>')
