import os

#Criating List
restaurantes = ['Outback', 'Segunda Casa', 'Yosugiro']

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
  print ('3. Ativar restaurante')
  print ('4. Sair\n')

#Function: Finalize APP
def finalizar_app():
  exibir_subtitulo('Finalizando APP\n')

#Function: Back main menu
def voltar_menu_principal():
  input('Digite a telha ENTER para voltar ao MENU PRINCIPAL ')
  main()

#Function: 
def exibir_subtitulo(texto):
  os.system('cls')
  print(texto)

#Function: Invalid option
def opcao_invalida():
  print('Opção Inválida!\n')

  voltar_menu_principal()

#Function: Register restaurant 
def cadastrar_novo_restaurante():
  exibir_subtitulo('Cadastro de Novos Restaurantes\n')

  nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
  restaurantes.append(nome_restaurante)
  print(f'Restaurante {nome_restaurante} cadastrado com sucesso!\n')

  voltar_menu_principal()

#Function: List restaurants
def listar_restaurantes():
  exibir_subtitulo('Restaurantes Cadastrados:\n')

  for restaurante in restaurantes:
    print(f'- {restaurante}\n')

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
      print('Ativar restaurantes')
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