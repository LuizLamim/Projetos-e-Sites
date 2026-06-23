section .data
    ; Simulando os sensores do satélite (valores em memória)
    altitude        dw 400      ; Altitude atual em km (ex: Órbita Baixa - LEO)
    energia         db 15       ; Nível de bateria (0 a 100%)
    
    ; Limiares de segurança
    ALTITUDE_CRITICA dw 350     ; Se cair abaixo disso, o satélite reentra na atmosfera
    BATERIA_BAIXA    db 20      ; Se cair abaixo disso, desliga sistemas não-essenciais

section .text
    global _start

_start:
    ; ----------------------------------------------------
    ; LOOP PRINCIPAL DE CONTROLE DO SATÉLITE
    ; ----------------------------------------------------
loop_controle:

    ; 1. VERIFICAÇÃO DE ALTITUDE (Controle de Órbita)
    mov ax, [altitude]
    cmp ax, [ALTITUDE_CRITICA]
    jl  corrigir_orbita         ; Se altitude < crítica, liga propulsores

    ; 2. VERIFICAÇÃO DE ENERGIA (Subsistema de Potência)
    mov bl, [energia]
    cmp bl, [BATERIA_BAIXA]
    jl  modo_economia           ; Se bateria < baixa, entra em modo de segurança

    ; 3. OPERAÇÃO NORMAL
    ; (Aqui o satélite coletaria dados ou transmitiria sinal)
    jmp ciclo_concluido