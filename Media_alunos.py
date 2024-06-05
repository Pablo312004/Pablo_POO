import csv
import flet as ft

# Criação do arquivo CSV com os dados dos alunos
students_data = [
    ["nome", "idade", "nota"],
    ["John", 16, 85],
    ["Bob", 15, 90],
    ["Charlie", 14, 78],
    ["David", 15, 88],
    ["Evellin", 17, 92],
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students_data)

# Leitura dos dados do arquivo students.csv
students = []

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append(row)

# Cálculo da média das notas - Parte 1
total_notas = 0
num_alunos = len(students)

for student in students:
    total_notas += int(student["nota"])

media_notas = total_notas / num_alunos

# Adicionando a média das notas nos dados de todos os alunos
for student in students:
    student["media_notas"] = media_notas

# Escrita dos dados processados em um novo arquivo CSV
with open("students_with_average.csv", "w", newline="") as file:
    fieldnames = ["nome", "idade", "nota", "media_notas"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(students)


# Função para encontrar as maiores e menores notas
def encontrar_maior_menor_nota(students):
    maior_nota = max(students, key=lambda x: int(x["nota"]))
    menor_nota = min(students, key=lambda x: int(x["nota"]))

    return maior_nota, menor_nota


maior_nota, menor_nota = encontrar_maior_menor_nota(students)


# Criação da interface gráfica com Flet
def main(page: ft.Page):
    page.title = "Dados dos Alunos"

    # Função para carregar dados dos alunos
    def carregar_dados():
        students = []
        with open("students.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append(row)
        return students

    # Função para calcular a média das notas dos alunos
    def calcular_media(students):
        total_notas = 0
        num_alunos = len(students)
        for student in students:
            total_notas += int(student["nota"])
        return total_notas / num_alunos

    # Função para poder encontrar as maiores e menores notas
    def encontrar_maior_menor(students):
        maior_nota = max(students, key=lambda x: int(x["nota"]))
        menor_nota = min(students, key=lambda x: int(x["nota"]))
        return maior_nota, menor_nota

    # Carregar os dados dos alunos
    students = carregar_dados()
    media_notas = calcular_media(students)
    maior_nota, menor_nota = encontrar_maior_menor(students)

    # Componentes da interface gráfica. Utilizada a flet
    media_label = ft.Text(f"Média das notas: {media_notas:.2f}", size=20, weight="bold")
    maior_nota_label = ft.Text(
        f"Maior Nota: {maior_nota['nota']} ({maior_nota['nome']})", size=18
    )
    menor_nota_label = ft.Text(
        f"Menor Nota: {menor_nota['nota']} ({menor_nota['nome']})", size=18
    )

    table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Nome")),
            ft.DataColumn(ft.Text("Idade")),
            ft.DataColumn(ft.Text("Nota")),
        ],
        rows=[
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(student["nome"])),
                    ft.DataCell(ft.Text(student["idade"])),
                    ft.DataCell(ft.Text(student["nota"])),
                ]
            )
            for student in students
        ],
    )

    page.add(media_label, maior_nota_label, menor_nota_label, table)


ft.app(target=main)
