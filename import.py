from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def buscar_alunos():
    conn = sqlite3.connect('escola.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM alunos")
    alunos = cursor.fetchall()
    conn.close()
    return alunos

@app.route('/')
def listar_alunos():
    alunos = buscar_alunos()
    return render_template('index.html', alunos=alunos)

if __name__ == '__main__':
    app.run(debug=True)

