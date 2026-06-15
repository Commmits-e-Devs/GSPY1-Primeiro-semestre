# FlySpace - Sistema de Gerenciamento Aeroespacial (GS - 1ESPY)
---

## 🛰️ Sobre o Projeto

A **FlySpace** é uma solução em formato de CLI (Interface de Linha de Comando) voltada para a gestão autônoma de tráfego orbital, segurança de frotas de satélites e monitoramento ambiental. O ecossistema processa telemetrias simuladas e dados reais da órbita terrestre para mitigar riscos de colisão, gerenciar o ciclo de vida de ativos espaciais e responder a eventos climáticos severos fora da atmosfera.

---

## 🚀 Funcionalidades Principais

O sistema é totalmente modularizado e conta com as seguintes ferramentas de controle:

| Módulo | Descrição Técnica | Arquivo Fonte |
| :--- | :--- | :--- |
| **Menu Centralizado** | Centraliza a navegação da aplicação com tratamento de entradas inválidas. | `Main.py` |
| **Simulação de Lançamento** | Simula órbitas divididas por altitudes e ângulos (0° a 360°), validando janelas seguras contra colisões imediatas. | `Lancamento.py` |
| **Sistema Anticolisão** | Identifica tráfego próximo e realiza manobras automáticas de desvio incremental ou de transferência orbital. | `TrocarOrbita.py` |
| **Monitoramento Climático** | Lê sensores de radiação solar e ativa o protocolo *Safe Mode* da frota se ultrapassar 85.0 MeV. | `ClimaEspacial.py` |
| **Auditoria de Sustentabilidade**| Monitora níveis críticos de combustível (< 5.0%) e direciona satélites para queima atmosférica ou Órbita Cemitério. | `Sustentabilidade.py` |
| **Mapeamento de Órbitas** | Conecta-se a um servidor externo para processar dados TLE reais e classificar satélites ativos (LEO, MEO, GEO). | `MapeamentoDaOrbita.py` |

---

## 🛠️ Arquitetura do Código

* **`Main.py`**: Ponto de entrada do programa. Gerencia o loop principal do menu e direciona o fluxo do usuário.
* **`Lancamento.py`**: Cria uma matriz espacial discreta, simula a presença de 50 objetos/detritos em órbita e testa o posicionamento seguro de novos satélites.
* **`TrocarOrbita.py`**: Implementa cálculos físicos reais (como raio orbital, velocidade e variação de energia via Delta-V) para manobras evasivas tangenciais.
* **`ClimaEspacial.py`**: Gera telemetrias randômicas de vento solar e automatiza o desligamento de cargas úteis não essenciais em caso de tempestades de radiação.
* **`Sustentabilidade.py`**: Garante as diretrizes de mitigação de lixo espacial avaliando a autonomia restante de cada dispositivo da frota.
* **`MapeamentoDaOrbita.py`**: Utiliza requisições HTTPS e bibliotecas matemáticas nativas para decodificar parâmetros de movimento médio diário obtidos via arquivo TLE.

---

## 🔧 Como Executar o Projeto

### Pré-requisitos
* Python 3.x instalado em sua máquina.
* Conexão com a internet (necessária exclusivamente para a função de Mapeamento de Órbitas ler o feed TLE).
