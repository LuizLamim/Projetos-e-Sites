#include <stdint.h>

// 1. DEFINIÇÕES DO SISTEMA
#define VNE_LIMIT 350  // Velocidade estrutural máxima (knots)

// Mapeamento de Hardware (Memory-Mapped I/O)
// Os ponteiros apontam para os endereços físicos do hardware no barramento.
// A palavra-chave 'volatile' é obrigatória: ela avisa o compilador para 
// NUNCA otimizar essas variáveis, pois o valor pode ser alterado pelo hardware a qualquer momento.
#define SENSOR_PITOT (*(volatile uint16_t*)0x0300)
#define ALARME_PAINEL (*(volatile uint8_t*)0x0302)

int main(void) {
    
    // Inicialização do sistema ocorreria aqui (boot, testes de hardware)

    // Loop infinito do sistema de controle de voo
    while (1) {
        
        // 2. AQUISIÇÃO DE DADOS
        // Lê o valor diretamente do hardware do tubo de Pitot
        uint16_t velocidade_atual = SENSOR_PITOT;

        // 3. LÓGICA DE CONTROLE E ATUAÇÃO
        if (velocidade_atual >= VNE_LIMIT) {
            // Condição crítica: Ativa o alarme
            ALARME_PAINEL = 1; 
        } else {
            // Condição segura: Garante que o alarme esteja desligado
            ALARME_PAINEL = 0; 
        }

        // 4. SINCRONIZAÇÃO
        // Em um sistema real (bare-metal), o loop aguardaria um timer do hardware.
        // Se estivesse usando um RTOS (Real-Time Operating System), haveria algo como:
        // vTaskDelay(pdMS_TO_TICKS(20)); // Roda a 50Hz
    }

    return 0;
}