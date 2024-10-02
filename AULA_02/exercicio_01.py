#Tendo como dado de entrada a altura (h) de uma pessoa, construa um programa que calcule o seu peso ideial, utilizando as seguintes fórmulas
#* Para homens: (72.7*h) - 58
#* Para mulheres: (62.1*h) - 44.7

#altura1 = float(input("Insira a sua altura: "))
#altura2 = altura1

#result = (72.7 * altura1) - 58
#result2 = (62.1 * altura2) - 44.7

#print("Se você for homem, seu peso ideal é: ", result , "Se você for mulher, seu peso ideal é: ", result2)



#Escreva um programa que efetue o cálculo do valor de uma prestração em atraso, utilizando a fórmula: valorfinal = prestacao +(prestacao*(taxa/100)*tempo)

#prestacao = float(input("Qual é o valor da prestação ? "))
#taxa = float(input("Qual é o valor da taxa ? "))
#tempo = int(input("Por quantos meses ? "))

#result = prestacao + (prestacao*(taxa/100)*tempo)

#print(f"O valor em atraso será de R$ {result:.2f}") #O f e o 2f é pra diminuir a casa decimal

#Crie um programa que calcule a idade de uma pessoa a partir do ano de nascimento dela 


#import datetime 

#data_atual = datetime.date.today()
#ano_atual = data_atual.year

#nascimento = int(input("Insira seu ano de nascimento: "))
#result = data_atual.year - nascimento
#print("A sua idade é de:",result, "anos")


# Faça um programa que leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit.A fórmula de conversão é: F = (9 * C + 160) / 5, na qual F é a temperatura em Fahrenheit e C é atemperatura em Celsius;

temperatura = float(input("Insira a temperatura em Celcius"))

temperatura = ( 9 * temperatura + 160) / 5

print("A temperatura atual é de:", temperatura,"ºF")
