###programa para loja de tintas.
area = int(input('Digitea area a ser pintada: '))

litros = area//3
if area % 3 > 0:
    litros = litros + 1

print ('Voce precisa de',litros,'litros')

latas = litros //18
if litros % 18  > 0:
    latas = latas+1
print('Você precisará de',latas, 'latas')
