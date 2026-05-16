section .data
    msg db "Olá, Mundo!", 0xA  ; A mensagem a ser impressa, seguida de uma quebra de linha (0xA)
    len equ $ - msg            ; Calcula automaticamente o tamanho da string

section .text
    global _start              ; Define o ponto de entrada do programa