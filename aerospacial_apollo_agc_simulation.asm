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

section .text
    global _start

_start:
    ; --- 1. BOOT DO COMPUTADOR ---
    mov edx, msg_boot
    call print_string

    ; --- 2. VERIFICAÇÃO DE SOBRECARGA (O famoso Alarme 1202) ---
    ; No AGC real, o radar de aproximação mandava dados demais, gerando o erro 1202.
    ; O software executava o "Executive", que deletava tarefas de baixa prioridade.
    mov ax, [cpu_load]
    cmp ax, 90                  ; Se a carga for maior que 90%...
    jl .engine_check            ; Se não, pula para o próximo passo

    ; Dispara Alarme 1202
    mov edx, msg_warn
    call print_string
    
    ; Simula a recuperação: reduz a carga limpando tarefas inúteis
    mov word [cpu_load], 45

.engine_check:
    mov edx, msg_ok
    call print_string

    ; --- 3. LOOP DE CONTROLE DO RCS (Atitude da Nave) ---
    ; O AGC lia os giroscópios e corrigia a posição acionando os propulsores a jato.
 .rcs_loop:
    mov ax, [pitch_error]
    cmp ax, 0                   ; O erro foi zerado?
    je .stable_orbit            ; Se sim, nave estabilizada

    ; Se o erro for grande, dispara o RCS
    mov edx, msg_rcs_fire
    call print_string

    ; Simula a correção diminuindo o erro (15 -> 10 -> 5 -> 0)
    sub word [pitch_error], 5
    jmp .rcs_loop               ; Repete até estabilizar

    ; --- 4. POUSO SEGURO ---
 .stable_orbit:
    mov edx, msg_stable
    call print_string

    ; --- 5. FINALIZAR PROGRAMA (Syscall exit) ---
    mov eax, 1                  ; sys_exit
    xor ebx, ebx                ; status 0
    int 0x80