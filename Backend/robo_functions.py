from serial.tools import list_ports
from Backend.moveJ import Arm

#Define alguns parâmetros (Instânciando Typer, Definindo o Spiner e Listanto as portas).
available_ports = list_ports.comports()

# Encontra automaticamente a porta em que o robô está conectado
for port in available_ports:
    if "Dispositivo Serial USB" in port.description:
        chosen_port = port.device
        print(f"Porta encontrada: {chosen_port}")
        break
else:
    print("Nenhuma porta encontrada para o robô.")
    raise SystemExit(1)

#Instancia a biblioteca do robo.
robot = Arm(port=chosen_port, verbose=False)

# Função responsável por iniciar a ferramenta conectado ao robo
def initialize_tool():
    robot.wait(200)
    robot.suck(True)

# Função responsável por desligar a ferramenta conectado ao robo
def turn_off_tool():
    robot.wait(200)
    robot.suck(False)

# Função responsável por levar ao robo de volta a posição inicial
def home():
    robot.wait(300)
    robot.movej_to(230, 1, 159, 0, wait=True)

# Função responsável por mover o robo para a distância e eixo escolhido pelo usuário
def move():
    actual_position = robot.pose()
    x,y,z,w = actual_position[:4]
    
    chosen_axle = inquirer.prompt([
    inquirer.List("axle",message="Para qual eixo você quer que o robo se mova: ", choices=["Eixo X","Eixo Y", "Eixo Z"])
    ])["axle"]

    chosen_distance = inquirer.prompt([
    inquirer.Text("distance",message="Digite a distância do movimento desejado: ")
    ])["distance"]

    if chosen_axle == "Eixo X":
        robot.wait(300)
        robot.movej_to(x + float(chosen_distance), y, z, w, wait=True)
    
    elif chosen_axle == "Eixo Y":
        robot.wait(300)
        robot.movej_to(x, y + float(chosen_distance), z, w, wait=True)
    
    elif chosen_axle == "Eixo Z":
        robot.wait(300)
        robot.movej_to(x, y, z + float(chosen_distance), w, wait=True)

# Função responsável por mostrar no console a localização atual do robo
def actual_location():
    actual_position = robot.pose()
    print(f"The actual robot position is: {actual_position}")

# Função responsável fechar o looping e fechar a conexão com robo
def turn_off_robot():
    global running
    running = False