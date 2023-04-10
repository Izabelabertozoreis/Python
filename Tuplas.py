lanche = ( 'hamburguer', 'suco', 'pizza', 'pudim')
print(sorted(lanche))

#for cont in range(0, len(lanche)):
   #print(f'eu vou comer {lanche[cont]} na posição {cont})
    
for pos, comida in enumerate(lanche):
    print(f'eu vou comer {comida} na posição {pos}') 