import tkinter as tk
from tkinter import ttk, messagebox
from controllers.aluno_controller import AlunoController
from controllers.professor_controller import ProfessorController
from controllers.disciplina_controller import DisciplinaController
from controllers.relatorio_controller import RelatorioController

class DeskAppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("DeskApp - Sistema Escolar Completo")
        self.root.geometry("700x600")
        
        self.style = ttk.Style()
        self.style.theme_use('winnative')
        self.root.configure(bg="#4040fa")
        
        self.aluno_controller = AlunoController()
        self.prof_controller = ProfessorController()
        self.disciplina_controller = DisciplinaController()
        self.relatorio_controller = RelatorioController()

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(pady=10, expand=True, fill='both')

        self.tab_pessoas = ttk.Frame(self.notebook)
        self.tab_disciplinas = ttk.Frame(self.notebook)
        self.tab_notas = ttk.Frame(self.notebook)
        self.tab_relatorios = ttk.Frame(self.notebook)

        self.notebook.add(self.tab_pessoas, text='1. Cadastros')
        self.notebook.add(self.tab_disciplinas, text='2. Disciplinas/Matrículas')
        self.notebook.add(self.tab_notas, text='3. Lançar Notas')
        self.notebook.add(self.tab_relatorios, text='4. Relatórios')

        self.montar_tab_pessoas()
        self.montar_tab_disciplinas()
        self.montar_tab_notas()
        self.montar_tab_relatorios()

    # MONTAGEM DAS TELAS (FRONT-END)
    
    def montar_tab_pessoas(self):
        frame_aluno = ttk.LabelFrame(self.tab_pessoas, text=" Cadastrar Novo Aluno ")
        frame_aluno.pack(fill="x", padx=15, pady=10)

        ttk.Label(frame_aluno, text="Nome:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.entry_aluno_nome = ttk.Entry(frame_aluno, width=40)
        self.entry_aluno_nome.grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(frame_aluno, text="Email:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry_aluno_email = ttk.Entry(frame_aluno, width=40)
        self.entry_aluno_email.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(frame_aluno, text="Matrícula (RA):").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.entry_aluno_ra = ttk.Entry(frame_aluno, width=40)
        self.entry_aluno_ra.grid(row=2, column=1, padx=10, pady=5)

        ttk.Button(frame_aluno, text="Salvar Aluno", command=self.cadastrar_aluno).grid(row=3, column=0, columnspan=2, pady=10)

        frame_prof = ttk.LabelFrame(self.tab_pessoas, text=" Cadastrar Novo Professor ")
        frame_prof.pack(fill="x", padx=15, pady=10)

        ttk.Label(frame_prof, text="Nome:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.entry_prof_nome = ttk.Entry(frame_prof, width=40)
        self.entry_prof_nome.grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(frame_prof, text="Email:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry_prof_email = ttk.Entry(frame_prof, width=40)
        self.entry_prof_email.grid(row=1, column=1, padx=10, pady=5)

        ttk.Button(frame_prof, text="Salvar Professor", command=self.cadastrar_professor).grid(row=2, column=0, columnspan=2, pady=10)

    def montar_tab_disciplinas(self):
        frame_disc = ttk.LabelFrame(self.tab_disciplinas, text=" Criar Disciplina ")
        frame_disc.pack(fill="x", padx=15, pady=10)

        ttk.Label(frame_disc, text="Nome:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.entry_disc_nome = ttk.Entry(frame_disc, width=40)
        self.entry_disc_nome.grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(frame_disc, text="Código:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry_disc_codigo = ttk.Entry(frame_disc, width=40)
        self.entry_disc_codigo.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(frame_disc, text="Professor Resp:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.combo_professores = ttk.Combobox(frame_disc, width=37, state="readonly")
        self.combo_professores.grid(row=2, column=1, padx=10, pady=5)

        ttk.Button(frame_disc, text="Criar Disciplina", command=self.cadastrar_disciplina).grid(row=3, column=0, columnspan=2, pady=10)

        frame_mat = ttk.LabelFrame(self.tab_disciplinas, text=" Matricular Aluno ")
        frame_mat.pack(fill="x", padx=15, pady=10)

        ttk.Label(frame_mat, text="Aluno:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.combo_alunos = ttk.Combobox(frame_mat, width=37, state="readonly")
        self.combo_alunos.grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(frame_mat, text="Disciplina:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.combo_disciplinas = ttk.Combobox(frame_mat, width=37, state="readonly")
        self.combo_disciplinas.grid(row=1, column=1, padx=10, pady=5)

        ttk.Button(frame_mat, text="Efetivar Matrícula", command=self.matricular_aluno).grid(row=2, column=0, columnspan=2, pady=10)

    def montar_tab_notas(self):
        frame_notas = ttk.LabelFrame(self.tab_notas, text=" Registro de Desempenho ")
        frame_notas.pack(fill="x", padx=15, pady=10)

        ttk.Label(frame_notas, text="1º Selecione a Disciplina:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.combo_notas_disc = ttk.Combobox(frame_notas, width=37, state="readonly")
        self.combo_notas_disc.grid(row=0, column=1, padx=10, pady=5)
        self.combo_notas_disc.bind('<<ComboboxSelected>>', self.filtrar_alunos_matriculados)

        ttk.Label(frame_notas, text="2º Selecione o Aluno:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.combo_notas_aluno = ttk.Combobox(frame_notas, width=37, state="readonly")
        self.combo_notas_aluno.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(frame_notas, text="Nota (0 a 10):").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.entry_nota = ttk.Entry(frame_notas, width=40)
        self.entry_nota.grid(row=2, column=1, padx=10, pady=5)

        ttk.Label(frame_notas, text="Frequência (%):").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.entry_freq = ttk.Entry(frame_notas, width=40)
        self.entry_freq.grid(row=3, column=1, padx=10, pady=5)

        ttk.Button(frame_notas, text="Gravar Desempenho", command=self.salvar_notas).grid(row=4, column=0, columnspan=2, pady=15)

    def montar_tab_relatorios(self):
        frame_rel = ttk.Frame(self.tab_relatorios)
        frame_rel.pack(fill="both", expand=True, padx=15, pady=15)

        ttk.Label(frame_rel, text="Selecione a Disciplina para Emitir o Boletim:", font=("Arial", 10, "bold")).pack(pady=5)
        self.combo_relatorio_disc = ttk.Combobox(frame_rel, width=50, state="readonly")
        self.combo_relatorio_disc.pack(pady=5)

        ttk.Button(frame_rel, text="Gerar Relatório Completo", command=self.gerar_relatorio).pack(pady=10)

        self.texto_relatorio = tk.Text(frame_rel, height=18, width=70, font=("Courier", 10), bg="#ffffff")
        self.texto_relatorio.pack(pady=10)
    
    def atualizar_listas_dropdown(self):
        self.combo_professores['values'] = [f"{p.nome} ({p.email})" for p in self.prof_controller.listar()]
        self.combo_alunos['values'] = [f"{a.nome} ({a.ra})" for a in self.aluno_controller.listar()]
        
        lista_disc = [f"{d.nome} ({d.codigo})" for d in self.disciplina_controller.listar()]
        self.combo_disciplinas['values'] = lista_disc
        self.combo_notas_disc['values'] = lista_disc
        self.combo_relatorio_disc['values'] = lista_disc

    def filtrar_alunos_matriculados(self, event):
        """Ao escolher uma disciplina na aba de notas, mostra apenas os alunos dela"""
        disc_sel = self.combo_notas_disc.get()
        if disc_sel:
            codigo_disc = disc_sel.split("(")[1].strip(")")
            disc = next((d for d in self.disciplina_controller.listar() if d.codigo == codigo_disc), None)
            if disc:
                self.combo_notas_aluno['values'] = [f"{m.aluno.nome} ({m.aluno.ra})" for m in disc.matriculas]
                self.combo_notas_aluno.set('') 

    def cadastrar_aluno(self):
        nome = self.entry_aluno_nome.get()
        email = self.entry_aluno_email.get()
        ra = self.entry_aluno_ra.get()

        if nome and email and ra:
            self.aluno_controller.cadastrar(nome, email, ra)
            messagebox.showinfo("Sucesso", f"O aluno {nome} foi salvo!")
            self.entry_aluno_nome.delete(0, tk.END)
            self.entry_aluno_email.delete(0, tk.END)
            self.entry_aluno_ra.delete(0, tk.END)
            self.atualizar_listas_dropdown()
        else:
            messagebox.showwarning("Erro", "Preencha todos os campos.")

    def cadastrar_professor(self):
        nome = self.entry_prof_nome.get()
        email = self.entry_prof_email.get()

        if nome and email:
            self.prof_controller.cadastrar(nome, email)
            messagebox.showinfo("Sucesso", f"O professor {nome} foi salvo!")
            self.entry_prof_nome.delete(0, tk.END)
            self.entry_prof_email.delete(0, tk.END)
            self.atualizar_listas_dropdown()
        else:
            messagebox.showwarning("Erro", "Preencha todos os campos.")

    def cadastrar_disciplina(self):
        nome = self.entry_disc_nome.get()
        codigo = self.entry_disc_codigo.get()
        prof_sel = self.combo_professores.get()

        if nome and codigo and prof_sel:
            email_prof = prof_sel.split("(")[1].strip(")")
            prof = next((p for p in self.prof_controller.listar() if p.email == email_prof), None)

            if prof:
                self.disciplina_controller.cadastrar(nome, codigo, prof)
                messagebox.showinfo("Sucesso", "Disciplina criada!")
                self.entry_disc_nome.delete(0, tk.END)
                self.entry_disc_codigo.delete(0, tk.END)
                self.combo_professores.set('')
                self.atualizar_listas_dropdown()
        else:
            messagebox.showwarning("Erro", "Preencha todos os campos.")

    def matricular_aluno(self):
        aluno_sel = self.combo_alunos.get()
        disc_sel = self.combo_disciplinas.get()

        if aluno_sel and disc_sel:
            ra_aluno = aluno_sel.split("(")[1].strip(")")
            codigo_disc = disc_sel.split("(")[1].strip(")")

            aluno = next((a for a in self.aluno_controller.listar() if a.ra == ra_aluno), None)
            disc = next((d for d in self.disciplina_controller.listar() if d.codigo == codigo_disc), None)

            if aluno and disc:
                if disc.matricular_aluno(aluno):
                    messagebox.showinfo("Sucesso", "Matrícula realizada!")
                else:
                    messagebox.showwarning("Aviso", "Aluno já matriculado.")
                self.combo_alunos.set('')
                self.combo_disciplinas.set('')
        else:
            messagebox.showwarning("Erro", "Selecione Aluno e Disciplina.")

    def salvar_notas(self):
        disc_sel = self.combo_notas_disc.get()
        aluno_sel = self.combo_notas_aluno.get()
        nota_str = self.entry_nota.get().replace(',', '.')
        freq_str = self.entry_freq.get().replace(',', '.')

        if disc_sel and aluno_sel and nota_str and freq_str:
            try:
                nota = float(nota_str)
                freq = float(freq_str)

                if not (0 <= nota <= 10) or not (0 <= freq <= 100):
                    messagebox.showwarning("Erro", "A nota deve ser de 0 a 10 e a frequência de 0 a 100.")
                    return

                codigo_disc = disc_sel.split("(")[1].strip(")")
                ra_aluno = aluno_sel.split("(")[1].strip(")")

                disc = next((d for d in self.disciplina_controller.listar() if d.codigo == codigo_disc), None)
                if disc:
                    matricula_alvo = next((m for m in disc.matriculas if m.aluno.ra == ra_aluno), None)
                    if matricula_alvo:
                        matricula_alvo.nota = nota
                        matricula_alvo.frequencia = freq
                        
                        if nota >= 6.0 and freq >= 75.0:
                            matricula_alvo.status = "Aprovado"
                        else:
                            matricula_alvo.status = "Reprovado"
                        
                        messagebox.showinfo("Sucesso", f"Avaliação de {matricula_alvo.aluno.nome} salva!\nStatus: {matricula_alvo.status}")
                        self.entry_nota.delete(0, tk.END)
                        self.entry_freq.delete(0, tk.END)
                        self.combo_notas_aluno.set('')
            except ValueError:
                messagebox.showwarning("Erro", "Digite apenas números válidos.")
        else:
            messagebox.showwarning("Aviso", "Preencha todos os campos da nota e frequência.")

    def gerar_relatorio(self):
        disc_sel = self.combo_relatorio_disc.get()
        if disc_sel:
            codigo_disc = disc_sel.split("(")[1].strip(")")
            disc = next((d for d in self.disciplina_controller.listar() if d.codigo == codigo_disc), None)

            if disc:
                # Construção manual do Relatório para garantir a exibição das Notas,
                # Frequência e Status, independentemente do que tem no RelatorioController antigo.
                texto =  f"╔════════════════════════════════════════════════════╗\n"
                texto += f"║ RELATÓRIO DE DESEMPENHO ACADÊMICO                    \n"
                texto += f"╠════════════════════════════════════════════════════╣\n"
                texto += f"  Disciplina: {disc.nome} ({disc.codigo})\n"
                texto += f"  Professor: {disc.professor.nome}\n"
                texto += f"╚════════════════════════════════════════════════════╝\n\n"
                
                if len(disc.matriculas) == 0:
                    texto += " Nenhuma matrícula registrada para esta disciplina.\n"
                else:
                    for m in disc.matriculas:
                        marca = "✅" if m.status == "Aprovado" else ("❌" if m.status == "Reprovado" else "⏳")
                        
                        texto += f" 👤 Aluno: {m.aluno.nome} (RA: {m.aluno.ra})\n"
                        texto += f"    ├─ Nota Final: {m.nota:.1f}\n"
                        texto += f"    ├─ Frequência: {m.frequencia}%\n"
                        texto += f"    └─ Situação:   {marca} {m.status.upper()}\n"
                        texto += " ----------------------------------------------------\n"
                
                self.texto_relatorio.delete("1.0", tk.END)
                self.texto_relatorio.insert(tk.END, texto)
        else:
            messagebox.showwarning("Aviso", "Selecione uma disciplina.")
