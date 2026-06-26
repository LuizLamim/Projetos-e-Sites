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