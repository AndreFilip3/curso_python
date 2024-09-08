aluno = str(input('Digite o nome do aluno: '))
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
soma_notas = nota1+nota2
media = soma_notas/2

print('A média de {} é: {:.2f}'.format(aluno, media))
