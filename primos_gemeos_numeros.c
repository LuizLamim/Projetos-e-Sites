#include <stdio.h>
#include <stdbool.h>
#include <math.h>

// Função para verificar se um número é primo
bool eh_primo(int n) {
    if (n <= 1) return false;
    if (n == 2) return true;
    if (n % 2 == 0) return false; // Elimina os pares de cara

    // Testa os divisores ímpares até a raiz quadrada de n
    int limite = (int)sqrt(n);
    for (int i = 3; i <= limite; i += 2) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

int main() {
    int limite;
    int contador = 0;

    printf("Digite o limite maximo para buscar primos gemeos: ");
    if (scanf("%d", &limite) != 1) {
        printf("Entrada invalida.\n");
        return 1;
    }

    printf("\nPares de primos gemeos ate %d:\n", limite);
    printf("-----------------------------------\n");

    // Começa do 3, já que (3, 5) é o primeiro par de primos gêmeos
    for (int i = 3; i <= limite - 2; i += 2) {
        // Se 'i' e 'i + 2' forem primos, temos um par gêmeo
        if (eh_primo(i) && eh_primo(i + 2)) {
            printf("(%d, %d)\n", i, i + 2);
            contador++;
        }
    }

    printf("-----------------------------------\n");
    printf("Total de pares encontrados: %d\n", contador);

    return 0;
}