#include <iostream>
#include <string>
#include <thread> // Para simular o tempo passando
#include <chrono>

// --- SUBSISTEMA DE ENERGIA ---
class SistemaEnergia {
public:
    double nivelBateria = 100.0; // em %
    bool paineisSolaresAbertos = true;

    void atualizar() {
        if (paineisSolaresAbertos) {
            nivelBateria += 2.0; // Recarrega com o Sol
        }
        nivelBateria -= 1.0; // Consumo básico do satélite
        
        // Garante os limites de 0% a 100%
        if (nivelBateria > 100.0) nivelBateria = 100.0;
        if (nivelBateria < 0.0) nivelBateria = 0.0;
    }

    void desativarSistemasNaoEssenciais() {
        std::cout << "[ENERGIA] Alerta! Modo de economia ativado. Desligando carga útil.\n";
    }
};

// --- SUBSISTEMA DE PROPULSÃO E ÓRBITA ---
class SistemaPropulsao {
public:
    double altitude = 500.0; // Altitude em km (Órbita Baixa)

    void atualizar() {
        altitude -= 0.5; // Decaimento orbital natural devido ao arrasto atmosférico
    }

    void dispararPropulsores() {
        std::cout << "[PROPULSÃO] Disparando propulsores iônicos! Elevando altitude...\n";
        altitude += 15.0; // Eleva a órbita
    }
};

// --- COMPUTADOR DE BORDO PRINCIPAL (OBC) ---
class SateliteOBC {
private:
    SistemaEnergia energia;
    SistemaPropulsao propulsao;
    bool modoSeguranca = false;

public:
    void loopPrincipal() {
        int ciclos = 0;
        
        // Loop de execução contínua (Simulando o RTOS - Sistema Operacional de Tempo Real)
        while (ciclos < 10) { 
            std::cout << "\n--- CICLO DE TELEMETRIA #" << ciclos + 1 << " ---\n";
            
            // Atualiza o estado físico do satélite
            energia.atualizar();
            propulsao.atualizar();

            // Exibe a telemetria na tela
            std::cout << "Altitude: " << propulsao.altitude << " km\n";
            std::cout << "Bateria: " << energia.nivelBateria << " %\n";

            // FDIR (Failure Detection, Isolation, and Recovery - Algoritmo de Segurança Espacial)
            executarFDIR();

            // Simula o intervalo de tempo do relógio de bordo (1 segundo por ciclo)
            std::this_thread::sleep_for(std::chrono::seconds(1));
            ciclos++;
        }
    }

    private:
    // Rotina de segurança essencial em qualquer satélite
    void ejecutarFDIR() {
        // 1. Verificação de Altitude Crítica
        if (propulsao.altitude < 498.0) {
            std::cout << "[FDIR] Altitude abaixo do limite de segurança!\n";
            if (energia.nivelBateria > 20.0) {
                propulsao.dispararPropulsores();
                energia.nivelBateria -= 5.0; // Disparo gasta muita energia
            } else {
                std::cout << "[FDIR] ERRO CRÍTICO: Altitude baixa, mas bateria insuficiente para manobra!\n";
            }
        }

        // 2. Verificação de Energia Crítica
        if (energia.nivelBateria < 95.0 && !modoSeguranca) { // Limiar alto para o teste rodar rápido
            modoSeguranca = true;
            energia.desativarSistemasNaoEssenciais();
        } else if (energia.nivelBateria >= 98.0 && modoSeguranca) {
            modoSeguranca = false;
            std::cout << "[ENERGIA] Bateria recuperada. Retornando operações normais.\n";
        }
    }
};

// --- PONTO DE ENTRADA DO SISTEMA ---
int main() {
    std::cout << "Inicializando Computador de Bordo do Satélite...\n";
    std::cout << "Sistemas NOMINAIS.\n";
    
    SateliteOBC obc;
    obc.loopPrincipal(); // Inicia o controle do satélite
    
    std::cout << "\nSimulação encerrada.\n";
    return 0;
}