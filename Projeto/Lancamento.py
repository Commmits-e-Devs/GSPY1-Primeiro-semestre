import random

# Variáveis globais de configuração (usamos maiúsculas para indicar que são constantes)
NUM_ALTITUDES = 3
NUM_GRAUS = 360
MARGEM_SEGURANCA = 2

def lancamento():
    def criar_matriz_espacial():
        """Cria e retorna a matriz vazia (preenchida com 0s)."""
        return [[0 for _ in range(NUM_GRAUS)] for _ in range(NUM_ALTITUDES)]


    def verificar_espaco(espaco, altitude, angulo_desejado):
        """Verifica se o espaço e os arredores estão livres na matriz recebida."""
        for i in range(-MARGEM_SEGURANCA, MARGEM_SEGURANCA + 1):
            angulo_verificar = (angulo_desejado + i) % 360
            if espaco[altitude][angulo_verificar] == 1:
                return False, angulo_verificar  # Retorna Falso e onde bateu
        return True, None  # Retorna Verdadeiro e nenhum conflito

    def gerar_lixo_espacial(espaco, quantidade):# podendo ser tanto lixo quanto outros satelites
        """Espalha objetos aleatórios pela matriz."""
        print(f"\n--- Espalhando {quantidade} objetos aleatórios pelas órbitas ---")
        sucessos = 0
        tentativas = 0
        limite_tentativas = quantidade * 10

        while sucessos < quantidade and tentativas < limite_tentativas:
            alt_aleatoria = random.randint(0, NUM_ALTITUDES - 1)
            ang_aleatorio = random.randint(0, NUM_GRAUS - 1)

            # Passamos a matriz 'espaco' para a função de verificação
            livre, _ = verificar_espaco(espaco, alt_aleatoria, ang_aleatorio)

            if livre:
                espaco[alt_aleatoria][ang_aleatorio] = 1
                sucessos += 1

            tentativas += 1

        print(f"Finalizado! {sucessos} objetos foram posicionados com segurança.\n")


    def lancar_satelite(espaco, nome, altitude, angulo):
        """Tenta alocar um novo satélite na matriz."""
        if altitude >= len(espaco):
            print("Erro: Altitude fora de alcance.")
            return

        # Verifica o espaço antes de lançar
        livre, angulo_conflito = verificar_espaco(espaco, altitude, angulo)

        if livre:
            espaco[altitude][angulo] = 1
            print(f"✅ SUCESSO: Satélite '{nome}' posicionado na altitude {altitude}, ângulo {angulo}°.")
        else:
            print(f"❌ ALERTA DE COLISÃO! Lançamento do '{nome}' abortado.")
            print(f"   Motivo: Objeto detectado na zona de segurança (ângulo {angulo_conflito}°).")


    # ==========================================
    #        FLUXO PRINCIPAL DO PROGRAMA
    # ==========================================

    # 1. Criamos a matriz que representa o universo da simulação
    minha_orbita = criar_matriz_espacial()

    # 2. Populamos essa matriz específica com 50 objetos de lixo espacial
    gerar_lixo_espacial(minha_orbita, 50) # mudando esse numero ele vai ficar com mais espaço na hora de enviar e vai fazer a entrada mais facil

    # 3. Tentamos lançar nosso satélite nessa mesma matriz
    lancar_satelite(minha_orbita, "Satélite FIAP", altitude=1, angulo=90)
    lancar_satelite(minha_orbita, "Satélite DEVS", altitude=2, angulo=270)