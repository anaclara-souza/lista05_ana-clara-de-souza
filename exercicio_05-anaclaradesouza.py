#EXE 005 - Crie uma variável chamada “adivinha” e defina o valor como 50. 
#Peça ao usuário para inserir um número. Embora o palpite não seja o mesmo que o valor do “adivinha”, diga a ele se o palpite é muito baixo ou muito alto e peça que ele dê outro palpite. 
#Se ele inserir o mesmo valor que “adivinha”, exiba a mensagem "Parabéns! Você acertou o número em {} tentativas!".
adivinha = 50
tentativa = 0

while(palpite := int(input("tente adivinhar o numero: "))) != adivinha :
    print("Muito alto!! " if palpite > adivinha else "muito baixo!!")

    tentativa += 1
print("Parabéns! Você acertou o número em {} tentativas!".format(tentativa))
print("Programa finalizado.")
print("Ana Clara De Souza")