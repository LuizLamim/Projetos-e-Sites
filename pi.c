#include <stdio.h>
#include <stdlib.h>

#define DIGITS 105 // Calculamos um pouco mais para evitar erros de arredondamento

// Função para setar um número de precisão arbitrária com um valor inteiro pequeno
void set_val(int *arr, int val) {
    arr[0] = val;
    for (int i = 1; i < DIGITS; i++) {
        arr[i] = 0;
    }
}