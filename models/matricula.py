class Matricula():
    def __init__(self, aluno, disciplina):
        self.aluno = aluno
        self.disciplina = disciplina
        self.nota = 0
        self.frequencia = 0
        self.status = "Matriculado"

    def registrar_nota(self, nota):
        if 0 <= nota <= 10:
            self.nota = nota
            self.atualizar_status()
        else:
            raise ValueError("A nota deve estar entre 0 e 10")
        
    def registrar_frequencia(self, frequencia):
        if 0 <= frequencia <= 100:
            self.frequencia = frequencia
            self.atualizar_status()
        else:
            raise ValueError("A frequencia deve estar entre 0 e 100")
    

    def atualizar_status(self):
        if self.frequencia < 75:
            self.status = "Reprovado por falta"
        if self.nota < 5:
            self.status = "Reprovado"
        if self.nota >= 5 and self.frequencia >= 75:
            self.status = "Aprovado"

    def __str__(self):
        return (f"Aluno: {self.aluno.nome}"
                f"Disciplina: {self.disciplina.nome}"
                f"Nota: {self.nota}"
                f"Frequência: {self.frequencia}%"
                f"Status:{self.status}")