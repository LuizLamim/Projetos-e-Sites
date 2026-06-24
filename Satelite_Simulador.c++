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