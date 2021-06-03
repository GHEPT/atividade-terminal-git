#02 - Utilizando estruturas de repetição com variável de controle, faça um programa que receba uma string com uma frase informada pelo usuário e conte quantas vezes aparece as vogais a,e,i,o,u e mostre na tela, depois mostre na tela essa mesma frase sem nenhuma vogal.

cont = 0 # VAI CONTAR QUANTAS VOGAIS HAVERÁ NA FRASE DO USUÁRIO
a = input('\nDigite uma frase: ').lower() # NECESSÁRIO TRANSFORMAR O INPUT DO USUÁRIO PARA DAR BOM NA CONDIÇÃO
for i in a: # TODA VEZ QUE O CONTADOR PASSAR POR UM CARACTERE DA FRASE
   if i in 'aáàãeéêiíoôóuú': # SE O CONTADOR ENCONTRAR QUALQUER UM DESSES CARACTERES
      cont += 1 # O CONTADOR SOMA 1
      a = a.replace(i, ' ') # E A FRASE DO USUÁRIO PERDE A VOGAL ENCONTRADA NAQUELA RODADA DO CONTADOR 
print()
print('-=' * 30)
print(f'A sua frase contém {cont} vogais')
print('-=' * 60)
print(f'Esta mesma frase sem vogais ficaria assim: [ {a} ]')
print('-=' * 60)
