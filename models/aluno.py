from models.pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, email, ra):
        super().__init__(nome, email)
        self.ra = ra

    def apresentar(self):
        return f"Aluno: {self.nome} | Matrícula: {self.ra} | Email: {self.email}"