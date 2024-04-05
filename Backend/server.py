from flask import Flask,render_template, request
from flask_cors import CORS
from pathlib import Path

from database import get_logs, insert_log
import robo_functions

app = Flask(__name__, template_folder=Path(__file__).parent.parent / "Frontend")
CORS(app)

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
        return "O robo está conectado! Pode começar a usar a ferramenta."
    else:    
        return "O robo está desconectado. Verifique a conexão e tente novamente."

@app.route('/initialize_tool', methods=['POST','GET'])
def initialize_tool():
    robo_functions.initialize_tool()
    insert_log("Ferramenta inicializada")
    return "Ferramenta inicializada com sucesso!"

@app.route('/turn_off_tool', methods=['POST','GET'])
def turn_off_tool():
    robo_functions.turn_off_tool()
    insert_log("Ferramenta desligada")
    return "Ferramenta desligada com sucesso!"

@app.route('/home_position' , methods=['GET'])
def home_position():
    robo_functions.home()
    insert_log("Robo levado a posição inicial")
    return "Robo levado a posição inicial com sucesso!"

@app.route('/move', methods=['POST'])
def move():
    axle = request.form['axle']
    distance = int(request.form['distance'])
    
    robo_functions.move(axle,distance)
    insert_log(f"Robo movido {distance} no eixo {axle}")
    return f"Robo movido {distance} no eixo {axle} com sucesso!"

@app.route('/actual_location', methods=['GET'])
def actual_location():
    insert_log("Localização atual do robo foi pega")
    return robo_functions.actual_location()

if __name__ == '__main__':
    app.run(debug=True)




