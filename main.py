from controllers.aluno_controller import AlunoController
from controllers.professor_controller import ProfessorController
from controllers.disciplina_controller import DisciplinaController
from controllers.relatorio_controller import RelatorioController


def main():
    print("\n===== INICIANDO TESTES DO SISTEMA =====\n")

    aluno_controller = AlunoController()
    professor_controller = ProfessorController()
    disciplina_controller = DisciplinaController()
    relatorio_controller = RelatorioController()

    # 1) Cadastro de professor
    print("1) CADASTRANDO PROFESSOR")
    professor = professor_controller.cadastrar("Henrique", "henrique@unb.br")
    print(professor)
    print("-" * 50)

    # 2) Cadastro de alunos
    print("2) CADASTRANDO ALUNOS")
    aluno1 = aluno_controller.cadastrar("João Pedro", "joao@aluno.com", "2024001")

    aluno2 = aluno_controller.cadastrar("Maria Souza", "maria@aluno.com", "2024002")

    aluno3 = aluno_controller.cadastrar("Ana Clara", "ana@aluno.com", "2024003")

    for aluno in aluno_controller.listar():
        print(aluno)

    print("-" * 50)

    # 3) Cadastro de disciplina
    print("3) CADASTRANDO DISCIPLINA")
    disciplina = disciplina_controller.cadastrar(
        "Programação Orientada a Objetos",
        "POO001",
        professor
    )
    print(disciplina)
    print(f"Professor responsável: {disciplina.professor}")
    print("-" * 50)

    # 4) Matrícula de alunos
    print("4) MATRICULANDO ALUNOS NA DISCIPLINA")
    resultado1 = disciplina.matricular_aluno(aluno1)
    resultado2 = disciplina.matricular_aluno(aluno2)
    resultado3 = disciplina.matricular_aluno(aluno3)

    print(f"{aluno1.nome} matriculado? {resultado1}")
    print(f"{aluno2.nome} matriculado? {resultado2}")
    print(f"{aluno3.nome} matriculado? {resultado3}")

    print("-" * 50)

    # 5) Teste de matrícula duplicada
    print("5) TESTANDO MATRÍCULA DUPLICADA")
    duplicada = disciplina.matricular_aluno(aluno1)
    print(f"Tentativa de matricular {aluno1.nome} novamente: {duplicada}")
    print("-" * 50)

    # 6) Listagem de alunos matriculados
    print("6) LISTANDO ALUNOS MATRICULADOS NA DISCIPLINA")
    alunos_matriculados = disciplina_controller.listar_alunos(disciplina)
    for aluno in alunos_matriculados:
        print(aluno)
    print("-" * 50)

    # 7) Lançamento de notas e frequência
    print("7) LANÇANDO NOTAS E FREQUÊNCIAS")
    disciplina_controller.lancar_nota(disciplina, "2024001", 8.5)
    disciplina_controller.lancar_nota(disciplina, "2024002", 4.0)
    disciplina_controller.lancar_nota(disciplina, "2024003", 7.0)

    disciplina_controller.lancar_frequencia(disciplina, "2024001", 90)
    disciplina_controller.lancar_frequencia(disciplina, "2024002", 80)
    disciplina_controller.lancar_frequencia(disciplina, "2024003", 60)

    for matricula in disciplina.matriculas:
        print(
            f"{matricula.aluno.nome} -> Nota: {matricula.nota} | "
            f"Frequência: {matricula.frequencia}% | "
            f"Status final: {matricula.status}"
        )
    print("-" * 50)

    # 8) Gerando relatório final
    print("8) RELATÓRIO FINAL DA DISCIPLINA")
    relatorio = relatorio_controller.gerar_relatorio(disciplina)
    print(relatorio)
    print("-" * 50)

    print("\n===== FIM DOS TESTES =====")


if __name__ == "__main__":
    main()