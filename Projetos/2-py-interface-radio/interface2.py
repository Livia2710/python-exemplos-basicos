import tkinter as tk
from tkinter import ttk # ttk traz mais varriedade de opções para estilização

# Função para atualizar (Nome e escolhas do usuário)
def atualizar_resultado():
    # Obter o nome usuário
    nome = Caixa_texto.get()

    # Obter preferencia bebida "radio"
    preferencia = var_radio.get()

    # Verificar tipo de saudação marcada "checkbox"

    # Informal
    if var_check_saudacao.get():
        saudacao = "Olá"
    else:
        saudacao = "Bem-vindo!"

    # Formal
    if var_check_personalizada.get():
        saudacao = f"{saudacao}, caro(a)"

    # Obter cor favorita selecionada
    cor_favorita = combo_cor.get()

    # Montar a mensagem final
    mensagem = f"{saudacao} {nome} ! Você prefere {preferencia}. "
    if cor_favorita:
        mensagem += f"Sua cor favorita é {cor_favorita}."

    # Atualizar o texto do rótulo com a mensagem
    label_resulado.config(text=mensagem)


def limpar_campo():
    # Limpa todos os campos
    Caixa_texto.delete(0, tk.END)
    var_radio.set("Café")
    var_check_saudacao.set(False)
    var_check_personalizada.set(False)
    combo_cor.set("")
    label_resulado.config(text="")





# Janela principal
janela = tk.Tk()
janela.title("Interface Avançada")
janela.geometry("400x500")

# Criar caixa entra
label_nome = tk.Label(janela, text= "Digite seu nome: ")
label_nome.pack(pady=5)
Caixa_texto = tk.Entry(janela, width=40)
Caixa_texto.pack(pady=5)

# Criar botões de radio
label_preferencia = tk.Label(janela, text = "Escolha sua preferencia: ")
label_preferencia.pack(pady=5)
var_radio = tk.StringVar(value="Café")
radio_cafe = tk.Radiobutton(janela, text= "Café", variable=var_radio, value="Café")
radio_cha = tk.Radiobutton(janela, text= "Chá", variable=var_radio, value="Chá")
radio_suco = tk.Radiobutton(janela, text= "Suco", variable=var_radio, value="Suco")
radio_agua = tk.Radiobutton(janela, text= "Água", variable=var_radio, value="Água")

# Para aparecer as opções
radio_cafe.pack()
radio_cha.pack()
radio_suco.pack()
radio_agua.pack()

# Criar caixas de seleção  "CheckBox"
var_check_saudacao = tk.BooleanVar()
check_saudacao = tk.Checkbutton(janela, text="Usar saudação informal ",  variable=var_check_saudacao)
check_saudacao.pack(pady=5)

var_check_personalizada = tk.BooleanVar()
check_personalizada = tk.Checkbutton(janela, text="Usar saudação personalizada ",  variable=var_check_personalizada)
check_personalizada.pack(pady=5)

# Lista de opções "ComboBox"
label_cor = tk.Label(janela, text="Selecione sua cor favorita: ")
label_cor.pack(pady=5)
combo_cor = ttk.Combobox(janela, values=["Vermelho", "Azul", "Verde", "Preto", "Branco"]) 
combo_cor.pack(pady=5)

# Criar botões
botao_atualizar = tk.Button(janela, text="Atualizar", command=atualizar_resultado)
botao_atualizar.pack(pady=10)

botao_limpar = tk.Button(janela, text="Limpar", command=limpar_campo)
botao_limpar.pack(pady=10)

# Criar um rótulo para mostrar o resultado "Label"
label_resulado = tk.Label(janela, text="", wraplength=350)
label_resulado.pack(pady=10)



# Executar a janela principal
janela.mainloop()