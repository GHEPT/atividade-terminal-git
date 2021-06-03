#01 - Utilizando estruturas condicionais faça um programa que pergunte ao usuário dois números e mostre:
   # A soma deles;
   # A multiplicação entre eles;
   # A divisão inteira deles;
   # Mostre na tela qual é o maior;
   # Verifique se o resultado da soma é par ou impar e mostre na tela;
   # Se a multiplicação entre eles for maior que 40, divida pelo resultado da divisão inteira e mostre o resultado na tela. Se não, mostre que a multiplicação não foi maior que 40.

import time
a = int(input('\nDigite um número: '))
time.sleep(0.5)
b = int(input('Digite outro número: '))
time.sleep(0.5)
# DEFININDO AS VARIÁVEIS
soma = a + b
mult = a * b
div = a // b
maior = a
impar = par = 0
# TESTE CONDICIONAL PARA DEFINIR O MAIOR VALOR DIGITADO
if b > a:
   maior = b
time.sleep(0.5)
# PRINTS DOS RESULTADOS
print() # ESSE SÓ IMPRIME VAZIO, COMO FORMA DE "PULAR UMA LINHA"
print('-=' * 30)  # É UMA FORMA DE IMPRIMIR UM SEPARADOR DE LINHAS, PARA FICAR ESTILOSO.
print(f'A soma de {a} + {b} é [ {soma} ]')
print('-=' * 30)
time.sleep(0.5)
print(f'A multiplicação de {a} x {b} é [ {mult} ]')
print('-=' * 30)
time.sleep(0.5)
print(f'A divisão inteira de {a} por {b} é [ {div} ]')
print('-=' * 30)
time.sleep(0.5)
print(f'O maior entre {a} e {b} é o [ {maior} ]')
print('-=' * 30)
# TESTE POSITIVO PARA NÚMERO PAR
if (a + b) % 2 == 0:
   time.sleep(0.5)
   print(f'O resultado da soma de {a} + {b} é um número [ PAR ]')
   print('-=' * 30)
else: # CASO CONTRÁRIO O NÚMERO SERÁ ÍMPAR
   time.sleep(0.5)
   print(f'O resultado da soma de {a} + {b} é um número [ ÍMPAR ]')
   print('-=' * 30)
if mult > 40: # TESTE A PEDIDO DO EXERCÍCIO
    if div > 0: # ESSA CONDIÇÃO É IMPORTANTE PARA QUE O PROGRAMA NÃO QUEBRE
       c = mult // div #SENDO POSITIVO, AGORA SIM PODEMOS FAZER O QUE O EXERCÍCIO PEDE, SENDO MULT MAIOR QUE 40
       time.sleep(0.5)
       print(f'O resultado da divisão inteira de {mult} por {div} é [ {c} ]')
       print('-=' * 30)
    elif div <= 0: # SE A MULT FOR MENOR OU IGUAL A 0, ENTRA UMA MENSAGEM ESCLARECEDORA
        time.sleep(0.5)
        print(f'Apesar de a multiplicação entre {a} e {b} ser maior que 40, não é possível dividir nenhum número por {div}.')
        print('-=' * 30)
else: # SE MULT FOR MENOR QUE 40
   time.sleep(0.5)
   print(f'A multiplicação de {a} x {b} NÃO foi maior que 40')
   print('-=' * 30)
print()
