#Faça um programa para ler: a descrição do produto (nome), a quantidade adquirida e o preço unitário. Calcular e escrever o total (total = quantidade adquirida * preço unitário), o desconto e o total a pagar (total a pagar = total - desconto), sabendo que:
# - se quantidade <= 5 o desconto será de 2%
# - Se a quantidade > 5 e quantidade <=10 o desconto será de 3%.
# - Se a quantidade > 10 o desconto será de 5%

# try:
#     nome_produto = input(("Por favor, digite o nome do produto que você deseja adquirir: "))
#     quantidade_adquirida = int(input("Por favor, digite a quantidade que você deseja adquirir: "))
#     preco_unitario = float(input("Digite o valor do produto: "))

# except ValueError:
#     print("Insira o valor corretamente!")
# else:    
    
#     total = quantidade_adquirida * preco_unitario

#     if quantidade_adquirida <=5:
#         print("A sua quantidade a pagar será de R$:",total * 0.98)

#     elif quantidade_adquirida > 5 and quantidade_adquirida <=10:
#         print("A sua quantidade a pagar será de R$:",total * 0.97 )    

#     else:
#         print("A sua quantidade a pagar será de R$:",total * 0.95 )


# Uma empresa quer verificar se um empregado está qualificado para a aposentadoria ou não.

# Para estar em condições, um dos seguintes requisitos deve ser satisfeito:

# - Ter no mínimo 65 anos de idade.
# - Ter trabalhado no mínimo 30 anos.
# - Ter no mínimo 60 anos e ter trabalhado no mínimo 25 anos.
# Com base nas informações acima, faça um programa que leia: o nome do empregado, o ano

# de nascimento e o ano que entrou na empresa.

# O programa deverá escrever a idade e o tempo trabalhado do empregado acompanhado da

# seguinte mensagem: ‘Apto a Aposentadoria' ou ‘Inapto a Aposentadoria’.

import datetime

data_atual = datetime.date.today()
 
ano_atual = data_atual.year

try:

    nome_empregado = input("Insira o seu nome: ")
    ano_nascimento = int(input("Insira a sua data de nascimento: "))
    ano_admissao = int(input("Insira o ano de contratação: "))
except ValueError:
    print("Verifique os dados!")

else:      
    idade = ano_atual - ano_nascimento
    contribuicao = ano_atual - ano_admissao

    if idade >= 65:
        print("Apto para aposentadoria")
    elif contribuicao >=30:
        print("Apto para aposentadoria")
    elif idade >= 60 and contribuicao >=25:
        print("Apto para aposentadoria")
    else:
         print("Você está inapto para aposentadoria")

