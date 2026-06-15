#include <stdio.h>
#include <stdlib.h>

// Definições da imagem
#define WIDTH 1200
#define HEIGHT 900
#define MAX_ITER 1000

int main(){
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


    return 0;
}