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
    
    // Calculando a raiz cúbica
    resultado = cbrt(numero);

    // Exibindo o resultado com 2 casas decimais
    printf("A raiz cúbica de %.2f é: %.2f\n", numero, resultado);
    
    return 0;

}