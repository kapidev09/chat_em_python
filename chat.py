import os

mensagens = []

nome = input("seu nome: ")
os.system('cls')

while True:
 if len(mensagens) >0:
   for x in mensagens:
    print (m['nome'], "-",m['texto'])

    print("------------")

 texto = input("escreva o texto: ")
 if texto == "fim":
   break

   mensagens.append({"nome": nome,
                     "texto": texto })



