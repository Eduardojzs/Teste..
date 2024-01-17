"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""





try:
    numero = input('Digite um número: ')
    numero_inteiro = float(numero) 
    if numero_inteiro % 2 == 0:
        print('Número Digitado é Par')
    else:
        print('Impar')
    ...
except:

    print('Digite um número inteiro')
    ...
