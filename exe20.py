import random
n1 = str(input('Primeiro aluno'))
n2 = str(input('Segundo aluno'))
n3 = str(input('Terseiro aluno'))
n4 = str(input('Quarto aluno'))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A orden de apresentaçao sera ')
print(lista)