#include <stdio.h>
#include <math.h>

int main() {

    double base, expoente, resultado;

    printf("--- Calculadora de Potencia ---\n");

    // Solicita os dados ao usuário
    printf("Digite o valor de X (base): ");
    scanf("%lf", &base);

    printf("Digite o valor de Y (expoente): ");
    scanf("%lf", &expoente);

    // Calcula X elevado a Y
    resultado = pow(base, expoente);

    // Exibe o resultado com 2 casas decimais
    printf("%.2f elevado a %.2f e igual a: %.2f\n", base, expoente, resultado);
    printf("-------------------------------\n");

    return 0;
}