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

// Calcula a série de Taylor para arctan(1/k) multiplicada por um fator
void arctan_series(int *res, int k, int factor) {
    int *term = (int *)malloc(DIGITS * sizeof(int));
    int *current_term = (int *)malloc(DIGITS * sizeof(int));
    
    // Primeiro termo: factor * (1/k)
    set_val(term, factor);
    div_arr(term, k);
    
    // Adiciona o primeiro termo ao resultado
    add_arr(res, term);
    
    int n = 3;
    int sign = -1;
    
    while (1) {
        // Próxima potência: divide o termo anterior por k^2
        div_arr(term, k);
        div_arr(term, k);
        
        if (is_zero(term)) break;
        
        // Copia o termo atual para dividir pelo divisor da série (3, 5, 7...)
        for (int i = 0; i < DIGITS; i++) current_term[i] = term[i];
        div_arr(current_term, n);
        
        if (sign == 1) {
            add_arr(res, current_term);
        } else {
            sub_arr(res, current_term);
        }
        
        sign = -sign;
        n += 2;
    }
    
    free(term);
    free(current_term);
}

int main() {
    int *pi = (int *)malloc(DIGITS * sizeof(int));
    int *term239 = (int *)malloc(DIGITS * sizeof(int));
    
    for (int i = 0; i < DIGITS; i++) {
        pi[i] = 0;
        term239[i] = 0;
    }
    
    // Pi = 4 * [ 4 * arctan(1/5) - arctan(1/239) ]
    // Que é o mesmo que: 16 * arctan(1/5) - 4 * arctan(1/239)
    
    arctan_series(pi, 5, 16);
    arctan_series(term239, 239, 4);
    
    sub_arr(pi, term239);
    
    // Imprime o resultado formatado
    printf("PI com 100 casas decimais:\n");
    printf("%d.", pi[0]);
    for (int i = 1; i <= 100; i++) {
        printf("%d", pi[i]);
        if (i % 10 == 0 && i < 100) printf(" "); // Espaço a cada 10 dígitos para facilitar a leitura
    }
    printf("\n");
    
    free(pi);
    free(term239);
    return 0;
}