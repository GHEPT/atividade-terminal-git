#08 - Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário. Se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente , além da idade, com quantos anos a pessoa vai se aposentar. Considere que o trabalhador deve contribuir por 35 anos para se aposentar.

from datetime import date
cadastro = dict() # CRIA UM DICIONÁRIO VAZIO
cadastro['Nome'] = input('Digite o seu nome: ') # CRIA UMA CHAVE 'NOME' NO DICIONÁRIO COM O VALOR QUE O USUÁRIO VAI DIGITAR
ano = cadastro['Ano de Nascimento'] = int(input('Digite o ano de nascimento: ')) # CRIA UMA CHAVE 'ANO DE NASCIMENTO' NO DICIONÁRIO COM O VALOR QUE O USUÁRIO VAI DIGITAR E TAMBÉM GUARDA O VALOR NA VARIÁVEL ANO
ctps = cadastro['CTPS'] = int(input('Informe o número da CTPS (digite 0 caso não tenha CTPS): ')) # CRIA UMA CHAVE 'CTPS' NO DICIONÁRIO COM O VALOR QUE O USUÁRIO VAI DIGITAR E TAMBÉM GUARDA O VALOR NA VARIÁVEL CTPS
cadastro['Idade'] = date.today().year - ano # CRIA UMA CHAVE 'IDADE' NO DICIONÁRIO COM O VALOR CALCULADO PELO ANO ATUAL MENOS ANO DE NASCIMENTO
if ctps == 0: # CONDICIONAL PEDIDO PELO ENUNCIADO
    contr = cadastro['Ano de Contratação'] = int(input('Digite o ano de contratação: ')) # CRIA UMA CHAVE 'ANO DE CONTRATAÇÃO' NO DICIONÁRIO COM O VALOR QUE O USUÁRIO VAI DIGITAR E TAMBÉM GUARDA NA VARIÁVEL CONTR QUE SERÁ USADA NA F STRING 
    cadastro['Salário'] = float(input('Informe o salário em R$: ')) # CRIA UMA CHAVE 'SALÁRIO' NO DICIONÁRIO COM O VALOR QUE O USUÁRIO VAI DIGITAR  
    print('-=' * 30)
    print(f'Você irá se aposentar com {(contr - ano) + 35} anos')
print('-=' * 30)
print('DICIONÁRIO CRIADO\n')
print(cadastro)
print('-=' * 30)
