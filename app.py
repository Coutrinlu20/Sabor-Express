
import os 

resraurantes = [{'nome':'praça', 'categoria': 'japonesa', 'ativo': False},
                {'nome': 'pizza suprema', 'categoria': 'italiana', 'ativo': True},
                {'nome':'Café', 'categoria': 'cafeteria', 'ativo': True}
]

def exibir_nome_do_programa():
    print("""
       ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
        ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
        ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
        ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
        ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
        ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░ 
    """)

def exibir_opcoes():
    print('1. cadastrar restaurante')
    print('2. listar restaurante')
    print('3. ativar resraurante')
    print('4. sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizando app')

def voltar_ao_menu_principal():
     input('\nDigite uma tecla para voltar ao menu: ')
     main()

def opcao_invalida():
    print('opção inválida\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novo restaurantes')

    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')

    categoria = input(f'Digite o nome da categoria do restauranre {nome_do_restaurante}: ')

    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
     
    resraurantes.append(dados_do_restaurante)
    print(f'o restaurante {nome_do_restaurante} foi cadastrado com sucesso!  ')
    voltar_ao_menu_principal()

def listrar_restaurantes():
    exibir_subtitulo('Listando os restaurantes')

    for restaurante in resraurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['ativo']
        print(f'- {nome_restaurante} | {categoria} | {ativo}')

    voltar_ao_menu_principal()


def escolher_opcao():
    try:
        opcao_esconhida = int(input('esconha uma opção: '))
        if opcao_esconhida == 1:
         cadastrar_novo_restaurante()
        elif opcao_esconhida == 2:
            listrar_restaurantes()
        elif opcao_esconhida == 3:
            print('ativar resraurante')
        elif opcao_esconhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()