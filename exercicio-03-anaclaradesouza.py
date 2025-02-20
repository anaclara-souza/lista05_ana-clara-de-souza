#EXE 003 - Peça ao usuário para inserir um número e, em seguida, insira outro número. Some esses dois números e pergunte se ele quer adicionar outro número.
#Se ele digitar “ s ", diga para inserir outro número e continuar adicionando números e somando até que ele não respondam “ s ".
#Depois que o loop for interrompido, exiba o total.
soma = int(input("Escreva um numero: "))
resposta = "S"
while resposta == "S":
    soma += int(input("Escreva outro numero: "))
    print('sua soma é', soma)
    resposta = input("Deseja adicionar outro numero ? (S/N)").upper()
print("Programa finalizado.")
print("Ana Clara De Souza")