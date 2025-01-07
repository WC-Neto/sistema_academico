class Aluno:
    def __init__(self, nome, matricula, data_nascimento, sexo, endereco, telefone, email):
        self.nome = nome
        self.matricula = matricula
        self.data_nascimento = data_nascimento
        self.sexo = sexo
        self.endereco = endereco
        self.telefone = telefone
        self.email = email

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Matrícula: {self.matricula}")
        print(f"Data de Nascimento: {self.data_nascimento}")
        print(f"Sexo: {self.sexo}")
        print(f"Endereço: {self.endereco}")
        print(f"Telefone: {self.telefone}")
        print(f"Email: {self.email}")
        print('-' * 30)


class Professor:
    def __init__(self, nome, matricula, data_nascimento, sexo, endereco, telefone, email, disciplina):
        self.nome = nome
        self.matricula = matricula
        self.data_nascimento = data_nascimento
        self.sexo = sexo
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self.disciplina = disciplina

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Matrícula: {self.matricula}")
        print(f"Data de Nascimento: {self.data_nascimento}")
        print(f"Sexo: {self.sexo}")
        print(f"Endereço: {self.endereco}")
        print(f"Telefone: {self.telefone}")
        print(f"Email: {self.email}")
        print(f"Disciplina: {self.disciplina}")
        print('-' * 30)


class Disciplina:
    def __init__(self, nome, codigo, carga_horaria, professor=None):
        self.nome = nome
        self.codigo = codigo
        self.carga_horaria = carga_horaria
        self.professor = professor

    def alocar_professor(self, professor):
        self.professor = professor
        print(f"Professor {professor.nome} alocado à disciplina {
              self.nome} com sucesso.")

    def exibir_professor_alocado(self):
        if self.professor:
            print(f"Professor alocado na disciplina {
                  self.nome}: {self.professor.nome}")
        else:
            print(f"Nenhum professor alocado na disciplina {self.nome}.")

    def exibir_informacoes(self):
        print(f"Nome da Disciplina: {self.nome}")
        print(f"Código: {self.codigo}")
        print(f"Carga Horária: {self.carga_horaria} horas")
        print(f"Professor: {
              self.professor.nome if self.professor else 'Nenhum professor alocado\n'}")
        print('-' * 30)


class Turma:
    def __init__(self, nome, codigo, disciplina, professor, alunos=None):
        self.nome = nome
        self.codigo = codigo
        self.disciplina = disciplina
        self.professor = professor
        self.alunos = alunos if alunos is not None else []

    def alocar_disciplina(self, disciplina):
        self.disciplina = disciplina
        print(f"Disciplina {disciplina.nome} alocada à turma {
              self.nome} com sucesso.")

    def exibir_informacoes(self):
        print(f"Nome da Turma: {self.nome}")
        print(f"Código: {self.codigo}")
        print(f"Disciplina: {self.disciplina.nome}")
        print(f"Professor: {self.professor.nome}")
        print(f"Alunos ( Matrículas): {', '.join(
            [aluno.matricula for aluno in self.alunos]) if self.alunos else 'Nenhum aluno cadastrado\n'}")
        print('-' * 30)


def menu():
    alunos = []
    professores = []
    turmas = []

    while True:
        print("\nMenu:")
        print("1. Cadastrar Aluno")
        print("2. Cadastrar Professor")
        print("3. Alocar Disciplina a Professor")
        print("4. Cadastrar Turma")
        print("5. Consultar Alunos Cadastrados")
        print("6. Consultar Professores Cadastrados")
        print("7. Consultar Turmas Cadastradas")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Digite o nome do aluno: ")
            matricula = input("Digite a matrícula do aluno: ")
            data_nascimento = input(
                "Digite a data de nascimento (dd/mm/aaaa): ")
            sexo = input("Digite o sexo do aluno (Masculino/Feminino): ")
            endereco = input("Digite o endereço do aluno: ")
            telefone = input("Digite o telefone do aluno: ")
            email = input("Digite o email do aluno: ")

            aluno = Aluno(nome, matricula, data_nascimento,
                          sexo, endereco, telefone, email)
            alunos.append(aluno)
            print("Aluno cadastrado com sucesso!")

        elif opcao == '2':
            nome = input("Digite o nome do professor: ")
            matricula = input("Digite a matrícula do professor: ")
            data_nascimento = input(
                "Digite a data de nascimento (dd/mm/aaaa): ")
            sexo = input("Digite o sexo do professor (Masculino/Feminino): ")
            endereco = input("Digite o endereço do professor: ")
            telefone = input("Digite o telefone do professor: ")
            email = input("Digite o email do professor: ")
            disciplina = input("Digite a disciplina que o professor leciona: ")

            professor = Professor(
                nome, matricula, data_nascimento, sexo, endereco, telefone, email, disciplina)
            professores.append(professor)
            print("Professor cadastrado com sucesso!\n")

        elif opcao == '3':
            if not professores:
                print("Nenhum professor cadastrado!\n")
                continue

            nome_prof = input("Digite o nome do professor a ser alocado: ")
            for professor in professores:
                if professor.nome.lower() == nome_prof.lower():
                    disciplina = input("Digite o nome da disciplina: ")
                    codigo = input("Digite o código da disciplina: ")
                    carga_horaria = input("Digite a carga horária: ")
                    disc = Disciplina(disciplina, codigo, carga_horaria)
                    disc.alocar_professor(professor)
                    print("Disciplina alocada ao professor com sucesso!")
                    break
            else:
                print("Professor não encontrado!\n")

        elif opcao == '4':
            if not professores:
                print("Nenhum professor cadastrado!\n")
                continue

            nome_turma = input("Digite o nome da turma: ")
            codigo_turma = input("Digite o código da turma: ")
            disciplina = input("Digite a disciplina da turma: ")

            professor_nome = input("Digite o nome do professor da turma: ")
            for professor in professores:
                if professor.nome.lower() == professor_nome.lower():
                    turma = Turma(nome_turma, codigo_turma,
                                  disciplina, professor)
                    turmas.append(turma)
                    print("Turma cadastrada com sucesso!\n")
                    break
            else:
                print("Professor não encontrado!\n")

        elif opcao == '5':
            print("Alunos Cadastrados:")
            for aluno in alunos:
                aluno.exibir_informacoes()

        elif opcao == '6':
            print("Professores Cadastrados:")
            for professor in professores:
                professor.exibir_informacoes()

        elif opcao == '7':
            print("Turmas Cadastradas:")
            for turma in turmas:
                turma.exibir_informacoes()

        elif opcao == '0':
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida! Por favor, escolha uma opção válida.\n")


menu()
