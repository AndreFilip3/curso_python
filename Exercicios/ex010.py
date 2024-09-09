real = float(input('Quantos reais(R$) você tem na carteira? R$'))
conversao = (real/3.27)

print('Você pode comprar ${:.2f}'.format(conversao))