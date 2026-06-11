#include <iostream>

int main() {
    double x1, y1, x2, y2;

    std::cout << "--- Calculadora de Coeficiente Angular ---" << std::endl;
    std::cout << "Digite as coordenadas do ponto A (x1 y1): ";
    std::cin >> x1 >> y1;
    std::cout << "Digite as coordenadas do ponto B (x2 y2): ";
    std::cin >> x2 >> y2;

    // Verifica se a reta é vertical (x1 == x2)
    if (x1 == x2) {
        std::cout << "\nO coeficiente angular e indefinido (reta vertical)." << std::endl;
    } else {
        double m = (y2 - y1) / (x2 - x1);
        std::cout << "\nO coeficiente angular (m) da reta e: " << m << std::endl;
    }


    return 0;
}