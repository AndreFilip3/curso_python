obj = input('Digite o que quiser: ')

#Verificando o tipo da variável digitada
print('O tipo primitivo que você digitou é: ', type(obj))

print('O que foi digitado é um número? ', obj.isnumeric())
print('O que foi digitado é uma letra? ', obj.isalpha())
print('O que foi digitado é alfanumérico? ', obj.isalnum())
print('O que foi digitado é um número decimal? ', obj.isdecimal())
print('O que foi digitado é um espaço? ', obj.isspace())
print('O que foi digitado está em letras maiúsculas?', obj.isupper())
print('O que foi digitado está em letras minúsculas? ', obj.islower())
print('O que foi digitado é um caracter da tabela ASCII? ', obj.isascii())