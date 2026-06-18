IDENTIFICATION DIVISION.
       PROGRAM-ID. SAT-MONITOR.
       AUTHOR. CLI
       DATE-WRITTEN. 2026-06-18.
      *----------------------------------------------------------------*
      * PROGRAMA QUE SIMULA O PROCESSAMENTO DE DADOS DE TELEMETRIA      *
      * DE UM SATÉLITE EM ÓRBITA.                                      *
      *----------------------------------------------------------------*

      ENVIRONMENT DIVISION.
       CONFIGURATION SECTION.
       SPECIAL-NAMES.
           DECIMAL-POINT IS COMMA.

       DATA DIVISION.
       WORKING-STORAGE SECTION.

       Mercedes-Benz dos Satélites - Dados de Entrada (Fictícios)
       01  REGISTRO-TELEMETRIA.
           05  ID-SATELITE        PIC X(08)   VALUE "ALFA-001".
           05  STATUS-BATERIA     PIC 9(03)   VALUE 085.
           05  TEMP-PAINEL        PIC S9(03)  VALUE +045.
           05  STATUS-SISTEMA     PIC X(02)   VALUE "OK".

        Variáveis de Controle e Limites Operacionais
       01  LIMITES-OPERACIONAIS.
           05  LIM-BATERIA-MIN    PIC 9(03)   VALUE 020.
           05  LIM-TEMP-MAX       PIC S9(03)  VALUE +080.
           05  LIM-TEMP-MIN       PIC S9(03)  VALUE -040.

        Variáveis de Formatação para o Relatório
       01  LINHA-ALERTA.
           05  FILLER             PIC X(15)   VALUE " >>> ALERTA: ".
           05  MSG-ALERTA         PIC X(40).

       PROCEDITION DIVISION.
       0000-PRINCIPAL.
           DISPLAY "=================================================="
           DISPLAY "    INICIANDO MONITORAMENTO DE TELEMETRIA          "
           DISPLAY "    SATÉLITE: " ID-SATELITE
           DISPLAY "=================================================="
           
           PERFORM 1000-VERIFICAR-BATERIA
           PERFORM 2000-VERIFICAR-TEMPERATURA
           PERFORM 3000-STATUS-GERAL
           
           DISPLAY "=================================================="
           DISPLAY "    FIM DO PROCESSAMENTO DE TELEMETRIA             "
           DISPLAY "=================================================="
           STOP RUN.

           1000-VERIFICAR-BATERIA.
           IF STATUS-BATERIA < LIM-BATERIA-MIN
               MOVE "BATERIA CRÍTICA! NÍVEL ABAIXO DE 20%" TO MSG-ALERTA
               DISPLAY LINHA-ALERTA
               MOVE "AL" TO STATUS-SISTEMA
           ELSE
               DISPLAY "STATUS BATERIA   : " STATUS-BATERIA "% - NORMAL"
           END-IF.

           2000-VERIFICAR-TEMPERATURA.
           IF TEMP-PAINEL > LIM-TEMP-MAX OR TEMP-PAINEL < LIM-TEMP-MIN
               MOVE "TEMPERATURA FORA DOS LIMITES SEGUROS!" TO MSG-ALERTA
               DISPLAY LINHA-ALERTA
               MOVE "AL" TO STATUS-SISTEMA
           ELSE
               DISPLAY "TEMP. DO PAINEL  : " TEMP-PAINEL " C - ESTÁVEL"
           END-IF.

           3000-STATUS-GERAL.
           DISPLAY "--------------------------------------------------"
           IF STATUS-SISTEMA = "OK"
               DISPLAY "STATUS GERAL     : SISTEMAS NOMINAIS"
           ELSE
               DISPLAY "STATUS GERAL     : ATENÇÃO! ANOMALIA DETECTADA!"
           END-IF.