#include <stdio.h>

// Variável global para rastrear onde colocar a vírgula
int total_impresso = 0;

// Função auxiliar para imprimir os dígitos e formatar com a vírgula
void imprimir_digito(int digito) {
    printf("%d", digito);
    total_impresso++;
    // Imprime a vírgula logo após o '3' inicial
    if (total_impresso == 1) {
        printf(".");
    }
}

int main() {
    // Queremos 1 dígito inteiro (o 3) e exatas 153 casas decimais
    int n = 154; 
    
    // O algoritmo de Rabinowitz-Wagon requer um array de tamanho ~ (10 * n) / 3
    int tamanho = (n * 10) / 3 + 1;
    int a[tamanho];
    
    int nines = 0;
    int predigit = 0;

    // Passo 1: Inicializa o array com 2
    for (int i = 0; i < tamanho; i++) {
        a[i] = 2;
    }

    // Passo 2: Calcula cada dígito sequencialmente
    for (int j = 1; j <= n; j++) {
        int q = 0;
        
        for (int i = tamanho; i > 0; i--) {
            int x = 10 * a[i - 1] + q * i;
            a[i - 1] = x % (2 * i - 1);
            q = x / (2 * i - 1);
        }

        a[0] = q % 10;
        q = q / 10;

        // Trata os casos onde o dígito calculado pode gerar "vai um" (carry)
        if (q == 9) {
            nines++;
        } else if (q == 10) {
            if (j > 1) {
                imprimir_digito(predigit + 1);
            }
            for (int k = 0; k < nines; k++) {
                imprimir_digito(0);
            }
            predigit = 0;
            nines = 0;
        } else {
            if (j > 1) {
                imprimir_digito(predigit);
            }
            for (int k = 0; k < nines; k++) {
                imprimir_digito(9);
            }
            predigit = q;
            nines = 0;
        }
    }
    
    // Imprime o último dígito restante no buffer
    imprimir_digito(predigit);
    printf("\n");
    
    return 0;
}