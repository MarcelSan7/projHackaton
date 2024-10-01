from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

@app.route('/agendar', methods=['POST'])
def agendar():
    nome = request.form['nome']
    email = request.form['email']
    data = request.form['data']
    tipo = request.form['tipo']
    medico = request.form['medico']
    # Salvar no banco de dados
    conn = sqlite3.connect('agendamentos.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO agendamentos (nome, email, data, tipo, medico) VALUES (?, ?, ?, ?, ?)", (nome, email, data, tipo, medico))
    conn.commit()
    conn.close()
    return "Agendamento realizado com sucesso!"

if __name__ == '__main__':
    app.run(debug=True)
