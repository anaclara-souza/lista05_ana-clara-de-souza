#EXE 007 . Escreva um programa que permaneça em laço lendo números inteiros. 
#O laço termina quando for digitado 0 (zero).
#Cada valor diferente de zero digitado deve ser colocado em uma lista, desde que ele ainda não esteja lá, ou seja, valores repetidos não são aceitos. 
#Se um valor repetido for digitado, o programa deve exibir uma mensagem na tela. 
#ao final exiba a lista e a quantidade de elementos que ela contém.

nums = []

num = int(input("digite um numero inteiro ou 0 para sair: "))

while num != 0:
    if num in nums:
        print("Numero repetido!! ")
    else:
        nums.append(num)
    num = int(input("digite um numero inteiro ou 0 para sair: "))

print("\nLIsta final:",nums)
print("Quantidades de elementos: ",
len(nums))    
print("Programa finalizado.")
print("Ana Clara De Souza")