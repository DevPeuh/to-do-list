import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class ToDoList:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title('Lista de Tarefas')
        self.raiz.geometry('600x400')
        self.tarefas = []
        self.tarefas_exibidas = []

        self.interface()

    def interface(self):
        quadro = ttk.Frame(self.raiz)
        quadro.pack(pady=20)

        self.entrada_tarefa = ttk.Entry(quadro, width=40)
        self.entrada_tarefa.grid(row=0, column=0, padx=5)

        botao_adicionar = ttk.Button(quadro, text='Adicionar Tarefa', command=self.adicionar_tarefa)
        botao_adicionar.grid(row=0, column=2, padx=5)

        self.lista_tarefas = tk.Listbox(self.raiz, width=80, height=15)
        self.lista_tarefas.pack(pady=20)

        quadro_botoes = ttk.Frame(self.raiz)
        quadro_botoes.pack()

        botao_atualizar = tk.Button(quadro_botoes, text='Atualizar Tarefa', command=self.atualizar_tarefa)
        botao_atualizar.grid(row=0, column=0, padx=5)

        botao_excluir = ttk.Button(quadro_botoes, text='Excluir Tarefa', command=self.excluir_tarefa)
        botao_excluir.grid(row=0, column=1, padx=5)

        botao_concluir = tk.Button(quadro_botoes, text='Concluir Tarefa', command=self.concluir_tarefa)
        botao_concluir.grid(row=0, column=2, padx=5)

        botao_listar_pendentes = tk.Button(quadro_botoes, text='Listar Tarefas Pendentes', command=self.listar_tarefas_pendentes)
        botao_listar_pendentes.grid(row=0, column=3, padx=5)

        botao_listar_concluidas = ttk.Button(quadro_botoes, text='Listar Tarefas Concluídas', command=self.listar_tarefas_concluidas)
        botao_listar_concluidas.grid(row=0, column=4, padx=5)

    def adicionar_tarefa(self):
        tarefa = self.entrada_tarefa.get()
        if tarefa:
            self.tarefas.append({'tarefa': tarefa, 'concluido': False})
            self.entrada_tarefa.delete(0, tk.END)
            self.atualizar_lista()
        else:
            messagebox.showwarning('Aviso', 'Digite uma tarefa para adicionar!')

    def atualizar_tarefa(self):
        posicao_tarefa_selecionada = self.lista_tarefas.curselection()
        if posicao_tarefa_selecionada:
            posicao_tarefa_selecionada = posicao_tarefa_selecionada[0]
            nova_tarefa = self.entrada_tarefa.get()
            if nova_tarefa:
                tarefa_real = self.tarefas_exibidas[posicao_tarefa_selecionada]
                tarefa_real['tarefa'] = nova_tarefa
                self.entrada_tarefa.delete(0, tk.END)
                self.atualizar_lista()
            else:
                messagebox.showwarning('Aviso', 'Digite uma tarefa!')
        else:
            messagebox.showwarning('Aviso', 'Selecione uma tarefa!')

    def excluir_tarefa(self):
        posicao_tarefa_selecionada = self.lista_tarefas.curselection()
        if posicao_tarefa_selecionada:
            posicao_tarefa_selecionada = posicao_tarefa_selecionada[0]
            tarefa_real = self.tarefas_exibidas[posicao_tarefa_selecionada]
            self.tarefas.remove(tarefa_real)
            self.atualizar_lista()
        else:
            messagebox.showwarning('Aviso', 'Selecione uma tarefa para excluir!')

    def concluir_tarefa(self):
        posicao_tarefa_selecionada = self.lista_tarefas.curselection()
        if posicao_tarefa_selecionada:
            posicao_tarefa_selecionada = posicao_tarefa_selecionada[0]
            tarefa_real = self.tarefas_exibidas[posicao_tarefa_selecionada]
            tarefa_real['concluido'] = True
            self.atualizar_lista()
        else:
            messagebox.showwarning('Aviso', 'Selecione uma tarefa para marcar como concluída!')

    def listar_tarefas_pendentes(self):
        self.tarefas_exibidas = [tarefa for tarefa in self.tarefas if not tarefa['concluido']]
        self.atualizar_lista(True)

    def listar_tarefas_concluidas(self):
        self.tarefas_exibidas = [tarefa for tarefa in self.tarefas if tarefa['concluido']]
        self.atualizar_lista(True)

    def atualizar_lista(self, filtrada=False):
        self.lista_tarefas.delete(0, tk.END)
        if not filtrada:
            self.tarefas_exibidas = self.tarefas
        for tarefa in self.tarefas_exibidas:
            texto_exibicao = tarefa['tarefa']
            if tarefa['concluido']:
                texto_exibicao += ' (Concluída)'
            self.lista_tarefas.insert(tk.END, texto_exibicao)

def main():
    raiz = tk.Tk()
    app = ToDoList(raiz)
    raiz.mainloop()

if __name__ == "__main__":
    main()
