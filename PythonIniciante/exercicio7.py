"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome_usuario = input('Digite seu nome: ')

tamanho_nome_do_usuario = len(nome_usuario)


if tamanho_nome_do_usuario <= 4:
    print('Seu nome é curto')
elif tamanho_nome_do_usuario == 5 or tamanho_nome_do_usuario == 6:
    print('Seu nome é normal')
else:
    print('Seu nome Muito grande!')