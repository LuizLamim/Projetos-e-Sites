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

// Função para dividir um número de precisão arbitrária por um inteiro comum
void div_arr(int *arr, int divisor) {
    int carry = 0;
    for (int i = 0; i < DIGITS; i++) {
        long current = arr[i] + (long)carry * 10;
        arr[i] = current / divisor;
        carry = current % divisor;
    }
}

// Função para somar dois números de precisão arbitrária (res = res + src)
void add_arr(int *res, int *src) {
    int carry = 0;
    for (int i = DIGITS - 1; i >= 0; i--) {
        int sum = res[i] + src[i] + carry;
        res[i] = sum % 10;
        carry = sum / 10;
    }
}

// Função para subtrair dois números de precisão arbitrária (res = res - src)
void sub_arr(int *res, int *src) {
    int borrow = 0;
    for (int i = DIGITS - 1; i >= 0; i--) {
        int diff = res[i] - src[i] - borrow;
        if (diff < 0) {
            diff += 10;
            borrow = 1;
        } else {
            borrow = 0;
        }
        res[i] = diff;
    }
}

// Verifica se o array é todo zero (para parar a série)
int is_zero(int *arr) {
    for (int i = 0; i < DIGITS; i++) {
        if (arr[i] != 0) return 0;
    }
    return 1;
}