import random
welcome = ' Gerador de apostas da mega sena '
print('{:#^70}'.format(welcome))
bemvindo = ' bem vindo (a) '
print('{:#^70}'.format(bemvindo))
byinvisible=' by invisible '
print('{:#^70}'.format(byinvisible))
nome = str(input('Digite seu nome: '))
n1 = random.randint(1, 60)
n2 = random.randint(1, 60)
n3 = random.randint(1, 60)
n4 = random.randint(1, 60)
n5 = random.randint(1, 60)
n6 = random.randint(1, 60)
print('\n')
print('Ola {}. Sua aposta com 6 numeros gerados foi: {} - {} - {} - {} - {} - {}\nBoa sorte.'.format(nome,n1,n2,n3,n4,n5,n6,))
