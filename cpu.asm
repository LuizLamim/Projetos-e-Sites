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

    ; ==========================================
    ; 3. OPERAÇÕES LÓGICAS (ALU)
    ; ==========================================
    ; XOR em um registrador com ele mesmo é a forma mais rápida e otimizada de zerá-lo.
    xor rcx, rcx     ; RCX = 0 
    
    ; Operação AND (mantém os bits que são 1 em ambos)
    and rax, 0xFF    ; Aplica uma máscara de 8 bits em RAX

    ; ==========================================
    ; 4. CHAMADA DE SISTEMA (Syscall) - Imprimir texto
    ; ==========================================
    ; O processador delega a tarefa de I/O (tela) para o Sistema Operacional
    mov rax, 1       ; Número da syscall para 'sys_write' no Linux x86_64
    mov rdi, 1       ; File descriptor 1 (stdout - saída padrão)
    mov rsi, msg     ; Ponteiro para a mensagem que criamos na seção .data
    mov rdx, len     ; Tamanho da mensagem
    syscall          ; Interrompe a CPU e pede para o Linux executar a ação

    ; ==========================================
    ; 5. ENCERRAMENTO DO PROGRAMA (Syscall - Exit)
    ; ==========================================
    mov rax, 60      ; Número da syscall para 'sys_exit'
    mov rdi, 0       ; Código de saída 0 (indica que o programa rodou sem erros)
    syscall          ; Interrompe a CPU e encerra o processo