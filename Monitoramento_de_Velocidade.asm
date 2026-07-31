; =====================================================================
; Sistema de Monitoramento de Velocidade (Overspeed Warning)
; Arquitetura: x86 (Exemplo de sistema embarcado legado)
; =====================================================================

section .data
    VNE_LIMIT equ 350       ; Limite de velocidade estrutural em nós (knots)
    PORT_PITOT equ 0x300    ; Endereço de I/O mapeado para o sensor Pitot
    PORT_ALARM equ 0x302    ; Endereço de I/O mapeado para o alarme no painel

section .text
    global _start

_start:
    ; Ponto de entrada do sistema

flight_control_loop:
    ; 1. AQUISIÇÃO DE DADOS (Leitura do Sensor)
    mov dx, PORT_PITOT      ; Carrega o endereço da porta do sensor no registrador de dados (DX)
    in ax, dx               ; Lê o valor do hardware (velocidade atual) e salva no registrador AX

    ; 2. LÓGICA DE CONTROLE (Comparação)
    cmp ax, VNE_LIMIT       ; Compara a velocidade atual (AX) com o limite seguro (350 nós)
    jge trigger_alarm       ; Se for Maior ou Igual (Jump if Greater or Equal), pula para o alarme

    ; 3. ATUAÇÃO: ESTADO SEGURO
    mov dx, PORT_ALARM      ; Aponta para a porta do alarme
    mov al, 0               ; Prepara o sinal 0 (Desligado)
    out dx, al              ; Envia o sinal para o hardware apagar a luz/som
    jmp next_cycle          ; Pula a rotina de ativação do alarme


trigger_alarm:
    ; 4. ATUAÇÃO: ESTADO CRÍTICO
    mov dx, PORT_ALARM      ; Aponta para a porta do alarme
    mov al, 1               ; Prepara o sinal 1 (Ligado)
    out dx, al              ; Envia o sinal para o hardware acender a luz/tocar o aviso sonoro

next_cycle:
    ; 5. SINCRONIZAÇÃO
    ; Em um sistema real, haveria uma interrupção de timer aqui 
    ; para garantir que o loop rode a uma frequência exata (ex: 50Hz).
    jmp flight_control_loop ; Reinicia o ciclo infinitamente