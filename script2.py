import schedule
import time
import smtplib
from email.mime.text import MIMEText

def enviar_lembrete():
    conn = sqlite3.connect('agendamentos.db')
    cursor = conn.cursor()
    cursor.execute("SELECT nome, email, data FROM agendamentos WHERE data = date('now')")
    agendamentos = cursor.fetchall()
    for agendamento in agendamentos:
        nome, email, data = agendamento
        msg = MIMEText(f"Olá {nome}, este é um lembrete para sua consulta no dia {data}.")
        msg['Subject'] = 'Lembrete de Consulta'
        msg['From'] = 'seuemail@example.com'
        msg['To'] = email
        with smtplib.SMTP('smtp.example.com') as server:
            server.login('seuemail@example.com', 'senha')
            server.sendmail('seuemail@example.com', email, msg.as_string())
    conn.close()

schedule.every().day.at("08:00").do(enviar_lembrete)

while True:
    schedule.run_pending()
    time.sleep(1)
