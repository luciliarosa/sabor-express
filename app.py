import os

#Criating List
restaurantes = [
  {'nome':'Outback', 'categoria':'Comida Australiana', 'ativo': True}, 
  {'nome':'Segunda Casa','categoria':'Lanches', 'ativo': True}, 
  {'nome':'Yosugiro','categoria':'Comida Japonesa', 'ativo': False}
]

#Function: Show APP name
def exibir_nome_do_programa():
  print("""
  █▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
  ▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█
  """)

#Function: Show options
def exibir_opcoes():
  print ('1. Cadastrar restaurante')
  print ('2. Listar restaurante')
  print ('3. Status restaurante')
  print ('4. Sair\n')

#Function: Finalize APP
def finalizar_app():
  exibir_subtitulo('Finalizando APP\n')

#Function: Back main menu
def voltar_menu_principal():
  input('\nDigite a telha ENTER para voltar ao MENU PRINCIPAL ')
  main()

#Function: 
def exibir_subtitulo(texto):
  os.system('cls')
  linha = '*' * (len(texto))
  print(linha)
  print(texto)
  print(linha)
  print()

#Function: Invalid option
def opcao_invalida():
  print('Opção Inválida!\n')

  voltar_menu_principal()

#Function: Register restaurant 
def cadastrar_novo_restaurante():
  exibir_subtitulo('Cadastro de Novos Restaurantes')

  nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
  categoria = input(f'Digite o nome da categoria do restaurante {nome_restaurante}: ')

  dados_restaurante = {'nome': nome_restaurante, 'categoria': categoria, 'ativo': False}

  restaurantes.append(dados_restaurante)

  print(f'Restaurante {nome_restaurante} cadastrado com sucesso!\n')

  voltar_menu_principal()

#Function: List restaurants
def listar_restaurantes():
  exibir_subtitulo('Restaurantes Cadastrados:')

  print(f'{'Nome do Restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'}')
  for restaurante in restaurantes:
    nome_restaurante = restaurante['nome']
    categoria = restaurante['categoria']
    ativo = 'ativado'if restaurante['ativo'] else 'desativado'
    print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

  voltar_menu_principal()

#Function: Status restaurant
def status_restaurante():
  exibir_subtitulo('Alterar Status do Restaurante:')
  nome_restaurante = input('Digite o nome do restaurate que deseja mudar o status: ')
  restaurante_encontrado = False

  for restaurante in restaurantes:
    if nome_restaurante == restaurante['nome']:
      restaurante_encontrado = True
      restaurante['ativo'] = not restaurante['ativo'] 
      mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
      print(mensagem)
  if not restaurante_encontrado:
    print('Restaurante não encontrado!')

  voltar_menu_principal()

#Function: Choice option
def escolher_opcoes():
  try:
    opcao_escolhida = int(input('Escolha uma opção: '))
    if opcao_escolhida == 1:
      cadastrar_novo_restaurante()
    elif opcao_escolhida == 2:
      listar_restaurantes()
    elif opcao_escolhida == 3:
      status_restaurante()
    elif opcao_escolhida == 4:
      finalizar_app()
    else:
      opcao_invalida()
  except:
    opcao_invalida()

#Function: Main
def main():
  os.system('cls')
  exibir_nome_do_programa()
  exibir_opcoes()
  escolher_opcoes()

if __name__ == '__main__':
  main()