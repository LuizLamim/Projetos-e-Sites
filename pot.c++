#include <iostream>
#include <cmath> // Biblioteca necessária para usar a função pow()

int main() {
    // Usamos 'double' para permitir números decimais e negativos
    double base, expoente, resultado;

    // Solicita a base ao usuário
    std::cout << "Digite o número base: ";
    std::cin >> base;

    // Solicita o expoente ao usuário
    std::cout << "Digite a potência (expoente): ";
    std::cin >> expoente;

    // A função pow(base, expoente) faz o cálculo matemático
    resultado = std::pow(base, expoente);

    // Exibe o resultado final na tela
    std::cout << base << " elevado a " << expoente << " é igual a " << resultado << std::endl;

return 0;
}