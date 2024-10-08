
#Maior média x menor média x media da turma x variação de menor para maior x mostre as medias em ordem crescente
# nomes = []
# medias = []
# resp = "S"

# while resp.lower() == "s":
    
#         nomes.append(input("Informe o nome do estudante: "))
#         medias.append(float(input("Informe a média do estudante: ")))
#         resp = input("Deseja continuar(S/N) ?")
# for i in range(len(medias)):
#     print(i,"-",nomes[i],"-",medias[i])
#     maior_media = max(medias)
#     pos = medias.index(maior_media)
#     print(f"{nomes[pos]}, você possui a maior média.")
#     print(f"A média da turma é: {(sum(medias)/len(medias)):.1f}")     
#     print(f"A maior média da turma é: {max(medias)}")
#     print(f"A menor média da turma é: {min(medias)}")  
#     print(f"A amplitude da média da turma é: {max(medias)-min(medias)}")

#     medias.sort(reverse = True)
#     print(medias)


#Pedir para os usuário informar o nome e senha se existir der o ok, caso contrário, não.
    
usuarios = ["Ingrid", "Marcos" , "Carlos", "Vanessa"]
senhas = ["123", "a1b2c3", "indyindy","formiga"] 

login = input(("Insira o seu nome de usuário"))
password = input(("Insira a sua senha"))

for i in range(len(usuarios)):
  if usuarios[i] == login:
    resp = "verificação concluída"
    break

  elif senhas[i] == password:
     resp = "Verificação concluída"
   
else:
    resp = "Usuário não encontrado" 

print(resp)
