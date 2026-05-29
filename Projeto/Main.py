from urllib import response

import MapeamentoDaOrbita

# NomeDoArquivo.nomeDaFuncao()
#MapeamentoDaOrbita.mapeamentoDaOrbita()
import time
from MapeamentoDaOrbita import mapeamentoDaOrbita

# Importando os outros arquivos do seu projeto
# Nota: Assumi que você tem funções dentro deles. Se não tiver, explico abaixo como ajustar.
import Lancamento
import TrocarOrbita
def exibir_menu():
    """Função responsável por desenhar a interface do menu no terminal."""
    print("\n" + "=" * 55)
    print(" 🛰️  SISTEMA DE GERENCIAMENTO AEROESPACIAL (GS - 1ESPY)  🛰️ ")
    print("=" * 55)
    print("  [ 1 ] - Mapeamento das Órbitas (Relatório TLE)")
    print("  [ 2 ] - Simular Lançamento de Satélite")
    print("  [ 3 ] - Trocar Órbita de um Satélite")
    print("  [ 0 ] - Sair do Sistema")
    print("-" * 55)


def main():
    """Função principal que gerencia o loop do programa e valida os dados."""

    while True:
        exibir_menu()

        # Recebendo a entrada do usuário e removendo espaços em branco extras
        opcao = input("Escolha uma opção válida (0 a 3): ").strip()

        # VALIDAÇÃO DE DADOS: Verifica qual opção foi escolhida
        if opcao == '1':
            print("\n>> Iniciando Mapeamento da Órbita...")
            time.sleep(1)  # Pausa dramática rápida para efeito visual no terminal
            MapeamentoDaOrbita.mapeamentoDaOrbita()

        elif opcao == '2':
            print("\n>> Iniciando Módulo de Lançamento...")
            time.sleep(1)
            # AQUI VOCÊ CHAMA A FUNÇÃO DO SEU ARQUIVO Lancamento.py
            Lancamento.lancamento()
            print("[Aviso: Substitua esta linha pela chamada da função real de Lançamento]")

        elif opcao == '3':
            print("\n>> Iniciando Módulo de Troca de Órbita...")
            time.sleep(1)
            # AQUI VOCÊ CHAMA A FUNÇÃO DO SEU ARQUIVO TrocarOrbita.py
            TrocarOrbita.executar_sistema_geral_anticolisao(TrocarOrbita.lista_de_satelites_proprios)
            print("[Aviso: Substitua esta linha pela chamada da função real de Trocar Órbita]")

        elif opcao == '0':
            print("\n>> Encerrando o sistema. Até logo!\n")
            break  # Sai do loop "while" e finaliza o programa

        else:
            # Caso o usuário digite "A", "5", "teste", etc.
            print("\n❌ ERRO: Entrada inválida! Por favor, digite apenas números entre 0 e 3.")
            time.sleep(1.5)


# Ponto de partida do programa
if __name__ == "__main__":
    main()