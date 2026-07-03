import tkinter as tk
from tkinter import ttk, messagebox
from controllers.aluno_controller import AlunoController
from controllers.professor_controller import ProfessorController
from controllers.disciplina_controller import DisciplinaController
from controllers.relatorio_controller import RelatorioController

class DeskApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DeskApp - Sistema Escolar")
        self.root.geometry("950x650")
        
        self.style = ttk.Style()
        
        # Muda o tema global (Tente trocar 'alt', 'default', 'classic', 'clam', 'winnative', 'aqua', 'vista', 'xpnative' para ver as diferenças)
        self.style.theme_use('winnative') 
        
        # Mudando a cor de fundo da janela principal
        self.root.configure(bg="#3058EB") # Um tom de cinza bem escuro (Dark Mode)

        self.aluno_controller = AlunoController()
        self.prof_controller = ProfessorController()
        self.disciplina_controller = DisciplinaController()
        self.relatorio_controller = RelatorioController()

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(pady=15, expand=True, fill='both')

        self.tab_pessoas = ttk.Frame(self.notebook)
        self.tab_disciplinas = ttk.Frame(self.notebook)
        self.tab_relatorios = ttk.Frame(self.notebook)

        self.notebook.add(self.tab_pessoas, text='1. Cadastros de novas Pessoas')
        self.notebook.add(self.tab_disciplinas, text='2. Disciplinas e Matrículas')
        self.notebook.add(self.tab_relatorios, text='3. Gerar Relatórios')

        self.montar_tab_pessoas()
        self.montar_tab_disciplinas()
        self.montar_tab_relatorios()

    
    def montar_tab_pessoas(self):
        # PAINEL DO ALUNO
        frame_aluno = ttk.LabelFrame(self.tab_pessoas, text=" Cadastrar Novo Aluno ")
        frame_aluno.pack(fill="x", padx=250, pady=10)

        ttk.Label(frame_aluno, text="Nome do Aluno:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.entry_aluno_nome = ttk.Entry(frame_aluno, width=40)
        self.entry_aluno_nome.grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(frame_aluno, text="Email:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry_aluno_email = ttk.Entry(frame_aluno, width=40)
        self.entry_aluno_email.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(frame_aluno, text="Matrícula (RA):").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.entry_aluno_ra = ttk.Entry(frame_aluno, width=40)
        self.entry_aluno_ra.grid(row=2, column=1, padx=10, pady=5)

        ttk.Button(frame_aluno, text="Salvar Aluno", command=self.cadastrar_aluno).grid(row=3, column=0, columnspan=2, pady=10)

        # PAINEL DO PROFESSOR
        frame_prof = ttk.LabelFrame(self.tab_pessoas, text=" Cadastrar Novo Professor ")
        frame_prof.pack(fill="x", padx=250, pady=10)

        ttk.Label(frame_prof, text="Nome do Professor:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.entry_prof_nome = ttk.Entry(frame_prof, width=40)
        self.entry_prof_nome.grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(frame_prof, text="Email:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry_prof_email = ttk.Entry(frame_prof, width=40)
        self.entry_prof_email.grid(row=1, column=1, padx=10, pady=5)

        ttk.Button(frame_prof, text="Salvar Professor", command=self.cadastrar_professor).grid(row=2, column=0, columnspan=2, pady=10)

    def montar_tab_disciplinas(self):
        # PAINEL DE NOVA DISCIPLINA
        frame_disc = ttk.LabelFrame(self.tab_disciplinas, text=" Criar Disciplina ")
        frame_disc.pack(fill="x", padx=250, pady=10)

        ttk.Label(frame_disc, text="Nome da Disciplina:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.entry_disc_nome = ttk.Entry(frame_disc, width=40)
        self.entry_disc_nome.grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(frame_disc, text="Código da Disciplina:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry_disc_codigo = ttk.Entry(frame_disc, width=40)
        self.entry_disc_codigo.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(frame_disc, text="Professor Responsável:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.combo_professores = ttk.Combobox(frame_disc, width=37, state="readonly")
        self.combo_professores.grid(row=2, column=1, padx=10, pady=5)

        ttk.Button(frame_disc, text="Criar Disciplina", command=self.cadastrar_disciplina).grid(row=3, column=0, columnspan=2, pady=10)

        # PAINEL DE MATRÍCULA
        frame_mat = ttk.LabelFrame(self.tab_disciplinas, text=" Matricular Aluno na Disciplina ")
        frame_mat.pack(fill="x", padx=250, pady=10)

        ttk.Label(frame_mat, text="Selecionar Aluno:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.combo_alunos = ttk.Combobox(frame_mat, width=37, state="readonly")
        self.combo_alunos.grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(frame_mat, text="Selecionar Disciplina:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.combo_disciplinas = ttk.Combobox(frame_mat, width=37, state="readonly")
        self.combo_disciplinas.grid(row=1, column=1, padx=10, pady=5)

        ttk.Button(frame_mat, text="Efetivar Matrícula", command=self.matricular_aluno).grid(row=2, column=0, columnspan=2, pady=10)

    def montar_tab_relatorios(self):
        frame_rel = ttk.Frame(self.tab_relatorios)
        frame_rel.pack(fill="both", expand=True, padx=10, pady=15)

        ttk.Label(frame_rel, text="Selecione a Disciplina para Emitir o Boletim:", font=("Arial", 10, "bold")).pack(pady=5)
        self.combo_relatorio_disc = ttk.Combobox(frame_rel, width=50, state="readonly")
        self.combo_relatorio_disc.pack(pady=5)

        ttk.Button(frame_rel, text="Gerar Relatório completo da Disciplina", command=self.gerar_relatorio).pack(pady=10)

        self.texto_relatorio = tk.Text(frame_rel, height=35, width=100, font=("Consolas", 10), bg="#f4f4f4")
        self.texto_relatorio.pack(pady=10)

    
    def atualizar_listas_dropdown(self):
        #Toda vez que alguém é cadastrado, atualiza os menus
        self.combo_professores['values'] = [f"{p.nome} ({p.email})" for p in self.prof_controller.listar()]
        self.combo_alunos['values'] = [f"{a.nome} ({a.ra})" for a in self.aluno_controller.listar()]
        
        lista_disc = [f"{d.nome} ({d.codigo})" for d in self.disciplina_controller.listar()]
        self.combo_disciplinas['values'] = lista_disc
        self.combo_relatorio_disc['values'] = lista_disc

    def cadastrar_aluno(self):
        nome = self.entry_aluno_nome.get()
        email = self.entry_aluno_email.get()
        ra = self.entry_aluno_ra.get()

        if nome and email and ra:
            self.aluno_controller.cadastrar(nome, email, ra)
            messagebox.showinfo("Sucesso", f"O aluno {nome} foi salvo no sistema!")
            
            self.entry_aluno_nome.delete(0, tk.END)
            self.entry_aluno_email.delete(0, tk.END)
            self.entry_aluno_ra.delete(0, tk.END)
            self.atualizar_listas_dropdown()
        else:
            messagebox.showwarning("Erro de Validação", "Por favor, preencha Nome, Email e RA do aluno.")

    def cadastrar_professor(self):
        nome = self.entry_prof_nome.get()
        email = self.entry_prof_email.get()

        if nome and email:
            self.prof_controller.cadastrar(nome, email)
            messagebox.showinfo("Sucesso", f"O professor {nome} foi salvo no sistema!")
            
            self.entry_prof_nome.delete(0, tk.END)
            self.entry_prof_email.delete(0, tk.END)
            self.atualizar_listas_dropdown()
        else:
            messagebox.showwarning("Erro de Validação", "Por favor, preencha Nome e Email do professor.")

    def cadastrar_disciplina(self):
        nome = self.entry_disc_nome.get()
        codigo = self.entry_disc_codigo.get()
        prof_selecionado = self.combo_professores.get()

        if nome and codigo and prof_selecionado:
            email_prof = prof_selecionado.split("(")[1].strip(")")
            prof = next((p for p in self.prof_controller.listar() if p.email == email_prof), None)

            if prof:
                self.disciplina_controller.cadastrar(nome, codigo, prof)
                messagebox.showinfo("Sucesso", f"Disciplina {codigo} criada com sucesso!")
                self.entry_disc_nome.delete(0, tk.END)
                self.entry_disc_codigo.delete(0, tk.END)
                self.combo_professores.set('') 
                self.atualizar_listas_dropdown()
        else:
            messagebox.showwarning("Erro de Validação", "Preencha o Nome, Código e vincule um Professor.")

    def matricular_aluno(self):
        aluno_sel = self.combo_alunos.get()
        disc_sel = self.combo_disciplinas.get()

        if aluno_sel and disc_sel:
            ra_aluno = aluno_sel.split("(")[1].strip(")")
            codigo_disc = disc_sel.split("(")[1].strip(")")

            aluno = next((a for a in self.aluno_controller.listar() if a.ra == ra_aluno), None)
            disc = next((d for d in self.disciplina_controller.listar() if d.codigo == codigo_disc), None)

            if aluno and disc:
                sucesso = disc.matricular_aluno(aluno)
                if sucesso:
                    messagebox.showinfo("Sucesso", "Matrícula realizada e confirmada!")
                else:
                    messagebox.showwarning("Aviso", "O aluno já estava matriculado nesta disciplina.")
                
                self.combo_alunos.set('')
                self.combo_disciplinas.set('')
        else:
            messagebox.showwarning("Erro de Validação", "Você precisa selecionar um Aluno e uma Disciplina.")

    def gerar_relatorio(self):
        disc_sel = self.combo_relatorio_disc.get()
        if disc_sel:
            codigo_disc = disc_sel.split("(")[1].strip(")")
            disc = next((d for d in self.disciplina_controller.listar() if d.codigo == codigo_disc), None)

            if disc:
                texto = self.relatorio_controller.gerar_relatorio(disc)
                
                self.texto_relatorio.delete("1.0", tk.END)
                self.texto_relatorio.insert(tk.END, texto)
        else:
            messagebox.showwarning("Aviso", "Por favor, selecione uma disciplina para gerar o relatório.")


if __name__ == "__main__":
    janela_principal = tk.Tk()
    app = DeskApp(janela_principal)
    janela_principal.mainloop()