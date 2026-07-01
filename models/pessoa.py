class Pessoa():
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def apresentar(self):
        return f"Pessoa: {self.nome} | Email: {self.email}"
    
    def __str__(self):
        return self.apresentar()