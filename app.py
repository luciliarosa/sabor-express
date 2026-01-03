import os

print("""
█▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█
""")

print ('1. Cadastrar restaurante')
print ('2. Listar restaurante')
print ('3. Ativar restaurante')
print ('4. Sair\n')

opcao_escolhida = int(input('Escolha uma opção: '))

#função
def finalizar_app():
  os.system('cls')
  print('Finalizando APP\n')

if opcao_escolhida == 1:
  print('Cadastrar restaurantes')
elif opcao_escolhida == 2:
  print('Listar restaurantes')
elif opcao_escolhida == 3:
  print('Ativar restaurantes')
else:
  finalizar_app()