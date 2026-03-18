#include <stdio.h>
#include <math.h>

int main() {
    double numero, resultado;

    printf("--- Calculadora de Raiz Cúbica ---\n");
    printf("Digite um número: ");
    
    // Lendo a entrada do usuário
    if (scanf("%lf", &numero) != 1) {
        printf("Erro: Por favor, digite um número válido.\n");
        return 1;
    }
    
    return 0;

}