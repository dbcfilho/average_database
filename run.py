import tkinter as tk
from tkinter import messagebox
import sqlite3

def criar_tabela():
    conn = sqlite3.connect('escola.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS alunos (
                    id INTEGER PRIMARY KEY,
                    nome TEXT,
                    presencas INTEGER,
                    faltas INTEGER,
                    nota1 REAL,
                    nota2 REAL,
                    media REAL,
                    frequencia REAL
                 )''')

    conn.commit()
    conn.close()

def calcular_situacao(media, frequencia):
    if media >= 6.0 and frequencia >= 75:
        return "Aprovado"
    else:
        return "Reprovado"

def adicionar_aluno():
    nome = nome_entry.get()
    presencas = int(presencas_entry.get())
    faltas = int(faltas_entry.get())
    nota1 = float(nota1_entry.get())
    nota2 = float(nota2_entry.get())

    conn = sqlite3.connect('escola.db')
    c = conn.cursor()

    media = (nota1 + nota2) / 2
    total_aulas = presencas + faltas
    frequencia = (presencas / total_aulas) * 100

    situacao = calcular_situacao(media, frequencia)

    c.execute("INSERT INTO alunos (nome, presencas, faltas, nota1, nota2, media, frequencia) VALUES (?, ?, ?, ?, ?, ?, ?)",
              (nome, presencas, faltas, nota1, nota2, media, frequencia))

    conn.commit()
    conn.close()

    messagebox.showinfo("Sucesso", f"Aluno {nome} adicionado com sucesso. Situação: {situacao}")

# Cria a janela principal
root = tk.Tk()
root.title("Controle de Alunos")

# Cria os widgets da interface
nome_label = tk.Label(root, text="Nome:")
nome_label.pack()
nome_entry = tk.Entry(root)
nome_entry.pack()

presencas_label = tk.Label(root, text="Presenças:")
presencas_label.pack()
presencas_entry = tk.Entry(root)
presencas_entry.pack()

faltas_label = tk.Label(root, text="Faltas:")
faltas_label.pack()
faltas_entry = tk.Entry(root)
faltas_entry.pack()

nota1_label = tk.Label(root, text="Nota 1:")
nota1_label.pack()
nota1_entry = tk.Entry(root)
nota1_entry.pack()

nota2_label = tk.Label(root, text="Nota 2:")
nota2_label.pack()
nota2_entry = tk.Entry(root)
nota2_entry.pack()

adicionar_button = tk.Button(root, text="Adicionar Aluno", command=adicionar_aluno)
adicionar_button.pack()

if __name__ == "__main__":
    criar_tabela()
    root.mainloop()
