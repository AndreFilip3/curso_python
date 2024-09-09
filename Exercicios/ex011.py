largura = float(input('Digite a largura da parede (em metros): '))
altura = float(input('Digite a altura da parede (em metros): '))
area = (altura * largura)
tinta = area/2

print('Sua parede tem a dimensão de {} x {} e sua área é de {}m²'.format(largura, altura, area), end = ' ')
print('Para pintar essa parede, você precisará de {} litros de tinta'.format(tinta))