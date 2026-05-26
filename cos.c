#include <stdio.h>
#include <math.h>

#define PI 3.14159265
#define LARGURA 40  // Amplitude visual do gráfico no terminal
#define PASSOS 30   // Quantidade de pontos (linhas) a serem plotados

int main() {
    // Imprime o cabeçalho para o eixo Y
    printf("--- Gráfico da Função Cosseno ---\n");
    printf("-1.0                      0.0                      1.0\n");
    printf(" |-------------------------|-------------------------|\n");

    // Loop para o eixo X (descendo verticalmente de 0 a 2*PI)
    for (int i = 0; i <= PASSOS; i++) {
        // Calcula o valor de x atualizado para o passo
        double x = (2 * PI / PASSOS) * i;
        
        // Calcula o cosseno de x
        double y = cos(x);

        // Mapeia o valor de y (-1 a 1) para o espaço de colunas do terminal (0 a 2 * LARGURA)
        int posicao_asterisco = (int)(y * LARGURA) + LARGURA;

        // Desenha a linha correspondente no terminal
        for (int espaco = 0; espaco <= 2 * LARGURA; espaco++) {
            if (espaco == posicao_asterisco) {
                printf("*"); // Plota o ponto da curva
            } else if (espaco == LARGURA) {
                printf("|"); // Desenha a linha do eixo central (zero)
            } else {
                printf(" "); // Espaço em branco
            }
        }
        
        // Mostra o valor numérico de x e y no final da linha
        printf("  (x: %.2f, y: %+1.2f)\n", x, y);
    }

    return 0;
}