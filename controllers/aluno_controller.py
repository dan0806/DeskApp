from models.aluno import Aluno

class AlunoController():
    def __init__(self):
        self.alunos = []

    def cadastrar(self, nome, email, ra):
        aluno = Aluno(nome, email, ra)
        self.alunos.append(aluno)
        return aluno

    def listar(self):
        return self.alunos
    