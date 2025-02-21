#EXE 006 - Peça ao usuário para inserir um número entre 15 e 20.
#Se ele inserir um valor abaixo de 15, exiba a mensagem "Muito baixo" e peça que tentem novamente.
#Se ele inserir um valor acima de 20, exiba a mensagem "Muito alto" e peça que tentem novamente.
#Continue repetindo isso até que ele insira um valor entre 15 e 20 e, em seguida, exibam a mensagem "Obrigado".
numero = int(input("Digite um numero entre 15 e 20: "))

while numero < 15 or numero > 20:
    if numero < 15:
        numero = int(input("Muito baixo!! Digite novamente:")) 
    elif numero > 20:
        numero = int(input("Muito alto!! Digite novamente:")) 
else: 
     print("obrigado:)")
print("Programa finalizado.")
print("Ana Clara De Souza")