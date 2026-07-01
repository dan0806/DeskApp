from models.pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome, email):
        super().__init__(nome, email)

    def apresentar(self):
        return f"Professor: {self.nome} | Email: {self.email}"