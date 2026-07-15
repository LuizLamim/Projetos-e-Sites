section .data
    ; Seção de dados inicializados
    msg db 'Operacoes da CPU concluidas com sucesso!', 0xA  ; String com quebra de linha (0xA)
    len equ $ - msg                                         ; Calcula o tamanho da string