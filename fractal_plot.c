#include <stdio.h>
#include <stdlib.h>

// Definições da imagem
#define WIDTH 1200
#define HEIGHT 900
#define MAX_ITER 1000

int main() {
    // Abre o arquivo para salvar a imagem
    FILE *fp = fopen("mandelbrot.ppm", "wb");
    if (fp == NULL) {
        printf("Erro ao criar o arquivo de imagem!\n");
        return 1;
    }

    // Cabeçalho do formato PPM (P6 significa binário colorido)
    fprintf(fp, "P6\n%d %d\n255\n", WIDTH, HEIGHT);

    // Limites do plano complexo para focar no fractal
    double min_re = -2.0, max_re = 1.0;
    double min_im = -1.2, max_im = 1.2;

    // Fatores de escala
    double re_factor = (max_re - min_re) / (WIDTH - 1);
    double im_factor = (max_im - min_im) / (HEIGHT - 1);

    printf("Gerando o fractal... Por favor, aguarde.\n");

    // Varre cada pixel da imagem
    for (int y = 0; y < HEIGHT; y++) {
        double c_im = max_im - y * im_factor; // Componente imaginária

        for (int x = 0; x < WIDTH; x++) {
            double c_re = min_re + x * re_factor; // Componente real

            // Z = Z^2 + C (Começando com Z = 0)
            double z_re = 0.0, z_im = 0.0;
            int iter = 0;
            
            // Variáveis para otimizar o cálculo (evita multiplicações repetidas)
            double z_re2 = 0.0, z_im2 = 0.0;

            // Laço principal de Mandelbrot
            while (z_re2 + z_im2 <= 4.0 && iter < MAX_ITER) {
                z_im = 2.0 * z_re * z_im + c_im;
                z_re = z_re2 - z_im2 + c_re;
                
                z_re2 = z_re * z_re;
                z_im2 = z_im * z_im;
                iter++;
            }

            // Colorização baseada no número de iterações
            unsigned char color[3];

            if (iter == MAX_ITER) {
                // Interior do conjunto (Preto)
                color[0] = 0;
                color[1] = 0;
                color[2] = 0;
            } else {
                // Gradiente de cores psicodélico para as bordas
                color[0] = (iter * 7) % 255;  // Vermelho
                color[1] = (iter * 13) % 255; // Verde
                color[2] = (iter * 23) % 255; // Azul
            }

            // Escreve os 3 bytes (RGB) do pixel no arquivo
            fwrite(color, 1, 3, fp);
        }
    }

    fclose(fp);
    printf("Pronto! O arquivo 'mandelbrot.ppm' foi gerado com sucesso.\n");

    return 0;
}