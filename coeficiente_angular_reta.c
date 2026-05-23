#include <stdio.h>

int main() {
    float x1, y1, x2, y2, m;

    printf("--- Calculadora de Coeficiente Angular ---\n\n");

    // Lendo o primeiro ponto
    printf("Digite as coordenadas do Ponto 1 (x1 y1): ");
    scanf("%f %f", &x1, &y1);

    // Lendo o segundo ponto
    printf("Digite as coordenadas do Ponto 2 (x2 y2): ");
    scanf("%f %f", &x2, &y2);

    // Verificando se a reta é vertical (x2 - x1 = 0)
    if (x1 == x2) {
        printf("\nComo x1 e x2 sao iguais, a reta eh vertical.\n");
        printf("O coeficiente angular eh indefinido (divisao por zero).\n");
    } else {
        // Calculando o coeficiente angular
        m = (y2 - y1) / (x2 - x1);
        printf("\nO coeficiente angular (m) da reta eh: %.2f\n", m);

    }

    return 0;
}