# #Média do aluno com if

# nome = input("Insira o nome do Estudante")
# nota1 = int(input("Insira a primeira nota de 0 a 100: "))
# nota2 = int(input("Insira a segunda nota de 0 a 100: "))
# media = (nota1 + nota2 ) / 2
# print("O valor da média é: ", media)
# if media >= 70:
#     print("Aprovado")
# elif media >= 30 and media <70:
#     print("Recuperação")
# else: 
#     print("Reprovado")    

#Escreva um programa que, dados 2 números inteiros (n1 e n2), diga se eles são iguais ou diferentes.

# N1 = int(input("Insira o primeiro número inteiro: "))
# N2 = int(input("Insira o segundo número inteiro: "))

# if N1 != N2:
#     print("Esses números são diferentes!")
# else:
#     print("Esses números são iguais")

#2- Utilizando a estrutura do programa anterior, some os dois valores se forem diferentes e multiplique-os se forem iguais.

# N1 = int(input("Insira o primeiro número inteiro: "))
# N2 = int(input("Insira o segundo número inteiro: "))

# if N1 != N2:
#     print(N1 + N2)
# else:
#     print(N1*N2)

#Faça um programa que pergunte a uma pessoa, a sua idade, o seu peso e quanto dormiu nas últimas 24 h e diga se ela pode doar ou não sangue de acordo com as seguintes condições:

idade = int(input("Informe a sua idade: "))
peso = float(input("Informe o seu peso: "))
sono = input("Você dormiu mais de 6 horas nas últimas 24h? Escreva S para Sim e N para não" )

    
if idade >= 16 and idade < 69:
    print(True)

elif idade == "Aprovado" and peso > 50:
    print("Aprovado")

elif sono == "S" or "s" and idade == "Aprovado" and peso > 50:
    print("Aprovado")

else:
    print("Reprovado")