section .data
    ; Simulando os sensores do satélite (valores em memória)
    altitude        dw 400      ; Altitude atual em km (ex: Órbita Baixa - LEO)
    energia         db 15       ; Nível de bateria (0 a 100%)
    
    ; Limiares de segurança
    ALTITUDE_CRITICA dw 350     ; Se cair abaixo disso, o satélite reentra na atmosfera
    BATERIA_BAIXA    db 20      ; Se cair abaixo disso, desliga sistemas não-essenciais

section .text
    global _start