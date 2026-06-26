org 100h          ; Padrão para executáveis .COM (DOS)

section .data
    ; Memória RAM simulada (Vetor de dados)
    ; Índice 0: Dado A (5), Índice 1: Dado B (3), Índice 2: Resultado (0)
    memoria db 5, 3, 0 

    ; Código de Máquina simulado (Programa na Memória de Instruções)
    ; Formato: [Opcode, Operando]
    ; Opcodes: 1 = LOAD, 2 = ADD, 3 = STORE, 0 = HALT
    programa db 1, 0    ; LOAD do índice 0 (Registrador = 5)
             db 2, 1    ; ADD do índice 1  (Registrador = 5 + 3 = 8)
             db 3, 2    ; STORE no índice 2 (Memória[2] = 8)
             db 0, 0    ; HALT (Para a CPU)

    ; Mensagem de sucesso
    msg_sucesso db "Execucao concluida! Resultado salvo na memoria[2].", 13, 10, "$"

    section .bss
    ; Registradores internos da nossa CPU simulada
    PC  resw 1    ; Program Counter (Ponteiro de Instrução)
    IR_op resb 1 ; Instruction Register (Opcode)
    IR_oprd resb 1; Instruction Register (Operando)
    ACC resb 1   ; Acumulador (Registrador de dados principal)

section .text
inicio:
    ; Inicializa o Program Counter no início do vetor 'programa'
    mov word [PC], 0
    mov byte [ACC], 0

ciclo_cpu:
    ; --- 1. BUSCA (FETCH) ---
    mov si, [PC]
    
    ; Lê o Opcode e o Operando da memória de programa
    mov al, [programa + si]
    mov [IR_op], al
    mov al, [programa + si + 1]
    mov [IR_oprd], al
    
    ; Incrementa o PC para a próxima instrução (2 bytes por instrução)
    add word [PC], 2

    ; --- 2. DECODIFICAÇÃO (DECODE) ---
    mov al, [IR_op]
    
    cmp al, 0
    je halt_cpu       ; Se Opcode == 0 (HALT)
    
    cmp al, 1
    je exec_load      ; Se Opcode == 1 (LOAD)
    
    cmp al, 2
    je exec_add       ; Se Opcode == 2 (ADD)
    
    cmp al, 3
    je exec_store     ; Se Opcode == 3 (STORE)
    
    jmp ciclo_cpu     ; Instrução inválida ignora e continua