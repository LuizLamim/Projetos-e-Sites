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

// Função para encontrar e imprimir primos gêmeos até um limite
void findTwinPrimes(int limit) {
    std::cout << "\nPares de primos gemeos ate " << limit << ":\n";
    std::cout << "-----------------------------------\n";
    
    bool found = false;
    
    // Começamos do 3, pois o par (2, 4) não é válido (4 não é primo)
    // Incrementamos de 2 em 2, pois primos maiores que 2 são ímpares
    for (int i = 3; i <= limit - 2; i += 2) {
        if (isPrime(i) && isPrime(i + 2)) {
            std::cout << "(" << i << ", " << i + 2 << ")\n";
            found = true;
        }
    }
    
    if (!found) {
        std::cout << "Nenhum par de primos gemeos encontrado nesse intervalo.\n";
    }
}

int main() {
    int limite;
    
    std::cout << "Digite o limite maximo para buscar primos gemeos: ";
    std::cin >> limite;

    // Garante que o usuário não digite um número negativo
    if (limite < 5) {
        std::cout << "O limite deve ser pelo menos 5 para encontrar o primeiro par (3, 5).\n";
    } else {
        findTwinPrimes(limite);
    }

    return 0;
}