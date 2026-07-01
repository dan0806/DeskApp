from models.disciplina import Disciplina

class DisciplinaController:

    def __init__(self):
        self.disciplinas = []

    def cadastrar(self, nome, codigo, professor):
        disciplina = Disciplina(nome, codigo, professor)
        self.disciplinas.append(disciplina)
        return disciplina

    def listar(self):
        return self.disciplinas

    def matricular_aluno(self, disciplina, aluno):
        disciplina.matricular_aluno(aluno)

    def listar_alunos(self, disciplina):
        return disciplina.listar_alunos()
    
    def lancar_nota(self, disciplina, ra, nota):
        matricula = disciplina.buscar_matricula(ra)
        if matricula:
            matricula.registrar_nota(nota)
        
    def lancar_frequencia(self, disciplina, ra, frequencia):
        matricula = disciplina.buscar_matricula(ra)
        if matricula:
            matricula.registrar_frequencia(frequencia)