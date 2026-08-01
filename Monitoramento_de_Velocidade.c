#include <stdint.h>

// 1. DEFINIÇÕES DO SISTEMA
#define VNE_LIMIT 350  // Velocidade estrutural máxima (knots)

// Mapeamento de Hardware (Memory-Mapped I/O)
// Os ponteiros apontam para os endereços físicos do hardware no barramento.
// A palavra-chave 'volatile' é obrigatória: ela avisa o compilador para 
// NUNCA otimizar essas variáveis, pois o valor pode ser alterado pelo hardware a qualquer momento.
#define SENSOR_PITOT (*(volatile uint16_t*)0x0300)
#define ALARME_PAINEL (*(volatile uint8_t*)0x0302)

int main(void) {}