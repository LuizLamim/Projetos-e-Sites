       IDENTIFICATION DIVISION.
       PROGRAM-ID. SISTEMA-PAGAMENTOS.
       AUTHOR. Luiz Lamim

       ENVIRONMENT DIVISION.
       CONFIGURATION SECTION.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 DADOS-PAGAMENTO.
          05 ID-CLIENTE      PIC 9(05).
          05 VALOR-BRUTO     PIC 9(07)V99.
          05 TIPO-PAGAMENTO  PIC X(01). *> 'A' = A vista, 'P' = Parcelado
          05 VALOR-FINAL     PIC 9(07)V99.
          05 DESCONTO        PIC 9(05)V99.

       01 MENSAGENS.
          05 MSG-SUCESSO     PIC X(30) VALUE "PAGAMENTO PROCESSADO COM SUCESSO".

       PROCEDURE DIVISION.
       MAIN-PROCEDURE.
           
           *> Simulação de entrada de dados
           MOVE 12345 TO ID-CLIENTE.
           MOVE 1000.00 TO VALOR-BRUTO.
           MOVE 'A' TO TIPO-PAGAMENTO.

           *> Lógica de Negócio: 10% de desconto para pagamento a vista
           IF TIPO-PAGAMENTO = 'A' THEN
               COMPUTE DESCONTO = VALOR-BRUTO * 0.10
               COMPUTE VALOR-FINAL = VALOR-BRUTO - DESCONTO
           ELSE
               MOVE VALOR-BRUTO TO VALOR-FINAL
               MOVE 0 TO DESCONTO
           END-IF.