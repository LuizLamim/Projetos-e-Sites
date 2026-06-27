#include <iostream>
#include <cmath> // Biblioteca necessária para a função cbrt

int main() {
    double numero, resultado;

    std::cout << "Digite um numero para calcular a raiz cubica: ";
    std::cin >> numero;

    // Calcula a raiz cúbica
    resultado = std::cbrt(numero);
}