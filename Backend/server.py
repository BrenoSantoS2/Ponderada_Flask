from flask import Flask,render_template
from pathlib import Path

from database import get_logs
import robo_functions

app = Flask(__name__, template_folder=Path(__file__).parent.parent / "Frontend")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_data')
def get_data():

    log_html = "<ul>"
    for log in get_logs():
        log_html += f"<li>{log['robot_action']} - {log['date']} - {log['time']}</li>"
    log_html += "</ul>"
    
    return log_html

@app.route('/robot_is_connected')
def robot_is_connected():
    if robo_functions.find_port()[1] == True:
        return "O robo foi conectado com sucesso! Pode começar a usar a ferramenta."
    else:    
        return "O robo não foi conectado. Verifique a conexão e tente novamente."

if __name__ == '__main__':
    app.run(debug=True)




