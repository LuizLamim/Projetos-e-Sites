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

}