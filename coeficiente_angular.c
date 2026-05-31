#include <stdio.h>

int main() {
    float x1, y1, x2, y2;
    float m;

    printf("--- Calculadora de Coeficiente Angular ---\n\n");

    // Entrada de dados do primeiro ponto
    printf("Digite as coordenadas do ponto A (x1 y1): ");
    scanf("%f %f", &x1, &y1);

    // Entrada de dados do segundo ponto
    printf("Digite as coordenadas do ponto B (x2 y2): ");
    scanf("%f %f", &x2, &y2);

    // Validação para evitar divisão por zero (reta vertical)
    if (x2 == x1) {
        printf("\nErro: x1 nao pode ser igual a x2.\n");
        printf("A reta e vertical e o coeficiente angular e indefinido.\n");
    } else {
        // Cálculo do coeficiente angular
        m = (y2 - y1) / (x2 - x1);
        
        printf("\n-----------------------------------------\n");
        printf("O coeficiente angular (m) da reta e: %.2f\n", m);
        printf("-----------------------------------------\n");
    }

    return 0;
}