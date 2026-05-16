section .data
    msg db "Olá, Mundo!", 0xA  ; A mensagem a ser impressa, seguida de uma quebra de linha (0xA)
    len equ $ - msg            ; Calcula automaticamente o tamanho da string

section .text
    global _start              ; Define o ponto de entrada do programa

_start:
    ; 1. Imprimir a mensagem na tela (syscall: sys_write)
    mov rax, 1                 ; Número da chamada de sistema para 'write' (1)
    mov rdi, 1                 ; Descritor de arquivo: 1 é a saída padrão (stdout)
    mov rsi, msg               ; Endereço de memória onde a mensagem começa
    mov rdx, len               ; Quantidade de bytes a serem lidos (tamanho da mensagem)
    syscall                    ; Pede ao sistema operacional para executar a ação