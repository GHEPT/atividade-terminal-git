#03 - Utilizando estruturas de repetição com teste lógico, faça um programa que peça uma senha para iniciar seu processamento, só deixe o usuário continuar se a senha estiver correta, após entrar dê boas vindas a seu usuário e apresente a ele o jogo da advinhação, onde o computador vai “pensar” em um número entre 0 e 10. O jogador vai tentar adivinhar qual número foi escolhido até acertar, a cada palpite do usuário diga a ele se o número escolhido pelo computador é maior ou menor ao que ele palpitou, no final mostre quantos palpites foram necessários para vencer.

import time
from random import randint
# EU DIVIDI AS FRASES PARA IMPRIMIR COM TEMPORIZAÇÕES DIFERENTES
frase1 = 'JOGO DA ADVINHAÇÃO\n\nEstou pensando em um número entre 1 e 10.\nSerá que você consegue acertar qual é?'
frase2 = '\nApós cada palpite eu te dou uma dica.'
frase3 = '\nVALENDOOO...'
palpite = 0 # VAI CONTAR QUANTAS VEZES O USUÁRIO PALPITOU ATÉ ACERTAR

senha = input('Digite sua senha: ')
while senha != '#JESUS2021': # VALIDAÇÃO DA SENHA
   senha = input('\nSenha incorreta. \nDigite sua senha: ') # SE ERRAR A SENHA VAI FICAR PEDINDO SENHA
   if senha == '#JESUS2021':
      break # SE ACERTAR A SENHA SAI DO LOOPING
time.sleep(1)
print('\nSeja bem vindo, Eduardo!')
time.sleep(1)

print() # PRA PULAR UMA LINHA
print('-=' * 44) # PRA IMPRIMIR UMA ESPÉCIE DE SEPARADOR DE LINHA
for i in frase1: # CONTADOR PARA IMPRIMIR A PRIMEIRA FRASE LETRA POR LETRA
   print(i, end = ' ') # ESTOU PEDINDO PARA IMPRIMIR NA MESMA LINHA E COM UM ESPAÇO ENTRE CADA CARACTERE
   time.sleep(.08)
time.sleep(1)
print()

for i in frase2:
   print(i, end = ' ')
   time.sleep(.08)
time.sleep(1)
print()

for i in frase3:
   print(i, end = ' ')
   time.sleep(.1)
print()
print('-=' * 44)
time.sleep(1)
# NÚMERO ALEATÓRIO DO COMPUTADOR
jogo = randint(1, 10)
resp = int(input('\nDigite um número inteiro entre 1 e 10: ')) # TENTATIVA 1 DO USUÁRIO
palpite += 1 # CONTADOR RECEBE MAIS 1 
while True: # LOOPING ENQUANTO O USUÁRIO NÃO ACERTAR 
   if resp > jogo: # DÁ UMA DICA PARA O USUÁRIO
      print('\n[ ERROU ] - Eu pensei em um número [ MENOR ]')
      resp = int(input(f'Faça um novo palpite [ menor que {resp} ]: '))
      palpite += 1
   elif resp < jogo:
      print('\n[ ERROU ] - Eu pensei em um número [ MAIOR ]')
      resp = int(input(f'Faça um novo palpite [ maior que {resp} ]: '))
      palpite += 1
   elif resp == jogo:
      break
print()
print('-=' * 44)
print(f'\n[ ACERTOOOUUU ] - Parabéns! Você acertou no {palpite}º palpite.\n')
print('-=' * 44)
