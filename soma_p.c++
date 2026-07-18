#include <iostream>

int main() {
    // Declaração das variáveis para armazenar os números
    double num1, num2, soma;

    // Solicita o primeiro número ao usuário
    std::cout << "Digite o primeiro número: ";
    std::cin >> num1;

    // Solicita o segundo número ao usuário
    std::cout << "Digite o segundo número: ";
    std::cin >> num2;

    // Realiza a soma
    soma = num1 + num2;

    // Exibe o resultado na tela
    std::cout << "A soma de " << num1 << " com " << num2 << " é: " << soma << std::endl;

    return 0;
}