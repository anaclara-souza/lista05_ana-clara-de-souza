#EXE 004 - Faça um programa que peça o nome do convidado que o usuario deseja convidar para uma festa. Depois disso, exiba a mensagem "[nome] foi adicionado(a) com sucesso no convite!" e adicione 1 à contagem.
#Em seguida, pergunte se ele quer convidar outra pessoa.
#Continue repetindo isso até que ele não queira mais convidar ninguém para a festa e, em seguida, mostre quantas pessoas foram convidas para a festa.

cont = 0
resposta ="S"

while resposta == "S":
    print(input("Digite o nome do convidado: "), "fOI ADICIONADO COM SUSESSO AO CONVITE!!")
    cont += 1
    resposta = input("Deseja adicionar outra pessoa?  (S/N)").upper()
    print("o total de convidados é",cont)
print("Programa finalizado.")
print("Ana Clara De Souza")