#include <iostream>

int main() {
    // Usamos 'double' para permitir tanto números inteiros quanto decimais
    double numero;
    double triplo;

    // Pede ao usuário para digitar um número
    std::cout << "Digite um numero: ";
    std::cin >> numero;

    // Calcula o triplo do número
    triplo = numero * 3;

    // Exibe o resultado final
    std::cout << "O triplo de " << numero << " e " << triplo << std::endl;

    return 0;
}