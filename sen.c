#include <stdio.h>
#include <math.h>

// Definição de constantes para o gráfico
#include <stdio.h>
#include <math.h>

#define PI 3.14159265
#define LARGURA 40  // Amplitude visual do gráfico no terminal
#define PASSOS 30   // Quantidade de pontos (linhas) a serem plotados

int main() {
    // Imprime um cabeçalho simples para o eixo Y
    printf("--- Gráfico da Função Seno ---\n");
    printf("-1.0                      0.0                      1.0\n");
    printf(" |-------------------------|-------------------------|\n");

    // Loop para o eixo X (que vai descer verticalmente no terminal)
    // Vamos plotar de 0 a 2*PI (um ciclo completo)
    for (int i = 0; i <= PASSOS; i++) {
        // Calcula o valor de x atualizado para o passo
        double x = (2 * PI / PASSOS) * i;
        
        // Calcula o seno de x (retorna um valor entre -1.0 e 1.0)
        double y = sin(x);

        // Mapeia o valor de y (-1 a 1) para o espaço de colunas do terminal (0 a 2 * LARGURA)
        // Somamos LARGURA para que o "zero" fique exatamente no centro da tela
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
        
        // Mostra o valor numérico de x e y no final da linha para referência
        printf("  (x: %.2f, y: %+1.2f)\n", x, y);
    }

    return 0;
}