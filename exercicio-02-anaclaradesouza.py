#EXE 002 - Peça ao usuário para inserir um número. Continue perguntando até que ele insira CINCO números, 
#em seguida, exibam a mensagem “ O último número que você digitou foi um [número] " e pare o programa.
i = 0

while i < 5:
    num = int(input("Escreva um numero: "))
    i += 1
    print("o ultimo numero que voce digitou foi: {}".format(num))
print("Programa finalizado.")
print("Ana Clara De Souza")