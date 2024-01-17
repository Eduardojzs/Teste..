nome = input('Digite seu nome: ')

nome_invertido = nome[::-1]
tamanho_nome = len(nome)
primeira_letra_nome = nome[:1]
ultima_letra = nome[-1:]

print(f'Seu nome invertido é: {nome_invertido}')
print(f'Seu tome tem o tamanho Do seu nome: {tamanho_nome}')
print(f'Primeira letra do seu nome é: {primeira_letra_nome}')
print(f'ultima Letra do seu nome é: {ultima_letra}')

if " " in nome:
    print('Seu Nome Tem espaço')

else:
    print('Seu nome Não tem espaço')



if len(nome) == 0:
    print('Desculpa, Você Deixou os campos Vazios')




