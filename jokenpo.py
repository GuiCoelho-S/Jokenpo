from random import choice
from time import sleep
print('\033[1;31mBEM VINDO AO JOGO JOKENPÔ\n ')

print('\033[;1mVocê deseja jogar contra o computador?')
a = str(input())
a = a.lower()

if a == 'sim':
    print('Escolha uma das opções abaixo: ')
    print('''[1] PEDRA
[2] TESOURA
[3] PAPEL''')
    escolha = int(input('Digite a opção escolhida: '))
    print('Você jogou \033[1;36m{}'.format(escolha))
    print('\033[1;31mJO')
    sleep(1)
    print('\033[1;31mKEN')
    sleep(1)
    print('\033[1;31mPÔ')

    lista = ['pedra', 'papel', 'tesoura']
    escolhidu = choice(lista)
    escolhido = str(escolhidu)
    print('\033[1;94mcomputador escolheu \033[1;96m {}'.format(escolhido, weights=[1, 1, 1], k=11))
    if escolhido == 'pedra' and escolha == 1:
        print('\033[1;96mEmpate')
    elif escolhido == 'tesoura' and escolha == 2:
        print('\033[1;96mEmpate')
    elif escolhido == 'papel' and escolha == 3:
        print('\033[1;96mEmpate')
    elif escolhido == 'pedra' and escolha == 2:
        print('\033[1;96mO computador venceu!')
    elif escolhido == 'pedra' and escolha == 3:
        print('\033[1;96mVocê ganhou!')
    elif escolhido == 'papel' and escolha == 2:
        print('\033[1;96mO Você venceu!')
    elif escolhido == 'papel' and escolha == 1:
        print('\033[1;96mO computador venceu!')
    elif escolhido == 'tesoura' and escolha == 1:
        print('\033[1;96mVocê venceu!')
    elif escolhido == 'tesoura' and escolha == 3:
        print('\033[1;96mO computador venceu!')
elif a == 'nao' or 'não':
    print('Quando quiser jogar, estarei aqui. Tenha um bom dia')
else:
    print('Caso queira jogar, digite sim ou não. Reinicie o programa para uma nova tentativa')
