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