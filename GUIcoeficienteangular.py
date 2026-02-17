import customtkinter as ctk

# Configurações de aparência
ctk.set_appearance_mode("dark")  # Opções: "dark", "light"
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Calculadora de Coeficiente Angular")
        self.geometry("400x450")
        self.resizable(False, False)

        # Título principal
        self.label_titulo = ctk.CTkLabel(self, text="Cálculo de Inclinação", font=("Roboto", 24, "bold"))
        self.label_titulo.pack(pady=20)

        # Container para os inputs
        self.frame_inputs = ctk.CTkFrame(self)
        self.frame_inputs.pack(pady=10, padx=20, fill="both")

        # Ponto 1
        self.label_p1 = ctk.CTkLabel(self.frame_inputs, text="Ponto 1 (x1, y1)")
        self.label_p1.grid(row=0, column=0, columnspan=2, pady=5)
        self.x1 = ctk.CTkEntry(self.frame_inputs, placeholder_text="x1")
        self.x1.grid(row=1, column=0, padx=10, pady=5)
        self.y1 = ctk.CTkEntry(self.frame_inputs, placeholder_text="y1")
        self.y1.grid(row=1, column=1, padx=10, pady=5)

        # Ponto 2
        self.label_p2 = ctk.CTkLabel(self.frame_inputs, text="Ponto 2 (x2, y2)")
        self.label_p2.grid(row=2, column=0, columnspan=2, pady=5)
        self.x2 = ctk.CTkEntry(self.frame_inputs, placeholder_text="x2")
        self.x2.grid(row=3, column=0, padx=10, pady=5)
        self.y2 = ctk.CTkEntry(self.frame_inputs, placeholder_text="y2")
        self.y2.grid(row=3, column=1, padx=10, pady=5)

        # Botão Calcular
        self.btn_calcular = ctk.CTkButton(self, text="Calcular m", command=self.calcular, font=("Roboto", 16))
        self.btn_calcular.pack(pady=20)

        # Label de Resultado
        self.lbl_resultado = ctk.CTkLabel(self, text="Resultado: -", font=("Roboto", 18, "italic"))
        self.lbl_resultado.pack(pady=10)

    def calcular(self):
        try:
            x1 = float(self.x1.get())
            y1 = float(self.y1.get())
            x2 = float(self.x2.get())
            y2 = float(self.y2.get())

            dx = x2 - x1
            dy = y2 - y1

            if dx == 0:
                self.lbl_resultado.configure(text="Resultado: Reta Vertical (Indefinido)", text_color="#FF6B6B")
            else:
                m = dy / dx
                self.lbl_resultado.configure(text=f"Coeficiente (m): {m:.2f}", text_color="#1DD1A1")
        except ValueError:
            self.lbl_resultado.configure(text="Erro: Digite apenas números!", text_color="#FF6B6B")

if __name__ == "__main__":
    app = App()
    app.mainloop()