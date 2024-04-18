import random

class Evento:
    def __init__(self, nome, data, horario, local, duracao, valor_base):
        self.nome = nome
        self.data = data
        self.horario = horario
        self.local = local
        self.duracao = duracao
        self.valor_base = valor_base
        self.participantes = random.randint(50, 200)  # Número aleatório de participantes
        self.valor = self.calcular_valor()
    
    def calcular_valor(self):
        # Método para calcular o valor do evento com base na quantidade de participantes
        return self.valor_base * self.participantes
    
    def calcular_lucro(self):
        # Método para calcular o lucro do evento
        return self.valor - self.custo()
    
    def custo(self):
        # Método para calcular o custo do evento (para simplificar, usaremos 30% do valor)
        return 0.3 * self.valor
    
    def __str__(self):
        return f"{self.nome} - {self.data}, {self.horario}, {self.local}"
    
    def exibir_detalhes(self):
        return f"Nome: {self.nome}, Data: {self.data}, Horário: {self.horario}, Local: {self.local}, Duração: {self.duracao} horas, Valor: R$ {self.valor:.2f}, Participantes: {self.participantes}"


class Palestra(Evento):
    def __init__(self, nome, data, horario, local, duracao, palestrante, tema):
        super().__init__(nome, data, horario, local, duracao, 50)  # Valor base para palestras
        self.palestrante = palestrante
        self.tema = tema
    
    def __str__(self):
        return f"Palestra: {self.nome} - {self.data}, {self.horario}, {self.local}"
    
    def exibir_detalhes(self):
        return super().exibir_detalhes() + f", Palestrante: {self.palestrante}, Tema: {self.tema}"


class Workshop(Evento):
    def __init__(self, nome, data, horario, local, duracao, instrutor, vagas):
        super().__init__(nome, data, horario, local, duracao, 100)  # Valor base para workshops
        self.instrutor = instrutor
        self.vagas = vagas
    
    def __str__(self):
        return f"Workshop: {self.nome} - {self.data}, {self.horario}, {self.local}"
    
    def exibir_detalhes(self):
        return super().exibir_detalhes() + f", Instrutor: {self.instrutor}, Vagas: {self.vagas}"


class Conferencia(Evento):
    def __init__(self, nome, data, horario, local, duracao, organizador, participantes):
        super().__init__(nome, data, horario, local, duracao, 150)  # Valor base para conferências
        self.organizador = organizador
        self.participantes = participantes
    
    def __str__(self):
        return f"Conferência: {self.nome} - {self.data}, {self.horario}, {self.local}"
    
    def exibir_detalhes(self):
        return super().exibir_detalhes() + f", Organizador: {self.organizador}, Participantes: {self.participantes}"


class Show(Evento):
    def __init__(self, nome, data, horario, local, duracao, banda, estilo_musical):
        super().__init__(nome, data, horario, local, duracao, 200)  # Valor base para shows
        self.banda = banda
        self.estilo_musical = estilo_musical
    
    def __str__(self):
        return f"Show: {self.nome} - {self.data}, {self.horario}, {self.local}"
    
    def exibir_detalhes(self):
        return super().exibir_detalhes() + f", Banda: {self.banda}, Estilo Musical: {self.estilo_musical}"


def cadastrar_evento():
    print("Opções de eventos:")
    print("1 - Palestra")
    print("2 - Workshop")
    print("3 - Conferência")
    print("4 - Show")
    opcao = int(input("Escolha o tipo de evento que deseja cadastrar: "))

    nome = input("Digite o nome do evento: ")
    data = input("Digite a data do evento (DD/MM/AAAA): ")
    horario = input("Digite o horário do evento: ")
    local = input("Digite o local do evento: ")
    duracao = float(input("Digite a duração do evento em horas: "))

    if opcao == 1:
        palestrante = input("Digite o nome do palestrante: ")
        tema = input("Digite o tema da palestra: ")
        return Palestra(nome, data, horario, local, duracao, palestrante, tema)
    elif opcao == 2:
        instrutor = input("Digite o nome do instrutor: ")
        vagas = int(input("Digite o número de vagas disponíveis: "))
        return Workshop(nome, data, horario, local, duracao, instrutor, vagas)
    elif opcao == 3:
        organizador = input("Digite o nome do organizador: ")
        participantes = int(input("Digite o número de participantes confirmados: "))
        return Conferencia(nome, data, horario, local, duracao, organizador, participantes)
    elif opcao == 4:
        banda = input("Digite o nome da banda: ")
        estilo_musical = input("Digite o estilo musical do show: ")
        return Show(nome, data, horario, local, duracao, banda, estilo_musical)
    else:
        print("Opção inválida")


# Criação de eventos
eventos = []

# Menu principal
while True:
    print("\nMenu Principal")
    print("1 - Visualizar Eventos")
    print("2 - Cadastrar Novo Evento")
    print("3 - Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print("\nEventos Cadastrados:")
        for evento in eventos:
            print(evento)
            print(evento.exibir_detalhes())
            print()
    elif opcao == 2:
        novo_evento = cadastrar_evento()
        eventos.append(novo_evento)
        print("Evento cadastrado com sucesso!")
    elif opcao == 3:
        break
    else:
        print("Opção inválida")
