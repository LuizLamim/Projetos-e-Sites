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


    return 0;
}