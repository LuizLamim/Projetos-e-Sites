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


; ----------------------------------------------------
; SUBROTINAS DEAÇÃO (ATUADORES)
; ----------------------------------------------------

corrigir_orbita:
    ; Simula o disparo dos propulsores químicos/iônicos
    mov ax, [altitude]
    add ax, 50                  ; Eleva a altitude em 50km
    mov [altitude], ax
    
    ; O uso dos propulsores gasta muita energia
    mov cl, [energia]
    sub cl, 10                  ; Consome 10% de bateria
    mov [energia], cl
    
    jmp loop_controle           ; Volta para o monitoramento

modo_economia:
    ; Desliga payloads (câmeras, experimentos) e orienta painéis ao Sol
    mov cl, [energia]
    add cl, 30                  ; Painéis solares recarregam +30%
    mov [energia], cl
    
    jmp loop_controle           ; Volta para o monitoramento

ciclo_concluido:
    ; Fim do ciclo de telemetria. Em um sistema real, haveria um delay aqui.
    ; Para encerrar a simulação no Linux:
    mov eax, 1                  ; Syscall sys_exit
    xor ebx, ebx                ; Status 0 (sucesso)
    int 0x80