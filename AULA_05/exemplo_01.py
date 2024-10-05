#Exemplo de como utilizar o FOR

# lista = [1, 2, 3, 4]

# for item in lista:
#     print(item)

#Exemplo de como utilizar o WHILE

# contador = 0
# while contador < 10:
#     print("valor do contador é",contador)
#     contador +=1

# print("Usando o comando for.......")
# for i in range(5): #Loop  Finito de 0 a 4
#     print(i)
# print("Print usando o comando while......")    


# for i in range(5):
#     print(i)
# print("Usando o comando while...")
# i = 1
# while i <= 5: #Loop finito de 1 a 5    
#     print(i)
#     i += 1


#Repetição com while

# resp = "S"
# while resp == "S":
#     nome = input("Informe o nome do usuário")
#     resp = input("Deseja continuar (S/N) ?" )
#     print("Programa finalizado.....")

#Acumulador
soma = 0
for i in range(5):
    valor = int(input("Informe um valor: "))
    soma = soma + valor
print(f"A soma é: {soma}")    

