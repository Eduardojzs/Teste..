"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
try:
    horario = input('Digite seu horario atual: ')


    horario_inteiro = float(horario)


    if horario_inteiro <= 11:
        print('Bom dia!')

    elif horario_inteiro == 12 or horario_inteiro <= 17:

        print('Boa tarde!')

    elif horario_inteiro == 18 or horario_inteiro <= 23 :
        print('Boa Noite!')



except:

    print('Dgitie um número')
