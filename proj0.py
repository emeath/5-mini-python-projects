# 08-12 18-04-2020
#
# Projeto 0 - Simulador de dado
#
# Objetivo: rodar um dado com número de lados determinado pelo usuário.
#
# Oferecer opções de dados e oferecer possibilidade de determinar outra
#  quantidade de lados

# Modulo para uso de números aleatórios
import random

def rolarDado(numeroDeLados):

  # Realiza simples validação para garantir que o argumento recebido seja um inteiro
  numeroDeLados = int(numeroDeLados)

  # Obtem e armazena valor entre 1 ate numeroDeLados
  rolarDado_valor = random.randint(1, numeroDeLados)

  return rolarDado_valor

def main():

  executando = True

  # Executar ate usuário decidir finalizar.
  while executando:

    #Exibir opções para o usuário
    print("\n\t <Opções> \t\n")
    print("1 \t - \t dado com 6 lados")
    print("2 \t - \t dado com 20 lados")
    print("3 \t - \t determinar quantidade de lados (1 a qualquer número Natural, exceto 0 -> N*)")
    print("-1 \t - \t para encerrar a aplicação")

    comando = int(input("\nComando: "))
    if comando == 1:
      valor = rolarDado(6)

    elif comando == 2:
      valor = rolarDado(20)

    elif comando == 3:
      nLados = int(input("\nPor gentileza, determine a quantidade de lados do dado: "))
      valor = rolarDado(nLados)

    # Caso o usuário deseje finalizar a aplicação
    elif comando == -1:
      print("\nA aplicação \"Simulador de dado\" será encerrada.\n")
      executando = False

    # Caso de comando desconhecido
    else:
      print("Este comando não é reconhecido nessa aplicação.")
      print("Comandos válidos são: < 1 >, < 2 >, < 3 > e < -1 >.")
      print("Aplicação será encerrada.")
      executando = False

    print("\nO dado foi rolado e a face virada para cima foi...")
    print("valor: %d" % valor)

# Invoca a função principal
main()