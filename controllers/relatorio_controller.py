class RelatorioController:
    def gerar_relatorio(self, disciplina):
        relatorio = []
        relatorio.append("---- RELATÓRIO ----")
        relatorio.append(
        f"Disciplina: {disciplina.nome} | Código: {disciplina.codigo}"
        )
        relatorio.append(f"{disciplina.professor}")
        
        if len(disciplina.matriculas) > 0:
            relatorio.append("\nAlunos:")
            for matricula in disciplina.matriculas:
                relatorio.append(f"Nome: {matricula.aluno} | Matrícula: {matricula.aluno.ra} | "
                                 f"Status: {matricula.status}")
        else:
            relatorio.append("\nNenhum aluno matriculado.")

        return "\n".join(relatorio)
