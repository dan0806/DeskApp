from models.professor import Professor

class ProfessorController():
    def __init__(self):
        self.professores = []

    def cadastrar(self, nome, email):
        professor = Professor(nome, email)
        self.professores.append(professor)
        return professor

    def listar(self):
        return self.professores