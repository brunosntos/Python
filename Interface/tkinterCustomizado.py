import customtkinter as ctk

# Função para converter real para dólar
def converter():
    try:
        valor_real = float(entry_real.get())
        taxa_cambio = 5.0  # Exemplo de taxa de câmbio (1 dólar = 5 reais)
        valor_dolar = valor_real / taxa_cambio
        label_resultado.configure(text=f"Dólares: {valor_dolar:.2f}")
    except ValueError:
        label_resultado.configure(text="Por favor, insira um valor válido.")

# Criar a janela principal
ctk.set_appearance_mode("light")  # ou "dark"
ctk.set_default_color_theme("blue")  # ou "green", "dark-blue", etc.

janela = ctk.CTk()
janela.title("Conversor de Real para Dólar")

# Criar elementos da interface
label_instrucoes = ctk.CTkLabel(janela, text="Digite o valor em Reais:")
label_instrucoes.pack(pady=10)

entry_real = ctk.CTkEntry(janela)
entry_real.pack(pady=10)

botao_converter = ctk.CTkButton(janela, text="Converter", command=converter)
botao_converter.pack(pady=10)

label_resultado = ctk.CTkLabel(janela, text="")
label_resultado.pack(pady=10)

# Iniciar a aplicação
janela.mainloop()
