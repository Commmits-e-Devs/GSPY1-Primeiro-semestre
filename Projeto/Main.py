import time

# Importando os arquivos do seu projeto
import MapeamentoDaOrbita
import Lancamento
import TrocarOrbita
import MonitoramentoDoClima
import DesorbitagemSustentavel

def exibir_menu():
    """Função responsável por desenhar a interface do menu no terminal."""
    print("\n" + "=" * 55)
    print("SISTEMA DE GERENCIAMENTO AEROESPACIAL (GS - 1ESPY)")
    print("=" * 55)
    print("  [ 1 ] - Descrição da Solução Proposta")
    print("  [ 2 ] - Simular Lançamento de Satélite")
    print("  [ 3 ] - Sistema Anticolisão (Trocar Órbita)")
    print("  [ 4 ] - Monitoramento de Clima Espacial (Safe Mode)")
    print("  [ 5 ] - Auditoria de Sustentabilidade (Lixo Espacial)")
    print("  [ 6 ] - Mapeamento das Órbitas (Relatório TLE)")
    print("  [ 0 ] - Sair do Sistema")
    print("-" * 55)


def main():
    """Função principal que gerencia o loop do programa e valida os dados."""

    while True:
        exibir_menu()

        # Recebendo a entrada do usuário e removendo espaços em branco extras
        opcao = input("Escolha uma opção válida (0 a 6): ").strip()

        # VALIDAÇÃO DE DADOS: Verifica qual opção foi escolhida
        if opcao == '1':
            print("\n>> Iniciando Descrição da Solução Proposta...")
            time.sleep(1)
            print("\n>> DESCRIÇÃO: Sistema de monitoramento e gestão de tráfego orbital da Flyspace...")

        elif opcao == '2':
            print("\n>> Iniciando Módulo de Lançamento...")
            time.sleep(1)
            Lancamento.lancamento()

        elif opcao == '3':
            print("\n>> Iniciando Módulo de Troca de Órbita...")
            time.sleep(1)
            TrocarOrbita.executar_sistema_geral_anticolisao(TrocarOrbita.lista_de_satelites_proprios)

        elif opcao == '4':
            print("\n>> Iniciando Módulo de Clima Espacial...")
            time.sleep(1)
            MonitoramentoDoClima.gerenciar_clima_espacial_frota(MonitoramentoDoClima.lista_de_satelites_proprios)

        elif opcao == '5':
            print("\n>> Iniciando Módulo de Sustentabilidade...")
            time.sleep(1)
            DesorbitagemSustentavel.executar_auditoria_ambiental_espacial(DesorbitagemSustentavel.lista_de_satelites_proprios)

        elif opcao == '6':
            print("\n>> Iniciando Mapeamento da Órbita...")
            time.sleep(1)  # Pausa dramática rápida para efeito visual no terminal
            MapeamentoDaOrbita.mapeamentoDaOrbita()

        elif opcao == '0':
            print("\n>> Encerrando o sistema da Flyspace. Até logo!\n")
            break  # Sai do loop "while" e finaliza o programa

        else:
            # Caso o usuário digite "A", "7", "teste", etc.
            print("\nERRO: Entrada inválida! Por favor, digite apenas números entre 0 e 6.")
            time.sleep(1.5)


# Ponto de partida do programa
if __name__ == "__main__":
    main()