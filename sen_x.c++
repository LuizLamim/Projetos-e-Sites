#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

int main() {
    // Configurações do gráfico
    const int num_linhas = 40;        // Quantidade de pontos no eixo x (linhas de cima para baixo)
    const int largura_maxima = 35;    // Quantidade de caracteres para a amplitude máxima (eixo y)
    const double PI = 3.14159265358979323846;
    const double max_x = 2.0 * PI;    // Vamos plotar um ciclo completo (0 a 2*pi)

    cout << "Grafico de y = sen(x) no terminal:\n";
    cout << "Eixo X desce, Eixo Y vai para a direita.\n\n";

    for (int i = 0; i <= num_linhas; ++i) {
        // Calcula o valor atual de x e y
        double x = (static_cast<double>(i) / num_linhas) * max_x;
        double y = sin(x);

        // Mapeia o valor de y (-1 a 1) para a posição da coluna no terminal
        // Somamos 1.0 para que y vá de 0 a 2, e multiplicamos pela largura máxima
        int posicao_y = static_cast<int>(round((y + 1.0) * largura_maxima));

        // Imprime os espaços até o ponto da curva
        for (int j = 0; j <= 2 * largura_maxima; ++j) {
            if (j == posicao_y) {
                cout << "*"; // Desenha o ponto da função
            } else if (j == largura_maxima) {
                cout << "|"; // Desenha o eixo central (y = 0)
            } else {
                cout << " ";
            }
        }
        
        // Imprime o valor de x e y para referência no final da linha
        cout << "  (x: " << fixed << setprecision(2) << x 
             << ", y: " << setw(5) << y << ")\n";
    }

    return 0;
}