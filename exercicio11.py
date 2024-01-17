"""
Exercício: Soma de Números Pares

Objetivo: Escreva um programa que peça ao usuário um número 
inteiro N e some todos os números pares de 1 até N, incluindo o próprio N (se for par). 

Utilize um loop for para esta tarefa.

Etapas:

    - Solicite ao usuário um número inteiro positivo N.
    - Utilize um loop for para iterar de 1 a N e some todos os números pares.
    - Imprima o resultado da soma.


Exemplo de Saída:

Digite um número inteiro positivo: 10
A soma dos números pares de 1 até 10 é: 30
"""
# Solicitando ao usuário o número
N = int(input("Digite um número inteiro positivo: "))

# Inicializando a variável para armazenar a soma
soma_pares = 0

# Utilizando um loop for para somar os números pares de 1 até N
for i in range(1, N + 1):
    
    # Verificando se o número é par
    if i % 2 == 0: 
        
        #Imprime cada etapa
        print(f"Número: {i} + {soma_pares} = {i+soma_pares}")
        
        soma_pares += i