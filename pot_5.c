#include <stdio.h>

int main(){
    double numero, resultado;

    // Solicita a entrada do usuário
    printf("Digite um número para calcular sua quinta potência: ");
    scanf("%lf", &numero);

    // Calcula a quinta potência multiplicando o número por ele mesmo
    resultado = numero * numero * numero * numero * numero;

    // Exibe o resultado na tela com duas casas decimais
    printf("A quinta potência de %.2lf é: %.2lf\n", numero, resultado);

}