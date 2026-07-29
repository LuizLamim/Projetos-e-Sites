#include <stdio.h>

// Variável global para rastrear onde colocar a vírgula
int total_impresso = 0;

// Função auxiliar para imprimir os dígitos e formatar com a vírgula
void imprimir_digito(int digito) {
    printf("%d", digito);
    total_impresso++;
    // Imprime a vírgula logo após o '3' inicial
    if (total_impresso == 1) {
        printf(".");
    }
}