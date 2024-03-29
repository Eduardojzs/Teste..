"""
Exercício: Multiplicação de Números

Objetivo: Escreva um programa que utilize um loop for para multiplicar os 
números de 1 a 5 e imprima o resultado de cada etapa e o resultado final.

Etapas:

    - Utilize um loop for para iterar pelos números de 1 a 5.
    - Multiplique cada número pelo resultado anterior (começando por 1).
    - Imprima o resultado de cada etapa.
    - Imprima o resultado final da multiplicação de todos os números.

Saída:

Multiplicando por 1, o resultado parcial é 1
Multiplicando por 2, o resultado parcial é 2
Multiplicando por 3, o resultado parcial é 6
Multiplicando por 4, o resultado parcial é 24
Multiplicando por 5, o resultado parcial é 120
"""

mutiplicado = 1

for numero in range (1, 6):

    mutiplicado *= numero
    print(f"MULTIPLICADO POR {numero}, o Resuçltado parcial é {mutiplicado}")
