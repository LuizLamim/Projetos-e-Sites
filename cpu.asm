section .data
    ; Seção de dados inicializados
    msg db 'Operacoes da CPU concluidas com sucesso!', 0xA  ; String com quebra de linha (0xA)
    len equ $ - msg                                         ; Calcula o tamanho da string

section .text
    global _start   ; Define o ponto de entrada do programa

_start:
    ; ==========================================
    ; 1. MOVIMENTAÇÃO DE DADOS (Load/Store)
    ; ==========================================
    mov rax, 15      ; Move o valor 15 para o registrador RAX
    mov rbx, 10      ; Move o valor 10 para o registrador RBX

    ; ==========================================
    ; 2. ARITMÉTICA BÁSICA (ALU - Arithmetic Logic Unit)
    ; ==========================================
    add rax, rbx     ; Soma: RAX = RAX + RBX (15 + 10 = 25)
    sub rax, 5       ; Subtração: RAX = RAX - 5 (25 - 5 = 20)
    inc rax          ; Incremento: Soma 1 a RAX (20 + 1 = 21)
    dec rbx          ; Decremento: Subtrai 1 de RBX (10 - 1 = 9)