import tkinter as tk

fonte = ("Arial", 16)

# Função que é chamada quando o botão é clicado
def gravar_valores():
    Descricao = entry1.get().upper()
    Codigo = entry2.get().upper()
    Revisao = entry3.get().upper()
    Desenhista = entry4.get().upper()
    Observacao = entry5.get().upper()
    #nome = entry1.get()
    #idade = entry2.get()
    #altura = entry3.get()
    #print(f"Nome: {nome}")
    #print(f"Idade: {idade}")
    #print(f"Altura: {altura}")
    print(Descricao, "\n",
          Codigo, "\n",
          Revisao, "\n",
          Desenhista)
    if Observacao != "":
        print(Observacao)
    else:
        print("Sem Observações")
# Cria a janela principal
janela = tk.Tk()
janela.geometry("800x500")
# Cria os widgets
label1 = tk.Label(janela, text="Descrição:", font=fonte)
entry1 = tk.Entry(janela, width=50, justify="center", font=fonte)

label2 = tk.Label(janela, text="Código:", font=fonte)
entry2 = tk.Entry(janela, width=7, justify="center", font=fonte)

label3 = tk.Label(janela, text="Revisão:", font=fonte)
entry3 = tk.Entry(janela, width=5, justify="center", font=fonte)

label4 = tk.Label(janela, text="Desenhista:")
entry4 = tk.Entry(janela)

label5 = tk.Label(janela, text="Observação:")
entry5 = tk.Entry(janela)

botao1 = tk.Button(janela, text="Enviar", command=gravar_valores)

# Organiza os widgets na janela
label1.place(x=10, y=10)
entry1.place(x=120, y=10)
label2.place(x=10, y=50)
entry2.place(x=120, y=50)
label3.place(x=230, y=50)
entry3.place(x=330, y=50)
label4.place(x=10, y=130)
entry4.place(x=120, y=130)
label5.place(x=10, y=170)
entry5.place(x=120, y=170)
botao1.place(x=380, y=200)

# Inicia o loop principal da interface gráfica
janela.mainloop()
