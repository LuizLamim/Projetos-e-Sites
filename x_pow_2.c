#include <stdio.h>

int main(){
    int x, y;

    printf("Grafico de y = x^2 no Terminal\n\n");
    
    // O eixo Y vai de 25 ate 0 (para cobrir x de -5 a 5)
    for (y = 25; y >= 0; y--) {
        printf("%2d |", y); // Imprime o eixo Y numérico
        
        // O eixo X vai de -5 ate 5
        for (x = -5; x <= 5; x++) {
            // Se a coordenada atual bater com a função, desenha o ponto
            if (y == x * x) {
                printf(" * ");
            } else {
                printf("   ");
            }
        }
        printf("\n");
    }
    
    // Desenha a linha inferior do eixo X
    printf("    ");
    for (x = -5; x <= 5; x++) {
        printf("---");
    }
    printf("\n    ");
    
    // Imprime os números do eixo X
    for (x = -5; x <= 5; x++) {
        if (x < 0) {
            printf("%2d ", x);
        } else {
            printf(" %d ", x);
        }
    }
    printf("\n");

return 0;
}