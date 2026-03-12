#include <stdio.h>

int main() {

    double raio, circunferencia;
    
    // Definição da constante Pi
    const double PI = 3.14159265359;

    printf("Digite o valor do raio da circunferencia: ");
    scanf("%lf", &raio);

    ircunferencia = 2 * PI * raio;

    // Exibe o resultado formatado com duas casas decimais
    printf("O valor da circunferencia e: %.2lf\n", circunferencia);

    return 0;
}