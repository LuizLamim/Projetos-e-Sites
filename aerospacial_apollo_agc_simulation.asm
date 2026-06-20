section .data
    ; Mensagens do painel do DSKY (Display and Keyboard)
    msg_boot      db "AGC BOOT SEQUENCING...", 10, 0
    msg_ok        db "[DSKY] PROG 11: LANDING MANEUVER ACTIVE", 10, 0
    msg_warn      db "[DSKY] *ALARM 1202* - CPU OVERLOAD! FLUSHING LOW PRIORITY...", 10, 0
    msg_rcs_fire  db "[RCS] THRUSTERS FIRING FOR ATTITUDE CORRECTION", 10, 0
    msg_stable    db "[DSKY] ORIENTATION STABLE. READY FOR TOUCHDOWN.", 10, 0

    ; Variáveis de estado da simulação
    cpu_load      dw 95          ; Carga da CPU em % (Simulando radar de pouso inundando a memória)
    pitch_error   dw 15          ; Erro de inclinação da nave (em graus)