import os

restaurantes = [{'nome':'Mega pizza', 'categoria':'Italiana', 'ativo':True},
                {'nome':'Sushi Hokkai', 'categoria':'Japonesa', 'ativo':False},
                {'nome':'Dogão', 'categoria':'Fast-Food', 'ativo':False}]

def mostra_titulo():
    print("""
╭━━━╮╱╱╭╮╱╱╱╱╱╱╱╭━━━╮
┃╭━╮┃╱╱┃┃╱╱╱╱╱╱╱┃╭━━╯
┃╰━━┳━━┫╰━┳━━┳━╮┃╰━━┳╮╭┳━━┳━┳━━┳━━┳━━┳━━╮
╰━━╮┃╭╮┃╭╮┃╭╮┃╭╯┃╭━━┻╋╋┫╭╮┃╭┫┃━┫━━┫━━┫╭╮┃
┃╰━╯┃╭╮┃╰╯┃╰╯┃┃╱┃╰━━┳╋╋┫╰╯┃┃┃┃━╋━━┣━━┃╰╯┃
╰━━━┻╯╰┻━━┻━━┻╯╱╰━━━┻╯╰┫╭━┻╯╰━━┻━━┻━━┻━━╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰╯
      """)

def mostra_escolhas():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair')

def cadastra_restaurante():
    exibir_subtitulo('Cadastro de novo restaurante:')

    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar:')
    categoria = input(f'Qual a categoria que o restaurante {nome_do_restaurante} pertence:')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso\n')

    retorna_ao_menu()

def mostra_restaurantes():
    exibir_subtitulo('Lista de restaurantes:')
    
    print(f'{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    retorna_ao_menu()

def alternar_estado_restaurante():
    exibir_subtitulo('Alternar estado de restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado:')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi destivado com sucesso'
            print(mensagem)
        
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado') 


    retorna_ao_menu()

def escolhe_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # Outra forma de fazer -> opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1:
            cadastra_restaurante()
        elif opcao_escolhida == 2:
            mostra_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finaliza_programa()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def finaliza_programa():
    exibir_subtitulo('Finalizar programa')

def retorna_ao_menu():
    input('\nDigite uma tecla para voltar ao menu principal:')
    main()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def opcao_invalida():
    print('Este caracter não é permitido\n')
    retorna_ao_menu()

def main():
    os.system('cls')
    mostra_titulo()
    mostra_escolhas()
    escolhe_opcao()

if __name__ == '__main__':
    main()