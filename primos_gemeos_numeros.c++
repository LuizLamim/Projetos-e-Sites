#include <iostream>
#include <cmath>

// Função otimizada para verificar se um número é primo
bool isPrime(int n) {
    // 0 e 1 não são primos
    if (n <= 1) return false;
    // 2 e 3 são primos
    if (n <= 3) return true;
    // Elimina múltiplos de 2 e 3
    if (n % 2 == 0 || n % 3 == 0) return false;
    
    // Verifica os divisores até a raiz quadrada de n
    // Usando a regra de que todos os primos maiores que 3 são da forma 6k ± 1
    for (int i = 5; i * i <= n; i += 6) {
        if (n % i == 0 || n % (i + 2) == 0) {
            return false;
        }
    }
    return true;
}