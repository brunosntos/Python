import tkinter as tk
from tkinter import messagebox

def converter():
    try:
        # Pega o valor em dólares do entry
        valor_dolar = float(entry_dolar.get())
        # Define a cotação do dólar (exemplo: 5.20)
        cotacao_dolar = 5.20
        # Converte para reais
        valor_real = valor_dolar * cotacao_dolar
        # Exibe o resultado
        label_resultado.config(text=f"Valor em Reais: R$ {valor_real:.2f}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido.")

# Cria a janela principal
janela = tk.Tk()
janela.title("Conversor de Dólar para Real")

# Cria os widgets
label_dolar = tk.Label(janela, text="Valor em Dólares:")
label_dolar.pack(pady=10)

entry_dolar = tk.Entry(janela)
entry_dolar.pack(pady=5)

botao_converter = tk.Button(janela, text="Converter", command=converter)
botao_converter.pack(pady=20)

label_resultado = tk.Label(janela, text="")
label_resultado.pack(pady=10)

# Inicia o loop da interface
janela.mainloop()
