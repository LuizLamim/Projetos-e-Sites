#include <iostream>
#include <vector>

// Função para verificar se um número é primo
bool isPrime(int n) {
    // Números menores ou iguais a 1 não são primos
    if (n <= 1) return false;
    
    // Verifica divisores de 2 até a raiz quadrada de n
    // Se 'n' for divisível por qualquer número nesse intervalo, não é primo
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}