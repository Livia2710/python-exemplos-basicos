import tkinter as tk 

# Função para transferir texto do input para o label
def mostrar_mensagem():
    texto = caixa_texto.get() #Obter o texto da caixa de texto
    label_resultado.config(text=texto) #Atualiza o texto  do label

# Janela principal
janela = tk.Tk()
janela.title("Exemplo de interface") 
janela.geometry("400x150") #Tamanho dajanela

# Criar uma caixa de texto para entrada
caixa_texto = tk.Entry(janela, width=60)
caixa_texto.pack(pady=10) #padding y (vertical)

# Criar um botão
botao = tk.Button(janela, text="Mostrar texto", command=mostrar_mensagem) # define a função
botao.pack(pady=5) # Só aparece quando coloca algum tamanho

# Criar rótulo  para mostar o resultado "Label"
label_resultado = tk.Label(janela, text="")
label_resultado.pack(pady=5) # Tem que colocar para o label aparecer

# Executar a janela principal
janela.mainloop()