import time
import random

DISTANCIA_CRITICA_KM = 15.0

# 3 satélites monitorados
satelites = [
    {"id": "SAT-1", "altitude_nominal": 600},
    {"id": "SAT-2", "altitude_nominal": 610},
    {"id": "SAT-3", "altitude_nominal": 620},
]


def consultar_api_risco(altitude_nominal):
    # Simulação de retorno de API com valores aleatórios (70% de chance de gerar ameaça)
    if random.randint(1, 10) <= 7:
        return {
            "ameaca": f"DEBRIS-{random.randint(100, 999)}",
            "distancia_km": round(random.uniform(2.0, 50.0), 1),  # Distância entre 2.0 e 50.0 km
            "altitude_ameaca": altitude_nominal + random.randint(-5, 5),
            "tempo_espera_seg": random.randint(2, 5)  # Tempo de espera variável
        }
    return None


def painel_decisao(sat_id, risco):
    print("=" * 50)
    if not risco:
        print(f"🛰️ {sat_id} | 🟢 STATUS: SEGURO")
        print("➡️ AÇÃO: MANTENDO ÓRBITA (Sem troca)")
        return False

    dist = risco['distancia_km']
    print(f"🛰️ {sat_id} | ⚠️ AMEAÇA: {risco['ameaca']} a {dist} km")

    if dist <= DISTANCIA_CRITICA_KM:
        print("🔴 STATUS: PERIGO (Distância crítica violada)")
        print("⬆️ AÇÃO: MANOBRA EXECUTADA (Troca de órbita)")
        return True
    else:
        print("🟡 STATUS: ATENÇÃO (Fora da zona crítica)")
        print("➡️ AÇÃO: MANTENDO ÓRBITA (Sem troca)")
        return False


def executar_evasao(sat_id, altitude_atual, tempo_espera):
    altitude_segura = altitude_atual + random.randint(30, 60)  # Afastamento também dinâmico
    print(f"   [COMANDO] Elevando {sat_id} para {altitude_segura} km...")
    time.sleep(1)

    print(f"   [ESPERA] Risco passando. Aguardando {tempo_espera} segundos...")
    time.sleep(tempo_espera)

    print(f"   [COMANDO] Retornando {sat_id} para órbita original ({altitude_atual} km)...")
    time.sleep(1)
    print("   [SUCESSO] Órbita restaurada.")


def sistema_antidebris(lista_satelites):
    for sat in lista_satelites:
        risco = consultar_api_risco(sat["altitude_nominal"])
        manobrar = painel_decisao(sat["id"], risco)

        if manobrar:
            executar_evasao(sat["id"], sat["altitude_nominal"], risco["tempo_espera_seg"])


if __name__ == "__main__":
    sistema_antidebris(satelites)