#include <stdio.h>

int main() {
    float x1, y1, x2, y2, m;

    printf("--- Calculadora de Coeficiente Angular ---\n");
    
    // Entrada de dados
    printf("Digite a coordenada x1: ");
    scanf("%f", &x1);
    printf("Digite a coordenada y1: ");
    scanf("%f", &y1);
    printf("Digite a coordenada x2: ");
    scanf("%f", &x2);
    printf("Digite a coordenada y2: ");
    scanf("%f", &y2);

    // Cálculo e verificação
    if (x2 - x1 == 0) {
        printf("\nErro: A reta e vertical. O coeficiente angular e indefinido.\n");
    } else {
        m = (y2 - y1) / (x2 - x1);
        printf("\nO coeficiente angular (m) e: %.2f\n", m);
    }

    return 0;
}