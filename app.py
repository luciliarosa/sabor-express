import os

def exibir_nome_do_programa():
  print("""
  █▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
  ▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█
  """)

def exibir_opcoes():
  print ('1. Cadastrar restaurante')
  print ('2. Listar restaurante')
  print ('3. Ativar restaurante')
  print ('4. Sair\n')

def finalizar_app():
  os.system('cls')
  print('Finalizando APP\n')

def opcao_invalida():
  print('Opção Inválida!\n')
  input('Digite a telha ENTER para voltar ao MENU PRINCIPAL ')
  main()

def escolher_opcoes():
  try:
    opcao_escolhida = int(input('Escolha uma opção: '))
    if opcao_escolhida == 1:
      print('Cadastrar restaurantes')
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

def main():
  os.system('cls')
  exibir_nome_do_programa()
  exibir_opcoes()
  escolher_opcoes()

if __name__ == '__main__':
  main()