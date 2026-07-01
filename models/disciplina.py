from models.matricula import Matricula
from models.professor import Professor
from models.aluno import Aluno

class Disciplina():
    def __init__(self, nome, codigo, professor: Professor):
        self.nome = nome
        self.codigo = codigo
        self.professor = professor
        self.matriculas = []

    def matricular_aluno(self, aluno: Aluno):
        for matricula in self.matriculas:
            if matricula.aluno.ra == aluno.ra:
                return False
        nova_matricula = Matricula(aluno, self)
        self.matriculas.append(nova_matricula)
        return True

    def apresentar(self):
        return f"Código: {self.codigo} | Nome: {self.nome}"
    
    def listar_alunos(self):
        return [matricula.aluno for matricula in self.matriculas]
    
    def buscar_matricula(self, ra):
        for matricula in self.matriculas:
            if matricula.aluno.ra == ra:
                return matricula
        return None
    
    def __str__(self):
        return self.apresentar()