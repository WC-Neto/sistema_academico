from faker import Faker
import random


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


def gerar_alunos(n):
    fake = Faker()
    alunos = []

    for _ in range(n):
        nome = fake.name()
        matricula = fake.unique.random_int(min=1000, max=9999)
        data_nascimento = fake.date_of_birth(minimum_age=18, maximum_age=25)
        sexo = random.choice(['Masculino', 'Feminino'])
        endereco = fake.address().replace('\n', ', ')
        telefone = fake.phone_number()
        email = fake.ascii_email()

        aluno = Aluno(nome, matricula, data_nascimento,
                      sexo, endereco, telefone, email)
        alunos.append(aluno)

    return alunos


lista_de_alunos = gerar_alunos(5)

for aluno in lista_de_alunos:
    aluno.exibir_informacoes()


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
              self.professor.nome if self.professor else 'Nenhum professor alocado'}")
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

    def consultar_disciplina(self):
        return self.disciplina

    def exibir_informacoes(self):
        print(f"Nome da Turma: {self.nome}")
        print(f"Código: {self.codigo}")
        print(f"Disciplina: {self.disciplina.nome}")
        print(f"Professor: {self.professor.nome}")
        print(f"Alunos ( Matrículas): {', '.join(
            self.alunos) if self.alunos else 'Nenhum aluno cadastrado'}")
        print('-' * 30)


def consultar_alunos_matriculados(turma):
    return turma.alunos
