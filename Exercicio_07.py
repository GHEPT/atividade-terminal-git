#07 - Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

pares = list() # LISTA QUE VAII RECEBER OS NÚMEROS PARES
impares = list() # LISTA QUE VAI RECEBER OS NÚMEROS ÍMPARES 

for i in range(1, 7+1): # O CONTADOR VAI PERGUNTAR 7 NÚMEROS 
   a = int(input(f'Digite o {i}º valor: '))
   if a % 2 == 0: # TESTE PRA SABER SE O NÚMERO É PAR
      pares.append(a) # SE SIM, ACRESCENTA ESSE NÚMERO DIGITADO NO FINAL DA LISTA PARES
   else:
      impares.append(a) # SE NÃO, ACRESCENTA ESSE NÚMERO DIGITADO NO FINAL DA LISTA ÍMPARES
lis_unica = sorted(pares) + sorted(impares) # GUARDA OS VALORES PARES E ÍMPARES EM UMA LISTA SÓ JÁ EM ORDEM CRESCENTE
print('-=' * 30)
print(lis_unica)
print('-=' * 30)
