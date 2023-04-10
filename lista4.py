teste = list()
teste.append('Izabela')
teste.append(29)
galera = list()
galera.append(teste[:])  
teste[0] = 'maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
###########################################################################
x = [['izabela', 29], ['Juliana', 27], ['Miguel', 2], ['Artur', 32]]
print(x)

for p in x:
    print(p)
######################################################################
x = list()
dado = list()
totmai = totmen = 0
for c in range (0, 3):
    dado.append(str(input('nome: ')))
    dado.append(int(input('idade: ')))
    x.append(dado[:])
    dado.clear()

for p in x:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen +=1
print(f' temos {totmai} maiores e {totmen} menores de idade.')