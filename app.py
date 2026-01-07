import os

#Criating List
restaurantes = []

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
  os.system('cls')
  print('Finalizando APP\n')

#Function: Invalid option
def opcao_invalida():
  print('Opção Inválida!\n')
  input('Digite a telha ENTER para voltar ao MENU PRINCIPAL ')
  main()

#Function: Register restaurant 
def cadastrar_novo_restaurante():
  os.system('cls')
  print('Cadastro de Novos Restaurantes\n')
  nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
  restaurantes.append(nome_restaurante)
  print(f'Restaurante {nome_restaurante} cadastrado com sucesso!\n')
  input('Digite a telha ENTER para voltar ao MENU PRINCIPAL ')
  main()

#Function: Choice option
def escolher_opcoes():
  try:
    opcao_escolhida = int(input('Escolha uma opção: '))
    if opcao_escolhida == 1:
      cadastrar_novo_restaurante()
    elif opcao_escolhida == 2:
      print('Listar restaurantes')
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