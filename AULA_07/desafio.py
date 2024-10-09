# 1 Colocar o print exibindo o calculo, sem if! Entrada hora trabalhada e o quanto ele recebe
# 2 Fazer um while com resp, não precisa de if
# 3 pode usar vetor, colocar if para procurar entre 18 e 35, criar if quantos tem olhos verdes e cabelos loiros 


# 1- Faça um programa que pergunte quanto um funcionário recebe por hora e o número de
# horas trabalhadas no mês. Calcule e mostre o total do seu salário, sabendo que são descontados 11%
# para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# a) salário bruto.
# b) quanto pagou ao IRRF.
# c) quanto pagou ao INSS.
# d) quanto pagou ao sindicato.
# e) o salário líquido.

# salario_hora = float(input("Quanto você recebe por hora ?"))
# horas_trabalhadas = float(input("Quantas horas você trabalha por mês?"))


# salario_bruto = salario_hora * horas_trabalhadas
# IRRF = salario_bruto * 0.11
# INSS = salario_bruto * 0.08
# SINDICATO = salario_bruto * 0.05

# print(f"Seu salário bruto é de: R${salario_bruto:.2f}")
# print(f"Você pagou ao imposto de renda: R${IRRF:.2f}")
# print(f"Você pagou ao INSS: R$ {INSS:.2f}" )
# print(f"Você pagou ao sindicato: R${SINDICATO:.2f}")
# print(f"Seu salário líquido é de: R${salario_bruto - IRRF - INSS - SINDICATO:.2f}" )


# 2- O Departamento Estadual de Meteorologia solicitou o desenvolvimento de um
# programa que armazene em um vetor um conjunto indeterminado de temperaturas, ao final
# informe a menor, a maior e a média das temperaturas.

# temperatura = []
# resp = "S"

# while resp == "S":
#     temperatura.append(int(input("Informe as temperaturas")))
    
#     resp = input("Deseja inserir outra temperatura? S/N")
# print(f"A temperatura mínima é de:{min(temperatura)} ºC")  
# print(f"A temperatura máxima é de:{max(temperatura)} ºC")
# print(f"A temperatura média é de:{sum(temperatura)/len(temperatura)} ºC")     
    
# 3- Foi realizada uma pesquisa de algumas características físicas da população de uma certa região, a
# qual coletaram os seguintes dados referentes a cada habitante para serem analisados:
# - sexo (masculino e feminino)
# - cor dos olhos (azuis, verdes ou castanhos)
# - cor dos cabelos (louros, castanhos, pretos)
# - idade
# Faça um programa que determine e escreva:
# a) a maior e a menor idade dos habitantes, assim como a média das idades;
# b) a quantidade de indivíduos do sexo feminino cuja idade está entre 18 e 35 anos, inclusive;
# c) a quantidade de indivíduos que tenham olhos verdes e cabelos louros;

    
# Foi realizada uma pesquisa de algumas características físicas da população de uma certa região, a qual coletaram os seguintes dados referentes a cada habitante para serem analisados: 
# - sexo (masculino e feminino) 
# - cor dos olhos (azuis, verdes ou castanhos) 
# - cor dos cabelos (louros, castanhos, pretos) 
# - idade 
# Faça um programa que determine e escreva: 
# a) a maior e a menor idade dos habitantes, assim como a média das idades; 
# b) a quantidade de indivíduos do sexo feminino cuja idade está entre 18 e 35 anos, inclusive; 
# c) a quantidade de indivíduos que tenham olhos verdes e cabelos louros; 


sexo = []
olhos = []
cabelos = []
idade = []
resp = "S"
qtd_sexo_idade = 0
qtd_olhos_cabelos = 0

while resp.upper() == "S":
    sexo.append(input("Informe o sexo M - Masculino ou F - Feminino: ").strip().upper())
    olhos.append(input("Informe a cor dos olhos A - Azuis, V - Verdes ou C - Castanhos: ").strip().upper())
    cabelos.append(input("Informe a cor dos cabelos L - Louros, P - Pretos ou C - Castanhos: ").strip().upper())
    idade.append(int(input("Informe a idade: ")))
    resp = input("Deseja Continuar(S/N)? ").strip().upper()

for i in range(len(sexo)):
    # Contar quantas pessoas do sexo feminino têm idade entre 18 e 35 anos
    if sexo[i] == "F" and 18 <= idade[i] <= 35:
        qtd_sexo_idade += 1
    # Contar quantas pessoas têm cabelos louros e olhos verdes
    if olhos[i] == "V" and cabelos[i] == "L":
        qtd_olhos_cabelos += 1

if idade:  # Verifica se a lista de idades não está vazia
    print(f"A maior idade é {max(idade)} anos.")
    print(f"A menor idade é {min(idade)} anos.")
    print(f"A média das idades é {(sum(idade) / len(idade)):.0f} anos.")
else:
    print("Nenhuma idade registrada.")

print(f"A quantidade de pessoas do sexo feminino com idades entre 18 e 35 anos é {qtd_sexo_idade}.")
print(f"A quantidade de pessoas que possuem cabelos louros e olhos verdes é {qtd_olhos_cabelos}.")
